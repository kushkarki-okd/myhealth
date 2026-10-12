from pathlib import Path
import joblib
import pandas as pd

ML_DIR =  Path(__file__).resolve().parent / "ml"

model =joblib.load(ML_DIR / "model.pkl")
symptoms =joblib.load(ML_DIR / "symptoms.pkl")

def predict_diseases(selected):
    vec=[1 if s in selected else 0 for s in symptoms ]
    df = pd.DataFrame([vec],columns=symptoms)
    prediction=model.predict(df)[0]
    probs =model.predict_proba(df)[0]
    top3 = sorted(zip(model.classes_, probs), key=lambda x: x[1], reverse=True)[:3]
    top3 = [(d, round(p * 100, 1)) for d, p in top3]

    return prediction, top3