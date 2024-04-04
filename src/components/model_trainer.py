import os
import sys
from dataclasses import dataclass

import pandas as pd

from catboost import CatBoostRegressor
from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor

from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

from sklearn.metrics import mean_absolute_error, r2_score

from src.constants.hyperparameters import *
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
                "Gradient Boosting Regressor": GradientBoostingRegressor(),
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
            print(f"Best model found: {best_model_name}")

            logging.info(f"Best model fine tuning: {best_model_name}")
            # Fine-tuning the best model using RandomizedSearchCV
            if best_model_name in models.keys():
                param_distributions = {}  # Define the parameter distributions for fine-tuning

                if best_model_name == 'Random Forest Regressor':
                    param_distributions = random_forest_regressor_dict

                elif best_model_name == 'Gradient Boosting Regressor':
                    param_distributions = gradient_boosting_regressor_dict

                elif best_model_name == 'Lasso':
                    param_distributions = lasso_dict

                elif best_model_name == 'Ridge':
                    param_distributions = ridge_dict

                elif best_model_name == 'K-Neighbors Regressor':
                    param_distributions = k_neighbors_regressor_dict

                elif best_model_name == 'AdaBoost Regressor':
                    param_distributions = adaboost_regressor_dict

                elif best_model_name == 'XGBRegressor':
                    param_distributions = xgb_regressor_dict

                elif best_model_name == 'CatBoosting Regressor':
                    param_distributions = catboost_regressor_dict

                # ============================================ #
                ### After some research CatBoostRegressor gave beter results.
                ### So we will fine tune this model.
                best_model = CatBoostRegressor(verbose=False)
                best_model_name = 'Cat Boost Regressor'
                param_distributions = catboost_regressor_dict
                # ============================================ #

                # Perform RandomizedSearchCV
                random_search = RandomizedSearchCV(
                    estimator=best_model, param_distributions=param_distributions, 
                    n_iter=50, cv=5, 
                    scoring='neg_mean_absolute_error', n_jobs=-1, random_state=42
                )
                random_search.fit(X_train, y_train)
                
                # Set the best model after fine-tuning
                best_model = random_search.best_estimator_
            
            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )

            predicted=best_model.predict(X_test)

            mae = mean_absolute_error(y_test, predicted)
            r2 = r2_score(y_test, predicted)

            # Save model
            save_object(
                file_path = self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )

            # Save results as txt
            data = {
                'Model Name': best_model_name,
                'MAE': mae,
                'R2': r2
            }
            ds = pd.Series(data)
            ds.to_csv(os.path.join('artifacts','results.txt'))

            return mae

        except Exception as e:
            raise CustomException(e,sys)
        