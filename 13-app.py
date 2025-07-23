# added field validator of the city in the previous api
# added the home endpoint
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Literal, Annotated
import pickle
from schema.prediction_response import PredictionResponse
import pandas as pd
from schema.userinput import UserInput
from model.predict import predict_output,MODEL_VERSION,model

app = FastAPI()

@app.get('/')
def message_return():
    return {'message':'Insurance premium prediction api'}

@app.get('/health')
def health_check():
    return { 
        'status':'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }

@app.post('/predict',response_model=PredictionResponse)
def predict_premium(data: UserInput):

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(user_input)
        # the output should be a list bcs wee are predict the 0th index in the predict.py so [] are used

        return JSONResponse(status_code=200, content={'predicted_category': prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})