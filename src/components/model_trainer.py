import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingClassifier, RandomForestRegressor

from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

from sklearn.metrics import mean_absolute_error

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainerConfig():
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Neighbors Regressor": KNeighborsRegressor(),
                "Random Forest Regressor": RandomForestRegressor(),
                "Gradient Boosting Classifier": GradientBoostingClassifier(),
                "AdaBoost Regressor": AdaBoostRegressor(),
                "XGBRegressor": XGBRegressor(), 
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
            }

            model_report:dict = evaluate_models(X_train=X_train, y_train=y_train, 
                                                X_test=X_test, y_test=y_test,
                                                models=models)
            
            best_model_score = min(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            if best_model_score > 1000:
                raise Exception("No best model found.")
            
            logging.info(f"Best model found: {best_model_name}")

            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )

            predicted=best_model.predict(X_test)

            mae_score = mean_absolute_error(y_test, predicted)
            return mae_score

        except Exception as e:
            raise CustomException(e,sys)