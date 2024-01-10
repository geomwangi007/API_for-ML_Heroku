# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 04:04:37 2024

@author: geoff
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
                  Pregnancies : int
                  Glucose : int
                  BloodPressure : int
                  SkinThickness : int
                  Insulin : int
                  BMI : float
                  DiabetesPedigreeFunction : float
                  Age : int
                 
#Loading the model
diabetes_model = pickle.load(open("diabetes_model.sav" , "rb"))

@app.post("/diabetes_prediction")

def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary["Pregnancies"]
    glu = input_dictionary["Glucose"]
    bp = input_dictionary["BloodPressure"]
    skin = input_dictionary["SkinThickness"]
    ins = input_dictionary["Insulin"]
    bmi = input_dictionary["BMI"]
    diabetes = input_dictionary["DiabetesPedigreeFunction"]
    age = input_dictionary["Age"]
    
    input_list = [preg , glu , bp ,skin , ins , bmi , diabetes , age]
    
    prediction = diabetes_model.predict([input_list])
    
    if prediction[0] == 0:
        return "The Person is Non-Diabetic"
    
    else:
        return "The Person is diabetic"
                  