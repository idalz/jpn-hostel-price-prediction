import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, RobustScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()        

    def get_data_transformer_object(self):
        """
        This function is responsible for data transformation.
        """
        try:
            num_features = ['summary.score','atmosphere',
                        'cleanliness','facilities','location.y',
                        'security','staff','valueformoney', 'distance_km']
            cat_features =  ['City', 'rating.band']

            num_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy="median")),
                    ('scaler', RobustScaler())
                ]
            )

            logging.info("Numerical columns standard scaling completed.")

            cat_pipeline = Pipeline(
                steps= [
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('one_hot_encoder',OneHotEncoder(handle_unknown='ignore', drop='first')) 
                ]
            )

            logging.info("Categorical columns encoding completed.")

            preprocessor = ColumnTransformer(
                transformers = [
                    ('num_pipeline', num_pipeline, num_features),
                    ('cat_pipeline', cat_pipeline, cat_features),
                ],
                remainder='drop'
            )

            logging.info("Column Transformer completed.")

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_extreme_outlier_indices(self, feature, data):
        """
        This function returns the index of extreme outliers of a feature.
        """
        try:
            # Calculate the IQR
            Q1 = data[feature].quantile(0.25)
            Q3 = data[feature].quantile(0.75)
            IQR = Q3 - Q1

            # Define the upper and lower bounds 
            #(4.5 in order to detect outliers significantly far from the median)
            lower_bound = Q1 - 4.5 * IQR
            upper_bound = Q3 + 4.5 * IQR

            # Identify extreme outliers
            extreme_outliers = data[(data[feature] < lower_bound) | (data[feature] > upper_bound)]

            # Return indices
            return extreme_outliers.index
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self, train_path, test_path):
        try:
            target_feature_name = 'price.from'

            logging.info("Reading train and test data.")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            remove_features_list = ['Unnamed: 0', 'hostel.name', 'lon', 'lat']
            logging.info("Removing irrelevant features from train and test data:", remove_features_list)
            train_df.drop(remove_features_list, axis=1, inplace=True)
            test_df.drop(remove_features_list, axis=1, inplace=True)

            logging.info("Converting categorical Distance to numerical distance_km.")
            train_df['distance_km'] = train_df['Distance'].str.extract('(\d+(\.\d+)?)').astype(float)[0]
            train_df.drop(['Distance'], axis=1, inplace=True)
            test_df['distance_km'] = test_df['Distance'].str.extract('(\d+(\.\d+)?)').astype(float)[0]
            test_df.drop(['Distance'], axis=1, inplace=True)

            logging.info("Removing significantly extreme outliers from target feature.")
            train_df.drop(self.get_extreme_outlier_indices(target_feature_name,train_df),inplace=True)
            test_df.drop(self.get_extreme_outlier_indices(target_feature_name,test_df),inplace=True)        
            

            logging.info("Obtaining transformer object.")
            transformer_obj = self.get_data_transformer_object()

            input_feature_train_df = train_df.drop(columns=[target_feature_name], axis=1)
            target_feature_train_df = train_df[target_feature_name]

            input_feature_test_df = test_df.drop(columns=[target_feature_name], axis=1)
            target_feature_test_df = test_df[target_feature_name]

            logging.info("Applying transformer object on train and test dataframe.")
            input_feature_train_arr = transformer_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = transformer_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Saving preprocessing object.")
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=transformer_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        