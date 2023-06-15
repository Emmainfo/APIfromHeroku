# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 15:56:05 2023

@author: iiiioiii
"""
#import libraries

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

# create an instance of the fastapi
app = FastAPI()

'''
define a class and pass the basemodel as an argument. 
Base model is used to declare the format of input data. Eg interge, float etc.
'''
class model_input(BaseModel):
    
    SepalLength: float
    SepalWidth: float
    PetalLength: float
    PetalWidth: float
    
#load the model
Iris_model=pickle.load(open("iris_model.sav",'rb'))

# post() receives the data from user and post it to the API    
@app.post('/Iris_Specie_Prediction')
def iris_specie_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary =json.loads(input_data)
    
    SL = input_dictionary['SepalLength']
    SW = input_dictionary['SepalWidth']
    PL = input_dictionary['PetalLength']
    PW = input_dictionary['PetalWidth']
    
    input_list = [SL, SW, PL, PW]
    
    prediction = Iris_model.predict([input_list])
    
    if prediction[0] == 0:
        return 'Iris Specie is Setosa'
    if prediction == 1:
        return 'Iris Specie is Versicolor'
    else:
        return 'Iris Specie is Virginica'