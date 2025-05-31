import joblib
 
model = joblib.load("model/rdf_model.joblib")
result_target = joblib.load("model/encoder_Status.joblib")

def prediction(data):
    """Making prediction
 
    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data
 
    Returns:
        str: Prediction result (Graduate, Dropout, Enrolled)
    """
    result = model.predict(data)
    final_result = result_target.inverse_transform(result)[0]
    return final_result
