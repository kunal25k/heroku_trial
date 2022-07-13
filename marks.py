import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import (LinearRegression, Ridge, Lasso)
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
import pickle 
from pickle import dump, load
from sklearn.multioutput import MultiOutputRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense

rf = load(open('rfReg_all.sav', 'rb'))

model = rf

def marks_prediction(marks):
    arr = np.array(marks).reshape(1,-1)
    values = model.predict(arr)

    return values