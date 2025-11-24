
import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import hashlib
import io
import base64


from nlp_model.bot import chatbot

# ----------------------------- CSS -----------------------------
def inject_css():
    st.markdown("""
    <style>
    .stApp { background-color: #FFEAF0 !important; }

    .main-header {
        background-color: #2E7D32;
        padding: 14px 20px;
        color: white;
        font-size: 22px;
        font-weight: 700;
        text-align: center;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 999;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.2);
    }

    .chat-container {
        margin-top: 80px; /* leave room for fixed header */
        padding: 12px 18px;
    }

    .chat-bubble {
        background-color: #E6F4EA;
        color: black !important;
        padding: 12px 16px;
        border-radius: 12px;
        max-width: 72%;
        margin: 10px 0;
        border: 1px solid #A8D5B1;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        display: inline-block;
        font-size: 15px;
        line-height: 1.35;
    }

    .user-msg { text-align: right; margin-right: 40px; }
    .bot-msg  { text-align: left;  margin-left: 40px; }

    .chat-image {
        max-width: 320px;
        border-radius: 8px;
        border: 1px solid #CFEAD1;
        display: block;
        margin-top: 8px;
    }

    .stTextInput input {
        background: #E6F4EA !important;
        border-radius: 25px !important;
        padding: 12px 18px !important;
        border: 1px solid #A8D5B1 !important;
        color: black !important;
        font-size: 15px !important;
        box-shadow: none !important;
        outline: none !important;
    }

    .stFileUploader > div > div > button {
        background: #E6F4EA !important;
        border: 1px solid #A8D5B1 !important;
        color: black !important;
    }

    div.stButton > button {
        background-color: #C8E6C9 !important;
        color: #1B5E20 !important;
        border-radius: 50% !important;
        width: 48px !important;
        height: 48px !important;
        font-size: 24px !important;
        padding: 0 !important;
        border: none !important;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .stTextInput input::placeholder {
        color: #3A3A3A !important;
        opacity: 1 !important;
    }
                /* Make selectbox label text black */
    div[data-testid="stSelectbox"] label {
        color: black !important;
        font-weight: 500 !important;
}

   

/* Prevent message container from hiding behind bottom bar */
.chat-container {
    margin-bottom: 120px !important;
}


    </style>
    """, unsafe_allow_html=True)

# ----------------------------- helper to clean classifier label -----------------------------
def raw_to_clean(raw_label: str) -> str:
    """
    'Apple___Apple_scab' -> 'apple scab'
    Works for all PlantVillage style labels.
    """
    if not raw_label:
        return ""
    if "___" in raw_label:
        raw = raw_label.split("___")[-1]
    else:
        raw = raw_label
    clean = raw.replace("_", " ").replace(",", " ").replace("(", " ").replace(")", " ")
    clean = " ".join(clean.split()).lower()
    return clean

# ----------------------------- load classifier -----------------------------
@st.cache_resource
def load_classifier():
    return tf.keras.models.load_model("models/classifier_model.keras")

classifier = load_classifier()

# ----------------------------- full 38 class list -----------------------------
class_names = [
    'Apple___Apple_scab',
    'Apple___Black_rot',
    'Apple___Cedar_apple_rust',
    'Apple___healthy',
    'Blueberry___healthy',
    'Cherry___healthy',
    'Cherry___Powdery_mildew',
    'Corn___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn___Common_rust',
    'Corn___healthy',
    'Corn___Northern_Leaf_Blight',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___healthy',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Peach___Bacterial_spot',
    'Peach___healthy',
    'Pepper,_bell___Bacterial_spot',
    'Pepper,_bell___healthy',
    'Potato___Early_blight',
    'Potato___healthy',
    'Potato___Late_blight',
    'Raspberry___healthy',
    'Soybean___healthy',
    'Squash___Powdery_mildew',
    'Strawberry___healthy',
    'Strawberry___Leaf_scorch',
    'Tomato___Bacterial_spot',
    'Tomato___Early_blight',
    'Tomato___healthy',
    'Tomato___Late_blight',
    'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot',
    'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot',
    'Tomato___Tomato_mosaic_virus',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus'
]


st.set_page_config(page_title="AgroBot", layout="centered")
inject_css()
st.markdown("<div class='main-header'>🌱 AgroBot Chatbot Project</div>", unsafe_allow_html=True)
# ----------------------------- Language Selector -----------------------------
if "language" not in st.session_state:
    st.session_state.language = "English"
LANG_OPTIONS = [
    "English",
    "Hindi",
    "Bengali",
    "Telugu",
    "Marathi",
    "Tamil",
    "Urdu",
    "Gujarati",
    "Kannada",
    "Odia",
    "Malayalam",
    "Punjabi",
    "Assamese",
    "Maithili",
    "Santali",
    "Kashmiri",
    "Nepali",
    "Konkani",
    "Sindhi",
    "Dogri",
    "Manipuri",
    "Bodo"
]

lang = st.selectbox(
    "🌐 Choose your language for responses:",
    LANG_OPTIONS,
    index=LANG_OPTIONS.index(st.session_state.language)
)


st.session_state.language = lang

if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_image_hash" not in st.session_state:
    st.session_state.last_image_hash = None
if "text_input_key" not in st.session_state:
    st.session_state.text_input_key = "txt1"

# initial bot greeting once per session
if len(st.session_state.messages) == 0:
    start_msg = "👋 Hello! I’m AgroBot — your agricultural assistant. How can I help you today?"
    st.session_state.messages.append({"role":"bot","content": start_msg, "image": None})

# ----------------------------- Render Chat History -----------------------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for msg in st.session_state.messages:
    role = msg["role"]
    content = msg.get("content","")
    image = msg.get("image", None)

    # sanitize content (safe to insert HTML; chatbot outputs already contain safe simple HTML like <b>)
    if role == "user":
        if image:
            st.markdown(f"""
            <div class="user-msg">
                <div class="chat-bubble">
                    {content}
                    <br><img src="{image}" class="chat-image" />
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="user-msg"><div class="chat-bubble">{content}</div></div>""", unsafe_allow_html=True)
    else:
        if image:
            st.markdown(f"""
            <div class="bot-msg">
                <div class="chat-bubble">
                    {content}
                    <br><img src="{image}" class="chat-image" />
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""<div class="bot-msg"><div class="chat-bubble">{content}</div></div>""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------- Input Row -----------------------------
st.markdown("""
<div class="bottom-input-bar">
""", unsafe_allow_html=True)

input_col, upload_col, send_col = st.columns([5,2,1])
with input_col:
    user_text = st.text_input("", key=st.session_state.text_input_key,
                              placeholder="Type a message...", label_visibility="collapsed")
with upload_col:
    uploaded_file = st.file_uploader("", type=["jpg","jpeg","png"], label_visibility="collapsed")
with send_col:
    send_clicked = st.button("➤")

st.markdown("</div>", unsafe_allow_html=True)


# ----------------------------- Handle Text Send -----------------------------
if send_clicked:
    text = (user_text or "").strip()
    if text:
       
        st.session_state.messages.append({"role":"user","content": text, "image": None})

       
        try:
            bot_reply = chatbot(text, input_type="text", forced_language=st.session_state.language)
        except Exception as e:
            bot_reply = f"⚠️ NLP Error: {e}"

        st.session_state.messages.append({"role":"bot","content": bot_reply, "image": None})

       
        st.session_state.text_input_key = f"txt{np.random.randint(1_000_000)}"

# ----------------------------- Handle Image Upload -----------------------------
if uploaded_file is not None:
    file_bytes = uploaded_file.getvalue()
    file_hash = hashlib.md5(file_bytes).hexdigest()

    if file_hash != st.session_state.last_image_hash:
        st.session_state.last_image_hash = file_hash

        pil_img = Image.open(io.BytesIO(file_bytes)).convert("RGB")

        
        buf = io.BytesIO()
        pil_img.save(buf, format="PNG")
        img_b64 = base64.b64encode(buf.getvalue()).decode()
        img_url = f"data:image/png;base64,{img_b64}"

        
        resized = pil_img.resize((64,64))
        arr = np.array(resized).astype("float32") / 255.0
        arr = np.expand_dims(arr, 0)

       
        pred = classifier.predict(arr)
        idx = int(np.argmax(pred[0]))
        raw_label = class_names[idx]

        
        clean_key = raw_to_clean(raw_label)

        
        try:
            nlp_info = chatbot(clean_key, input_type="image", forced_language=st.session_state.language)
        except Exception as e:
            nlp_info = f" NLP Error: {e}"

        
        formatted_reply = (
            f"<b>📷 Thanks for your image.</b><br><br>"
            f"{nlp_info.replace(chr(10), '<br>')}"
        )

        st.session_state.messages.append({
            "role":"bot",
            "content": formatted_reply,
            "image": img_url
        })
        
        st.session_state.text_input_key = f"txt{np.random.randint(1_000_000)}"
