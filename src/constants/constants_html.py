index_dict = {
    "title": "Home",
    "quote_h2": "Craft Your <span>Dream</span> Stay",
    "quote_p": "Discover the magic of Japan without breaking the bank! Predict hostel prices effortlessly with our innovative tool.",
    "quote_button": "Make a Prediction"
}

predict_dict = {
    "title": "Hostel Information",
    "form_title": "Hostel Information Form",
    "form_button": "Predict Price"
}

about_dict = {
    "title": "About this Project",
    ### About the project
    "project_title": "About the Project",
    "project_descr": """
    <p>Navigating the diverse and dynamic landscape of hostel accommodation in Japan presents a challenge for travelers seeking to estimate costs accurately.
    With a multitude of factors influencing hostel prices, including city, distance from attractions, and various quality metrics, 
    travelers often lack the tools to make informed decisions regarding their accommodation budget. 
    Without access to sophisticated data analysis techniques, travelers risk overpaying or underestimating costs,
    leading to potential budgetary constraints or unexpected expenses during their stay.</p>

    <br><br>

    <p><strong>Our objective</strong> is to develop an advanced regressor model capable of accurately <strong>predicting hostel prices in Japan</strong>.
    Leveraging a comprehensive dataset comprising critical features such as city, distance from attractions, and summary scores, 
    our aim is to empower travelers with a precise estimation tool for hostel accommodation costs. 
    Through the creation of this regressor model, we seek to enhance the travel planning experience, 
    enabling individuals to make well-informed decisions and optimize their budget allocation for accommodation expenses 
    while exploring the rich cultural tapestry of Japan.</p>
 
    """,
    ### About the model
    "model_title": "About the Model",
    "model_descr": """
    <p>After experimenting with various models, the <strong>CatBoost Regressor</strong> was ultimately chosen due to slightly improved results.
    However, it's important to note that the model's performance still falls short of expectations. 
    Despite its selection and a pretty ok <strong>MAE of 482.22</strong> within a price range of 1000 to 4000 (with some outliers exceeding 6000),
    the low <strong>R-squared value of 0.26</strong> during evaluation indicate substantial room for improvement. 
    While these adjustments show potential for enhancement, it's evident that further refinement and exploration of alternative strategies are necessary
    to achieve satisfactory predictive performance.</p>

    """,
    ### About the data
    "data_title": "About the Data",
    "data_descr": """
    <p>The dataset used in this project was sourced from Kaggle's <a href="https://www.kaggle.com/datasets/koki25ando/hostel-world-dataset" style="color: var(--primary-color-1)";>
    Japan Hostel Dataset</a>. 
    It comprises a collection of hostel listings along with various features used for predicting hostel prices.</p>
    <p><strong>City:</strong> City name where the hostel is located</p>
    <p><strong>price.from:</strong> Minimum Price for a 1-night stay</p>
    <p><strong>Distance:</strong> Distance from the city center (km)</p>
    <p><strong>summary.score:</strong> Summary score of ratings</p>
    <p><strong>rating.band:</strong> Rating band</p>
    <p><strong>atmosphere:</strong> Rating score of atmosphere</p>
    <p><strong>cleanliness:</strong> Rating score of cleanliness</p>
    <p><strong>facilities:</strong> Rating score of facilities</p>
    <p><strong>location.y:</strong> Rating score of location</p>
    <p><strong>security:</strong> Rating score of security</p>
    <p><strong>staff:</strong> Rating score of staff</p>
    <p><strong>valueformoney:</strong> Rating score of value for money</p>
        """,
}