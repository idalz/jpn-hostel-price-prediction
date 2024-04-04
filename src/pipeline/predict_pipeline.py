import sys 
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = 'artifacts/preprocessor.pkl'
            preprocessor = load_object(file_path=preprocessor_path)
            model_path = 'artifacts/model.pkl'
            model = load_object(file_path=model_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return np.round(pred)
        
        except Exception as e:
            raise CustomException(e,sys)
        

class CustomData:
    def __init__(
            self,
            city: str,        
            distance_km: float,
            summary_score: float,
            rating_band: str,
            atmosphere: float, 
            cleanliness: float,
            facilities: float,
            location_y: float, 
            security: float, 
            staff: float,
            valueformoney: float
    ):
        self.city = city     
        self.distance_km = distance_km
        self.summary_score = summary_score
        self.rating_band = rating_band
        self.atmosphere = atmosphere 
        self.cleanliness = cleanliness
        self.facilities = facilities
        self.location_y = location_y
        self.security = security
        self.staff = staff
        self.valueformoney = valueformoney
    
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {    
            "city": [self.city],
            "summary_score": [self.summary_score],
            "rating_band": [self.rating_band],
            "atmosphere": [self.atmosphere],
            "cleanliness": [self.cleanliness],
            "facilities": [self.facilities],
            "location_y": [self.location_y],
            "security": [self.security],
            "staff": [self.staff],
            "valueformoney": [self.valueformoney],      
            "distance_km": [self.distance_km]
            }
            
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)
        