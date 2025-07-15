# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 21:34:31 2025

@author: hp
"""

import numpy as np
import pickle
file_load= pickle.load(open("model_trained.sav",'rb'))
input_data=(10,168,74,0,0,38,0.537,34)
#converting data into numpy array for efficient processing
input_data_as_numpy_array= np.asarray(input_data)
#reshaping np array for one instance of data
data_reshaped=input_data_as_numpy_array.reshape(1,-1)
#instance for correct prediction,we will use scalar.transform,we dont need to fit data as we already did it
#std_data= scalar.transform(data_reshaped)
prediction= file_load.predict(data_reshaped)
print(prediction)
if (prediction[0]==1):
  print("The patient is Diabetic")
else:
  print("The patent is not Diabetic")
