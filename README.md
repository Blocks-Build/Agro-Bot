🌾 **AgroBot – Smart Farming Assistant**

AgroBot is a machine learning–powered farming assistant that helps farmers identify crop issues and get agricultural guidance using a combination of CNN-based image classification, NLP-based chatbot interaction, and multilingual translation. The system is built with a clean and simple Streamlit interface for easy use.

🚀 Key Features

🔍 CNN Model for detecting crop diseases or issues from images

💬 NLP Chatbot that understands user queries and provides relevant responses

🌐 Multilingual Support using Google Translate API (deep-translator)

🖥️ Streamlit UI for user interaction

**Tech Stack**

Python

TensorFlow (CNN model)

Streamlit (Frontend UI)

deep-translator (Google Translate API)

langdetect

rapidfuzz



Project Structure 
```
AGROBOT/
├── app.py
├── models/
│   └── classifier_model.keras
├── nlp_model/
│   ├── preprocess.py
│   ├── match.py
│   ├── bot.py
│   ├── translate.py
│   └── dict.py
├── FINAL REVIEW DOCS/
│   ├── AgroBot_final ppt.pptx
│   └── Project documentation.pdf
├── requirements.txt
└── LICENSE
```

📜 License

This project is licensed under the MIT License.
