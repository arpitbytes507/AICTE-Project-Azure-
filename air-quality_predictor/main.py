from Source.preprocesses import load_preprocesses_data
from Source.train_model import train
from Source.prediction import predict_new_data
import pandas as pd 

X_train, X_test, y_train, y_test, scaler= load_preprocesses_data('/workspaces/AICTE-Project-Azure-/air-quality_predictor/data/air_quality_data.csv')

#Model taining function
train(X_train,y_train,X_test,y_test)
#Using Sample for predicition
feature_names=['NO2 Mean', 'O3 Mean', 'SO2 Mean', 'CO Mean']
# Sample input with proper column names
sample = pd.DataFrame([[32, 65, 5.5, 1015]], columns=feature_names)
#Predict
predicted_aqi = predict_new_data(scaler, sample)
print(f"Predicted AQI: {predicted_aqi:.2f}")