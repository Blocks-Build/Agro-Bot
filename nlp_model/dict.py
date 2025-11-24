# nlp_model/knowledge_base.py

plant_disease_info = {
    # Apple
    "apple scab": {
        "plant": "Apple",
        "symptoms": "Olive-brown scabby spots on leaves and fruit.",
        "cause": "Venturia inaequalis (fungus).",
        "treatment": "Remove affected leaves/fruit, apply captan or mancozeb."
    },
    "apple black rot": {
        "plant": "Apple",
        "symptoms": "Dark sunken lesions on fruit; leaf spots and cankers.",
        "cause": "Botryosphaeria obtusa (fungus).",
        "treatment": "Prune/remove infected wood and fruit; apply appropriate fungicide."
    },
    "apple cedar apple rust": {
        "plant": "Apple",
        "symptoms": "Bright yellow-orange spots on leaves; galls on nearby junipers.",
        "cause": "Gymnosporangium rust fungus.",
        "treatment": "Remove nearby junipers if possible, use rust fungicide."
    },
    "apple healthy": {
        "plant": "Apple",
        "symptoms": "No visible disease signs.",
        "cause": "Healthy plant.",
        "treatment": "Maintain good cultural practices."
    },

    # Blueberry
    "blueberry healthy": {
        "plant": "Blueberry",
        "symptoms": "No visible disease symptoms.",
        "cause": "Healthy plant.",
        "treatment": "Maintain correct soil pH and watering."
    },

    # Cherry
    "cherry healthy": {
        "plant": "Cherry",
        "symptoms": "No visible disease symptoms.",
        "cause": "Healthy plant.",
        "treatment": "Maintain pruning and airflow."
    },
    "cherry powdery mildew": {
        "plant": "Cherry",
        "symptoms": "White powdery fungal growth on leaves and shoots.",
        "cause": "Powdery mildew fungi (Podosphaera etc.).",
        "treatment": "Remove infected growth, use sulfur or potassium bicarbonate sprays."
    },

    # Corn
    "corn cercospora leaf spot gray leaf spot": {
        "plant": "Corn",
        "symptoms": "Rectangular gray/brown lesions on leaves following veins.",
        "cause": "Cercospora zeae-maydis (fungus).",
        "treatment": "Use resistant hybrids, rotate crops, fungicide if severe."
    },
    "corn common rust": {
        "plant": "Corn",
        "symptoms": "Reddish-brown pustules on leaves (uredinia).",
        "cause": "Puccinia sorghi (rust fungus).",
        "treatment": "Plant tolerant hybrids; apply fungicide if threshold exceeded."
    },
    "corn healthy": {
        "plant": "Corn",
        "symptoms": "Green leaves; no spotting.",
        "cause": "Healthy plant.",
        "treatment": "Normal agronomic care."
    },
    "corn northern leaf blight": {
        "plant": "Corn",
        "symptoms": "Long gray-green cigar-shaped lesions on leaves.",
        "cause": "Exserohilum turcicum (fungus).",
        "treatment": "Resistant hybrids, crop rotation, fungicide when necessary."
    },

    # Grape
    "grape black rot": {
        "plant": "Grape",
        "symptoms": "Dark circular lesions on fruit and leaves; rotted berries.",
        "cause": "Guignardia bidwellii (fungus).",
        "treatment": "Remove mummified berries, apply mancozeb or similar fungicide."
    },
    "grape esca black measles": {
        "plant": "Grape",
        "symptoms": "Dark spotting and vine decline; black measles on berries.",
        "cause": "Wood-rotting fungi (complex of pathogens).",
        "treatment": "Remove heavily affected wood; improve vine vigor; consult specialist."
    },
    "grape healthy": {
        "plant": "Grape",
        "symptoms": "No visible disease.",
        "cause": "Healthy plant.",
        "treatment": "Maintain pruning and sanitation."
    },
    "grape leaf blight isariopsis leaf spot": {
        "plant": "Grape",
        "symptoms": "Brown/black leaf spots; early defoliation possible.",
        "cause": "Isariopsis spp. (fungal leaf spot).",
        "treatment": "Improve airflow, apply fungicides if severe."
    },

    # Orange / Citrus
    "orange huanglongbing citrus greening": {
        "plant": "Orange (Citrus)",
        "symptoms": "Yellow shoots, blotchy leaves, poor fruit; systemic disease.",
        "cause": "Bacterial (Candidatus Liberibacter) vectored by psyllids.",
        "treatment": "No cure; remove infected trees; control psyllid vectors."
    },

    # Peach
    "peach bacterial spot": {
        "plant": "Peach",
        "symptoms": "Small dark spots on leaves and fruit; fruit scarring.",
        "cause": "Xanthomonas campestris pv. pruni (bacterium).",
        "treatment": "Use copper sprays, remove infected fruit/branches, resistant cultivars."
    },
    "peach healthy": {
        "plant": "Peach",
        "symptoms": "No visible disease.",
        "cause": "Healthy plant.",
        "treatment": "Maintain cultural care."
    },

    # Pepper bell
    "pepper bell bacterial spot": {
        "plant": "Pepper (bell)",
        "symptoms": "Water-soaked spots on fruit and leaves that become dark; leaf drop.",
        "cause": "Xanthomonas spp. (bacterial).",
        "treatment": "Use certified seed/seed treatments, copper sprays, remove infected plants."
    },
    "pepper bell healthy": {
        "plant": "Pepper (bell)",
        "symptoms": "No visible disease.",
        "cause": "Healthy plant.",
        "treatment": "Maintain irrigation and nutrition."
    },

    # Potato
    "potato early blight": {
        "plant": "Potato",
        "symptoms": "Dark concentric-ring lesions on leaves.",
        "cause": "Alternaria solani (fungus).",
        "treatment": "Crop rotation, avoid overhead irrigation, apply chlorothalonil."
    },
    "potato healthy": {
        "plant": "Potato",
        "symptoms": "No visible disease.",
        "cause": "Healthy plant.",
        "treatment": "Maintain best practices."
    },
    "potato late blight": {
        "plant": "Potato",
        "symptoms": "Water-soaked lesions and white fuzzy growth under leaves; tuber rot.",
        "cause": "Phytophthora infestans (oomycete).",
        "treatment": "Systemic fungicides (metalaxyl), remove infected plants, use certified seed."
    },

    # Raspberry
    "raspberry healthy": {
        "plant": "Raspberry",
        "symptoms": "No visible disease.",
        "cause": "Healthy plant.",
        "treatment": "Maintain pruning and sanitation."
    },

    # Soybean
    "soybean healthy": {
        "plant": "Soybean",
        "symptoms": "Green healthy leaves.",
        "cause": "Healthy plant.",
        "treatment": "Standard care."
    },

    # Squash
    "squash powdery mildew": {
        "plant": "Squash",
        "symptoms": "White powdery patches on leaf surfaces.",
        "cause": "Powdery mildew fungi.",
        "treatment": "Apply sulfur or potassium bicarbonate; improve airflow."
    },

    # Strawberry
    "strawberry healthy": {
        "plant": "Strawberry",
        "symptoms": "No visible disease.",
        "cause": "Healthy plant.",
        "treatment": "Good irrigation and sanitation."
    },
    "strawberry leaf scorch": {
        "plant": "Strawberry",
        "symptoms": "Brown lesions at leaf margins; leaf scorch symptoms.",
        "cause": "Likely fungal or environmental stress.",
        "treatment": "Remove affected leaves, adjust irrigation, consider fungicide."
    },

    # Tomato
    "tomato bacterial spot": {
        "plant": "Tomato",
        "symptoms": "Small water-soaked dark lesions on leaves and fruit.",
        "cause": "Xanthomonas spp. (bacterial).",
        "treatment": "Copper sprays, remove infected fruit, use disease-free seed."
    },
    "tomato early blight": {
        "plant": "Tomato",
        "symptoms": "Brown leaf spots with concentric rings.",
        "cause": "Alternaria solani (fungus).",
        "treatment": "Remove affected foliage; apply copper-based fungicide."
    },
    "tomato healthy": {
        "plant": "Tomato",
        "symptoms": "No visible disease.",
        "cause": "Healthy plant.",
        "treatment": "Maintain watering and airflow."
    },
    "tomato late blight": {
        "plant": "Tomato",
        "symptoms": "Large dark patches; white mold under humid conditions.",
        "cause": "Phytophthora infestans (oomycete).",
        "treatment": "Systemic fungicides, remove diseased plants."
    },
    "tomato leaf mold": {
        "plant": "Tomato",
        "symptoms": "Yellow patches above, olive-green mold on underside.",
        "cause": "Fulvia fulva (Passalora fulva) fungus.",
        "treatment": "Improve ventilation; apply copper fungicides."
    },
    "tomato septoria leaf spot": {
        "plant": "Tomato",
        "symptoms": "Small, water-soaked circular spots; grey centers.",
        "cause": "Septoria lycopersici (fungus).",
        "treatment": "Remove infected leaves; apply fungicide."
    },
    "tomato spider mites": {
        "plant": "Tomato",
        "symptoms": "Fine stippling on leaves; webbing in severe cases.",
        "cause": "Two-spotted spider mite (Tetranychus urticae).",
        "treatment": "Use miticides or insecticidal soap; encourage predatory mites."
    },
    "tomato target spot": {
        "plant": "Tomato",
        "symptoms": "Circular brown lesions with target-like rings.",
        "cause": "Corynespora cassiicola (fungus).",
        "treatment": "Remove infected debris; fungicide when necessary."
    },
    "tomato mosaic virus": {
        "plant": "Tomato",
        "symptoms": "Mottled mosaic leaf patterns; stunted growth.",
        "cause": "Tobamovirus (TMV) – viral infection.",
        "treatment": "No chemical cure; remove infected plants; use resistant varieties."
    },
    "tomato yellow leaf curl virus": {
        "plant": "Tomato",
        "symptoms": "Leaf curling, yellowing and stunted growth.",
        "cause": "Tomato yellow leaf curl virus transmitted by whiteflies.",
        "treatment": "Control whiteflies, remove infected plants, use resistant varieties."
    }
}
