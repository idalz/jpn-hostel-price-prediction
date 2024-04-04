from flask import Flask, request,render_template

from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.constants.constants_html import *

app = Flask(__name__)

@app.route('/')
def index():
    content = index_dict
    return render_template('index.html', content=content)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    content = predict_dict
    if request.method=='GET':
        return render_template('predict.html',content=content)
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

        return render_template('predict.html', results=results[0], content=content)
    
@app.route("/about", methods=['GET'])
def about():
    content = about_dict
    return render_template('about.html', content=content)

if __name__=='__main__':
    #app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(host="0.0.0.0", port=8080)
