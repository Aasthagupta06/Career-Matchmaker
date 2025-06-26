import json
import os

model_info = {
    "model_type": "SVC", 
    "vectorizer": "TfidfVectorizer",
    "label_encoder": "LabelEncoder",
    "trained_on": "Skills and Interests TF-IDF features",
    "tuned": True,
    "accuracy": 0.9778,  
    "best_params": {
        "C": 1,
        "kernel": "rbf",
        "gamma": "scale"
    }
}

# Save JSON file to ml_model folder
info_path = os.path.join('career_app', 'ml_model', 'model_info.json')
with open(info_path, 'w') as f:
    json.dump(model_info, f, indent=4)

print("✅ Model info updated at:", info_path)
