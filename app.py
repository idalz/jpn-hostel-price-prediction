from flask import Flask, request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import RobustScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)

app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data = CustomData(
            city = request.form.get('city'),
            distance_km = request.form.get('distance'),
            summary_score = request.form.get('summaryScore'),
            rating_band = request.form.get('ratingBand'),
            atmosphere = request.form.get('atmosphere'),
            cleanliness = request.form.get('cleanliness'),
            facilities = request.form.get('facilities'),
            location_y = request.form.get('location'),
            security = request.form.get('security'),
            staff = request.form.get('staff'),
            valueformoney = request.form.get('valueForMoney'),
        )
    
        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results=predict_pipeline.predict(pred_df)

        return render_template('home.html', results=results[0])
    
if __name__=='__main__':
    app.run(host="0.0.0.0", debug=True)
