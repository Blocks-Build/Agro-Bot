import re

def preprocess_text(text: str) -> str:
    if not text:
        return ""

    # Lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # Tokenize by splitting on spaces
    tokens = text.split()

    return " ".join(tokens)
