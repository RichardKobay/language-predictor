""" src/utils/predictor.py """

import joblib
from sklearn.feature_extraction.text import CountVectorizer

class Predictor:
    """ Predictor class for loading and using a pre-trained model. """
    
    def __init__(self) -> None:
        """ Initializes the Predictor with the path to the model. """
        self.model_path = "models/language_classifier.pkl"
        self.vectorizer_path = "models/vectorizer.pkl"
        self.model = joblib.load(self.model_path)
        self.vectorizer = joblib.load(self.vectorizer_path)
        self.labels = [
            'German',
            'Danish',
            'English',
            'Spanish',
            'French',
            'Italian',
            'Dutch',
            'Swedish'
        ]

    def predict(self, data: str) -> str:
        """ Predicts the output using the loaded model. """
        vectorized_data = self.vectorizer.transform([data])
        prediction = self.model.predict(vectorized_data)
        return self.labels[prediction[0]]