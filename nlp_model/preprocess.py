import nltk
from nltk.stem import WordNetLemmatizer
import re

# Download resources only the first time
nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

lemmatizer = WordNetLemmatizer()

def preprocess_text(text: str) -> str:
    if not text:
        return ""

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # Tokenize
    tokens = nltk.word_tokenize(text)

    # Lemmatize
    tokens = [lemmatizer.lemmatize(t) for t in tokens]

    return " ".join(tokens)
