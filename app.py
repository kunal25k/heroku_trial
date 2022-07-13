from flask import Flask, render_template, request
# import marks as m
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

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/sub", methods = ['POST'])
def submit(): 
    if request.method == 'POST':
        name = request.form['username']
    return render_template('sub.html', n = name)


if __name__ == '__main__':
    app.run(debug=True)
