from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

def train(X_train, y_train, X_test, y_test):
    # Use fewer trees to speed up training
    model = RandomForestRegressor(n_estimators=10,max_depth=5,n_jobs=1,random_state=42)
    print("[INFO] Training model...")
    model.fit(X_train, y_train)
    predictions=model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    print(f"[INFO] Model Evaluation:\nMSE: {mse:.2f}, R² Score: {r2:.2f}")
    # Saving model
    print("[INFO] Saving model...")
    import joblib
    joblib.dump(model, 'Source/aqi_model.pkl')

