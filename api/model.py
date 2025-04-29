import joblib
import numpy as np

model = joblib.load("datasets/mental_health_model.pkl")
label_encoder = joblib.load("datasets/label_encoder.pkl")


def predict_mental_health(input_data):
    """
    Takes a list of 16 responses and returns the predicted mental health label.
    """
    
    prediction = model.predict([input_data])
    label = label_encoder.inverse_transform(prediction)

    return label[0]
