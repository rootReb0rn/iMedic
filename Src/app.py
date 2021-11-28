from flask import Flask, app,render_template,request,flash,redirect
import pickle
from flask.sessions import NullSession
import numpy as np

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    if request.method == "POST":

        value1 = request.form['pregnancies']
        value2 = request.form['glucose']
        value3 = request.form['blood_pressure']
        value4 = request.form['skin_thickness']
        value5 = request.form['insulin']
        value6 = request.form['bmi']
        value7 = request.form['diabetes_pedigree_function']
        value8 = request.form['age']

        input_data = (value1,value2,value3,value4,value5,value6,value7,value8)

        model = pickle.load(open("../Model/diabetes.pkl",'rb'))
        values = np.asarray(input_data)
        prediction = model.predict(values.reshape(1, -1))[0]

        print(prediction)

        if (prediction == 0):
            print('The person is not diabetic')
        else:
            print('The person is diabetic')    

        return render_template('index.html',result = prediction)