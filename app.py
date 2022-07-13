from flask import Flask, render_template, request
# import marks as m
import numpy as np
import pandas as pd
import pickle 
from pickle import dump, load

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/sub", methods = ['POST'])
def submit(): 
    if request.method == 'POST':
        name = request.form['username']
        x = 0
        if name == 2:
            x = 1
        else:
            x = 5
    return render_template('sub.html', n = x)


if __name__ == '__main__':
    app.run(debug=True)
