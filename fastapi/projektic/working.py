from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

import re
import string
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import joblib

from sklearn.base import BaseEstimator, TransformerMixin
from preprocessor import preprocess_string
import sys

class TextPreprocessor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return [preprocess_string(text) for text in X]


# Dodajte ovo pre učitavanja pipeline-a
sys.modules['__main__'].TextPreprocessor = TextPreprocessor
pipeline = joblib.load('pipeline.pkl')


pipeline = joblib.load('pipeline.pkl')

key_to_category = {
    1: 'bela-tehnika',
    5: 'lepota-i-zdravlje',
    3: 'it-uredjaji',
    8: 'telefonija',
    9: 'tv-video-i-foto-tehnika',
    4: 'kucni-aparati',
    0: 'alati-i-bastenska-oprema',
    6: 'pokucstvo',
    7: 'sport-i-rekreacija',
    2: 'grejanje-i-klimatizacija'
}

def predict_(lista):
    predictions = pipeline.predict(lista)

    return [key_to_category[x.item()] for x in predictions]

app = FastAPI()

class Sentences(BaseModel):
    recenice: List[str]

@app.post(
    "/predict", 
    description="Predicts a category based on the input sentences."
)
def predict(request: Sentences):
    input = request.recenice
    predicted_category = predict_(input)
    return {'predictions': predicted_category}
