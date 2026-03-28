import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import os

def build_model(input_shape):
    """
    Builds a simple neural network for burnout prediction.
    """
    model = Sequential([
        Dense(64, activation='relu', input_shape=(input_shape,)),
        Dropout(0.2),
        Dense(32, activation='relu'),
        Dense(1, activation='linear')  # Assuming burnout score is a continuous value
    ])
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

def save_model(model, path='models/burnout_model.h5'):
    """
    Saves the trained model to the specified path.
    """
    model.save(path)
    print(f"Model saved to {path}")

def load_trained_model(path='models/burnout_model.h5'):
    """
    Loads the trained model from the specified path.
    """
    if os.path.exists(path):
        return tf.keras.models.load_model(path)
    return None
