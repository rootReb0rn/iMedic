# Project Execution

## Project Design and Code

### Flowchart

![Flowchart of the project](https://github.com/CharaeKeow/iMedic/blob/main/Documentation/Assets/Execution/Flowchart.png)

### Design

### Code

#### Training

For the training, the datasets used are the `diabetes.csv`, `heart.csv`, and `indian_liver_patient.csv`, which can be viewed in the [Dataset](https://github.com/rootReb0rn/iMedic/tree/main/Dataset) folder. The training code, which are written in Jupyter Notebook, are located in the [Train](https://github.com/rootReb0rn/iMedic/tree/main/Train) folder. The model `.pkl` file are located in [Model](https://github.com/rootReb0rn/iMedic/tree/main/Train) folder.

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

The full code can be viewed in [app.py](https://github.com/rootReb0rn/iMedic/blob/main/Src/app.py) file in the [Src](https://github.com/rootReb0rn/iMedic/tree/main/Src) folder.

## Project Result



---
[◀ Back : Project Implementation](A_PROJECT_IMPLEMENTATION.md)

[Next : Project Closing ▶](C_PROJECT_CLOSING.md)