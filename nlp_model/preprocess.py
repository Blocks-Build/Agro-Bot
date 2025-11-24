# nlp_model/preprocess.py

import spacy
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text: str) -> str:
    """
    Lowercase -> spaCy tokenization -> lemmas joined.
    """
    if not text:
        return ""
    doc = nlp(text.lower())
    lemmas = [token.lemma_ for token in doc if not token.is_punct and not token.is_space]
    return " ".join(lemmas)
