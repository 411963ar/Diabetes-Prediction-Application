# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 21:47:01 2025

@author: hp
"""

import numpy as np  # for numpy arrays
import pickle  #for loading and saving model
import streamlit as st   # for graphical user interface,web application
# loading the saved file
file_load= pickle.load(open("C:/Users/hp/OneDrive/Desktop/Diabetes prediction/model_trained.sav",'rb'))
# defining a function for prediction

def diabetes_prediction(input_data):
    input_data_as_numpy_array= np.asarray(input_data)
    #reshaping np array for one instance of data
    data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    #instance for correct prediction,we will use scalar.transform,we dont need to fit data as we already did it
    #std_data= scalar.transform(data_reshaped)
    prediction= file_load.predict(data_reshaped)
    print(prediction)
    if (prediction[0]==1):
      return "The patient is Diabetic"
    else:
      return "The patent is not Diabetic"
 
    
def main():
    #Title of predictive Web Application
    st.title("Diabetes Prediction Web Application")
    # filed boxes for user input
    Pregnancies=st.text_input("Current Week of Pregnancy:")
    Glucose=st.text_input("Unit of Glucose milligrams per deciliter (mg/dL) or millimoles per liter (mmol/L) depending upon country:")
    BloodPressure= st.text_input("Blood pressure in millimeters of mercury (mmHg):")
    SkinThickness=st.text_input("SkinThickness in millimeters (mm):")
    Insulin=st.text_input("Insulin  microunits per milliliter (μU/mL):")
    BMI=st.text_input("BMI (Body Mass Index) in kg/m²:")
    DiabetesPedigreeFunction=st.text_input("Likelihood Value For Diabetes Pedigree Function:")
    Age=st.text_input(" Age in Years:")
    
    
    # Code for Prediction
    
    output=" "  #  to store final predicted value in this variable
    # creating button to be pressed for prediction after getting input from user
    if st.button("test result"):
        output= diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        # it means when button is pressed, the diabetes_prediction function will be called with values given by user,after processing the output will be stored in output variable
        
    st.success(output)    # succesfully predicted out put will be displayed
    
    
if __name__ =="__main__":  #this function is used to run this code on command promt of anaconda as it will not run directly here on spyder
  main()    
    
    
    
    
    
    
    