from flask import Flask, render_template, request
# import marks as m
import numpy as np
import pandas as pd

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
