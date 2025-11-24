

from rapidfuzz import process, fuzz
from .preprocess import preprocess_text


# Symptom keywords → used to block “healthy”

SYMPTOM_KEYWORDS = [
    "spot", "spots", "dark", "brown", "black", "yellow",
    "powder", "powdery", "rot", "rust", "blight", "curl",
    "dry", "dead", "patch", "patches", "lesion", "infected",
    "disease", "sick", "wilt", "wilted", "mold", "mould",
    "hole", "holes", "discolor", "discolour"
]


# Detect plant name from text

def detect_plant(user_input):
    plants = [
        "apple", "tomato", "corn", "grape", "peach",
        "orange", "pepper", "potato", "strawberry",
        "cherry", "blueberry", "raspberry", "soybean",
        "squash"
    ]

    words = preprocess_text(user_input)

    for p in plants:
        if p in words:
            return p
    return None

def get_best_match(user_input, disease_keys):
    text = user_input.lower().strip()
    tokens = preprocess_text(user_input)
    
    has_symptom = any(word in text for word in SYMPTOM_KEYWORDS)
   
    plant = detect_plant(user_input)
    filtered = disease_keys.copy()

    if plant:
        filtered = [d for d in disease_keys if d.startswith(plant)]

        if not filtered:
            filtered = disease_keys.copy()
    
    if has_symptom:
        filtered = [d for d in filtered if "healthy" not in d.lower()]
    
    if "healthy" in text:
        filtered = [d for d in disease_keys if "healthy" in d.lower()]
    
    if not filtered:
        filtered = disease_keys.copy()
    
    inp = " ".join(tokens)
    best, score, _ = process.extractOne(inp, filtered, scorer=fuzz.WRatio)
    return best, score
