import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_preprocesses_data(csv_path="data/air_quality_data.csv"):
    df=pd.read_csv(csv_path)
    df = df.dropna()
    #Features selection
    X = df[['NO2 Mean', 'O3 Mean', 'SO2 Mean', 'CO Mean']]
    df['AQI'] = df[['NO2 AQI', 'O3 AQI', 'SO2 AQI', 'CO AQI']].max(axis=1)
    y = df['AQI']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler
