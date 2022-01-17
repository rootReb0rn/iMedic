# 👓 PROJECT OVERVIEW

## D. EXECUTING THE PROJECT

### Flowchart

![Flowchart of the project](Assets/Execution/Flowchart.png)

### Design

### Code

#### Training

For the training, the datasets used are the `diabetes.csv`, `heart.csv`, and `indian_liver_patient.csv`, which can be viewed in the [Dataset](../Dataset) folder. The training code, which are written in Jupyter Notebook, are located in the [Train](../Train) folder. The model `.pkl` file are located in [Model](../Model) folder.

#### Web application

**1.Dependencies**

For the web application, Flask is used to as the web framework. The dependencies are:

- `flask`
- `numpy`

To install the dependencies, run `pip install flask numpy`

**2. Code Snippet**

The code snippet of the code for creating the web server:

```Python
from flask import Flask, app, render_template, request, flash, redirect
import pickle
from flask.sessions import NullSession
import numpy as np

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/prediction')
def prediction():
    return render_template('prediction.html', report=0)


@app.route("/predict", methods=['POST', 'GET'])
def predictPage():
    if request.method == "POST":

        diabetes_list = []
        heart_list = []
        liver_list = []

        ####################End of snippet########################
```

The full code can be viewed in [app.py](../Src/app.py) file in the [Src](../Src) folder.

## Project Result

### Homepage
Homepage and the About Us section of the web app

![Homepage of the web application](Assets/Execution/Homepage.png)

![About Us section of the web application](Assets/Execution/AboutUsPage.png)

### Form
For entering patient's details as input data for the model

![Form](Assets/Execution/FormPage.png)

### Result Page
Displaying the result of the model - i.e., negative or positive. The [Project Result.pdf](Assets/Execution/Project%20Result.pdf) shows the result output from the website.

![Result Page](Assets/Execution/ResultPage.png)


---
◀ Back : [Project Implementation](C-PROJECT_IMPLEMENTATION.md)

Next : [Project Closing ▶](E-PROJECT_CLOSING.md)
