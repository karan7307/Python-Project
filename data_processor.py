import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """
    Loads raw student data from CSV.
    """
    return pd.read_csv(file_path)

def preprocess_data(df):
    """
    Cleans and scales data for model training/prediction.
    """
    # Placeholder for cleaning logic
    df = df.dropna()
    
    # Feature selection (example columns)
    features = ['study_hours', 'stress_level', 'sleep_hours', 'extracurricular_activities']
    X = df[features]
    y = df['burnout_score']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, y, scaler

def save_processed_data(df, path='data/processed_data.csv'):
    """
    Saves cleaned data to CSV.
    """
    df.to_csv(path, index=False)
