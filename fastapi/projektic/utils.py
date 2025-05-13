import re
import string
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import joblib
from preprocessor import TextPreprocessor

# Učitavanje pipeline-a
pipeline = joblib.load('pipeline.pkl')

# Kategorije
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


if __name__=='__main__':
    print(predict_(['Beko Kombinovani frižider RDSO206K40WN','Tastatura i mis']))