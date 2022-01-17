from flask import Flask, app, render_template, request, flash, redirect
import pickle
from flask.sessions import NullSession
import numpy as np

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/prediction')
def prediction():
    return render_template('prediction.html', report=0,obtain_diabetes = [],
                               obtain_heart= [],
                               obtain_liver= [])


@app.route("/predict", methods=['POST', 'GET'])
def predictPage():
    if request.method == "POST":

        diabetes_list = []
        heart_list = []
        liver_list = []
        mytable_list = []

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
        valueL1 = request.form['age-liver']
        valueL2 = request.form['gender_liver']
        valueL3 = request.form['total-bilirubin']
        valueL4 = request.form['direct-bilirubin']
        valueL5 = request.form['alkaline-phosphotase']
        valueL6 = request.form['alamine-aminotransferase']
        valueL7 = request.form['aspartate-aminotransferase']
        valueL8 = request.form['total-protiens']
        valueL9 = request.form['albumin']
        valueL10 = request.form['albumin_and_alobulin_ratio']

        diabetes_list.append(float(valueD1))
        diabetes_list.append(float(valueD2))
        diabetes_list.append(float(valueD3))
        diabetes_list.append(float(valueD4))
        diabetes_list.append(float(valueD5))
        diabetes_list.append(float(valueD6))
        diabetes_list.append(float(valueD7))
        diabetes_list.append(float(valueD8))

        heart_list.append(float(valueH1))
        heart_list.append(float(valueH2))
        heart_list.append(float(valueH3))
        heart_list.append(float(valueH4))
        heart_list.append(float(valueH5))
        heart_list.append(float(valueH6))
        heart_list.append(float(valueH7))
        heart_list.append(float(valueH8))
        heart_list.append(float(valueH9))
        heart_list.append(float(valueH10))
        heart_list.append(float(valueH11))
        heart_list.append(float(valueH12))
        heart_list.append(float(valueH13))

        liver_list.append(float(valueL1))
        liver_list.append(float(valueL2))
        liver_list.append(float(valueL3))
        liver_list.append(float(valueL4))
        liver_list.append(float(valueL5))
        liver_list.append(float(valueL6))
        liver_list.append(float(valueL7))
        liver_list.append(float(valueL8))
        liver_list.append(float(valueL9))
        liver_list.append(float(valueL10))
        print(diabetes_list)
        print(heart_list)
        print(liver_list)
        # diabetes_prediction = (valueD1,valueD2,valueD3,valueD4,valueD5,valueD6,valueD7,valueD8)
        # heart_prediction = (valueH1,valueH2,valueH3,valueH4,valueH5,valueH6,valueH7,valueH8,valueH9,valueH10,valueH11,valueH12,valueH13)
        # liver_prediction = (valueL1,valueL2,valueL3,valueL4,valueL5,valueL6,valueL7,valueL8,valueL9,valueL10)

        diabetes_model = pickle.load(open("../Model/diabetes.pkl", 'rb'))
        heart_model = pickle.load(open("../Model/heart.pkl", 'rb'))
        liver_model = pickle.load(open("../Model/liver.pkl", 'rb'))

        get_diabetes = np.asarray(diabetes_list)
        get_heart = np.asarray(heart_list)
        get_liver = np.asarray(liver_list)

        diabetes_prediction = diabetes_model.predict(
            get_diabetes.reshape(1, -1))[0]
        heart_prediction = heart_model.predict(get_heart.reshape(1, -1))[0]
        liver_prediction = liver_model.predict(get_liver.reshape(1, -1))[0]

        if (diabetes_prediction == 0):
            print('The person is not diabetic')
        else:
            print('The person is diabetic')

        if (heart_prediction == 0):
            print('The person is not heart')
        else:
            print('The person is heart')

        if (liver_prediction == 0):
            print('The person is not liver')
        else:
            print('The person is liver')

        return render_template('prediction.html',
                               report=1,
                               diabetes=diabetes_prediction,
                               heart=heart_prediction,
                               liver=liver_prediction,
                               obtain_diabetes = diabetes_list,
                               obtain_heart=heart_list,
                               obtain_liver=liver_list)

