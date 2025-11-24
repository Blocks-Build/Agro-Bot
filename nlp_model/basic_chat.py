from rapidfuzz import fuzz

GREETING_KEYWORDS = [
    "hi", "hello", "hey", "hei", "helo", "hlo",
    "yo", "hii", "heyy", "sup", "wassup",
    "namaste", "नमस्ते", "नमस्कार", "हेलो", "हाय"
]


HOW_ARE_YOU_KEYWORDS = [
    "how are you", "kaisa", "kaise ho", "kaisi ho", "कैसे हो", "आप कैसे"
]

THANKS_KEYWORDS = [
    "thank", "thanks", "dhanyavaad", "धन्यवाद", "shukriya", "शुक्रिया"
]

BYE_KEYWORDS = [
    "bye", "goodbye", "tata", "see you", "alvida", "अलविदा"
]


def detect_smalltalk(text: str) -> str:
    """
    Returns type of small-talk intent if found, else None.
    """

    t = text.lower().strip()

    for g in GREETING_KEYWORDS:
        if fuzz.partial_ratio(t, g) > 80:
            return "greeting"


    for h in HOW_ARE_YOU_KEYWORDS:
        if h in t:
            return "how_are_you"

    for th in THANKS_KEYWORDS:
        if th in t:
            return "thanks"

 
    for b in BYE_KEYWORDS:
        if b in t:
            return "bye"

    SYMPTOMS = [
        "spot", "spots", "dark", "brown", "black", "rot",
        "rust", "curl", "powder", "patch", "disease", "sick",
        "blight", "lesion"
    ]

    words = t.split()
    if len(words) <= 3:
        if not any(s in t for s in SYMPTOMS):
            return "greeting"

    return None


#reply
def smalltalk_reply(text: str, lang: str):
    t = detect_smalltalk(text)

    if t == "greeting":
        return "नमस्ते किसान मित्र! मैं आपकी कैसे मदद कर सकता हूँ? " if lang == "hi" \
            else "Hello! How can I assist you today? "


    if t == "how_are_you":
        return "मैं अच्छा हूँ! आपकी फसल की समस्या बताइए। " if lang == "hi" \
            else "I'm doing great! How can I help with your plants today? "

    if t == "thanks":
        return "धन्यवाद! आपको और किस चीज़ में मदद चाहिए? " if lang == "hi" \
            else "You're welcome! How else can I assist you? "

    if t == "bye":
        return "अलविदा! अपना ध्यान रखें। " if lang == "hi" \
            else "Goodbye! Take care. "

    return "मैं आपकी कैसे सहायता कर सकता हूँ?" if lang == "hi" else "How can I help you?"
