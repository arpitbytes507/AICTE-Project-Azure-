import joblib
#prediction function
def predict_new_data(scaler, sample_df):
    model=joblib.load('Source/aqi_model.pkl')
    sample_scaled = scaler.transform(sample_df)
    prediction = model.predict(sample_scaled)
    return prediction[0]
