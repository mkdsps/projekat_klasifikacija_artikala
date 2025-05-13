import re
import string

def trim(transient_tweet_text):
    return transient_tweet_text.strip()

def strip_whiteSpaces(transient_tweet_text):
    return re.sub(r'[\s]+', ' ', transient_tweet_text)

def preprocess_string(text: str) -> str:
    translator = str.maketrans('', '', string.punctuation)
    text_without_punctuation = text.translate(translator)

    pattern = r'\b([A-Z]+[0-9]+[A-Z]+[A-Z0-9]|[0-9]+[A-Z]+[0-9][A-Z0-9]*)\b'
    text_without_codes = re.sub(pattern, '', text_without_punctuation)

    result = text_without_codes.lower()
    result = trim(result)

    return strip_whiteSpaces(result)

