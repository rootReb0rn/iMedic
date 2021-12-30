from flask import Flask, app,render_template,request,flash,redirect
import pickle
from flask.sessions import NullSession
import numpy as np

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route("/predict", methods = ['POST', 'GET'])
def predictPage():
    if request.method == "POST":

        # Diabetes
        valueD1 = request.form['pregnancies']
        valueD2 = request.form['glucose']
        valueD3 = request.form['blood_pressure']
        valueD4 = request.form['skin_thickness']
        valueD5 = request.form['insulin']
        valueD6 = request.form['bmi']
        valueD7 = request.form['diabetes_pedigree_function']
        valueD8 = request.form['age']

        # Heart
        valueH1 = request.form['age_heart']
        valueH2 = request.form['sex']
        valueH3 = request.form['chest-pain-type']
        valueH4 = request.form['resting-blood-pressure']
        valueH5 = request.form['serum-cholestoral']
        valueH6 = request.form['fasting-blood-sugar']
        valueH7 = request.form['resting-electrocardiographic']
        valueH8 = request.form['maximum-heart-rate']
        valueH9 = request.form['exercise-induced-angina']
        valueH10 = request.form['st-depression']
        valueH11 = request.form['slope']
        valueH12 = request.form['vessels-colored']
        valueH13 = request.form['thalassemia']

        # Liver
        valueL1 = request.form['age_liver']
        valueL2 = request.form['gender_liver']
        valueL3 = request.form['total-bilirubin']
        valueL4 = request.form['direct-bilirubin']
        valueL5 = request.form['alkaline-phosphotase']
        valueL6 = request.form['alamine-aminotransferase']
        valueL7 = request.form['aspartate-aminotransferase']
        valueL8 = request.form['total-protiens']
        valueL9 = request.form['albumin']
        valueL10 = request.form['albumin_and_alobulin_ratio']

        diabetes_prediction = (valueD1,valueD2,valueD3,valueD4,valueD5,valueD6,valueD7,valueD8)
        heart_prediction = (valueH1,valueH2,valueH3,valueH4,valueH5,valueH6,valueH7,valueH8,valueH9,valueH10,valueH11,valueH12,valueH13)
        liver_prediction = (valueL1,valueL2,valueL3,valueL4,valueL5,valueL6,valueL7,valueL8,valueL9,valueL10)


        diabetes_model = pickle.load(open("../Model/diabetes.pkl",'rb'))
        heart_model = pickle.load(open("../Model/heart_test.pkl",'rb'))
        liver_model = pickle.load(open("../Model/heart_test.pkl",'rb'))


        get_diabetes = np.asarray(diabetes_prediction)
        get_heart = np.asarray(heart_prediction)
        get_liver = np.asarray(liver_prediction)

        prediction = model.predict(values.reshape(1, -1))[0]

        print(prediction)

        if (prediction == 0):
            print('The person is not diabetic')
        else:
            print('The person is diabetic')    

        return render_template('index.html',result = prediction)