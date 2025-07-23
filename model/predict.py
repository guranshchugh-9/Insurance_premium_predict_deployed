import pickle 
import pandas as pd

with open('12-model.pkl', 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'

class_labels = model.classes_.tolist()
def predict_output(user_input:dict):
    df = pd.DataFrame([user_input])
    predicted_class = model.predict(df)[0]
    predicted_prob = model.predict_proba(df)[0]
    confidence = max(predicted_prob)

    # create mapping of {class_name: probability}
    class_probs = {label:round(prob,4) for label,prob in zip(class_labels,predicted_prob)}

    return {
        'predicted category': predicted_class,
        'confidence': round(confidence,4),
        'class_probabilities': class_probs
    }