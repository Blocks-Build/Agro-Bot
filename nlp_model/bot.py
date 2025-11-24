
from .match import get_best_match
from .dict import plant_disease_info
from .basic_chat import detect_smalltalk, smalltalk_reply
from .translate import detect_language, translate_text

REGION_KEYWORDS = [
    "punjab", "uttar pradesh", "maharashtra", "bihar", "karnataka",
    "tamil nadu", "west bengal", "gujarat", "haryana", "assam",
    "kerala", "rajasthan", "odisha", "chhattisgarh", "jharkhand"
]


def extract_region(user_text: str) -> str:
    text = user_text.lower()
    for r in REGION_KEYWORDS:
        if r in text:
            return r.title()
    return ""


def format_detailed_english(disease_key: str, info: dict, region: str = "") -> str:
    """
    Build a readable English reply (full details). We'll translate this whole text
    into the user's language later if necessary.
    """
    lines = []
    disease_name = disease_key.title()
    lines.append(f"It looks like your plants may be affected by *{disease_name}*.")

    
    if info.get("symptoms"):
        lines.append(f"Symptoms usually include: {info['symptoms']}.")

    
    if info.get("cause"):
        lines.append(f"Cause: {info['cause']}.")

    
    if region:
        lines.append(
            f"Note: In {region}, environmental conditions can sometimes increase the risk of this disease — consider local climate and recent weather."
        )

    
    if info.get("treatment"):
        lines.append(f"Suggested actions: {info['treatment']}.")

    
    if info.get("prevention"):
        lines.append(f"Prevention: {info['prevention']}.")

    return "\n\n".join(lines)


def chatbot(query: str, input_type: str = "text", forced_language: str = "English"):
    """
    Main chatbot function with full multilingual support using deep-translator.

    - query: user text (or cleaned disease key for image)
    - input_type: "text" or "image"
    """

    
    if not query or not isinstance(query, str) or query.strip() == "":
        return "Hello! I am AgroBot — your agricultural assistant. How can I help you today?"

    
    user_lang = detect_language(query) or "en"
    if forced_language and forced_language.lower() != "auto":
        user_lang = forced_language.lower()

    
    smalltalk_type = detect_smalltalk(query)
    if smalltalk_type:
        
        base_reply = smalltalk_reply(query, "en")
        
        if user_lang == "en":
            return base_reply
        
        try:
            translated = translate_text(base_reply, user_lang)
            return translated
        except Exception:
            
            return base_reply

    
    disease_keys = list(plant_disease_info.keys())

    
    if input_type == "image":
        key = query.strip().lower()
        if key in plant_disease_info:
            best = key
            score = 100
        else:
            
            best, score = get_best_match(query, disease_keys)
    else:
        
        if user_lang != "en":
            try:
                eng_query = translate_text(query, "en")
            except Exception:
                
                eng_query = query
        else:
            eng_query = query

        best, score = get_best_match(eng_query, disease_keys)

    
    if not best or score < 40:
        fallback_en = "Sorry, I couldn't understand clearly. Please describe the symptoms a bit more or upload a close-up photo of the affected leaf."
        if user_lang == "en":
            return fallback_en
        try:
            return translate_text(fallback_en, user_lang)
        except Exception:
            return fallback_en

    
    info = plant_disease_info.get(best, {})
    region = extract_region(query if input_type == "text" else "")  

    english_reply = format_detailed_english(best, info, region)

    
    if user_lang == "en":
        return english_reply

    
    try:
        translated_reply = translate_text(english_reply, user_lang)
        return translated_reply
    except Exception:
        
        return english_reply
