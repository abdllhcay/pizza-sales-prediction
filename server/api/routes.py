from flask import request, jsonify, abort
from api import app, db, bcrypt
from api.models import User, Task
import json
import secrets
import datetime

# Data analysis libraries
import warnings
import itertools
import numpy as np
import pandas as pd
import statsmodels.api as sm

warnings.filterwarnings("ignore")

# Returns all tasks
@app.route('/api/tasks/', methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([i.serialize for i in tasks])

# Return task by id
@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify([task.serialize])

# Create new task
@app.route("/api/tasks/", methods=["POST"])
def create_task():
    if not request.json:
        return abort(404)
    
    task = Task(name=request.json["name"], started="N/A", finished="N/A", status="Not started", step=request.json["step"], file_path=request.json["file_path"], result="")
    db.session.add(task)
    db.session.commit()

    return jsonify([task.serialize])

# User registration
@app.route("/api/register/", methods=["POST"])
def register():
    username = request.json["username"]
    password = request.json["password"]
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()

    token = secrets.token_hex(20)
    resp = {
        "token": token,
        "user": user.serialize
    }

    if user:
        return jsonify(resp)
    else:
        return abort(404)

# User login
@app.route("/api/login/", methods=["POST"])
def login():
    username = request.json["username"]
    password = request.json["password"]
    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    user = User(username=username, password=hashed_password)

    token = secrets.token_hex(20)
    resp = {
        "token": token,
        "user": user.serialize
    }

    if user:
        return jsonify(resp)
    else:
        return abort(404)

# Prediction method by task id
@app.route("/api/predict/<int:task_id>", methods=["POST"])
def predict_sales(task_id):
    task = Task.query.get_or_404(task_id)
    file_name = task.file_path
    step = task.step

    started_time = datetime.datetime.now().time().strftime("%H:%M:%S")

    # Loading Time Series
    df = pd.read_excel(file_name)
    categories = df["Category"].unique()
    result = {}

    for category in categories:
        pizza = df.loc[df["Category"] == category]

        cols = ['Category']
        pizza.drop(cols, axis=1, inplace=True)
        pizza = pizza.sort_values("Month")
        pizza = pizza.groupby('Month')['Sales'].sum().reset_index()

        pizza = pizza.set_index('Month')
        ts = pizza["Sales"].resample("MS").mean()

        # ARIMA Model Fitting
        mod = sm.tsa.statespace.SARIMAX(ts, order=(1, 1, 1), seasonal_order=(1, 1, 0, 12), enforce_stationarity=False, enforce_invertibility=False)
        results = mod.fit()

        # Producing Forecasts
        pred_uc = results.get_forecast(steps=step)  

        result[category] = pred_uc.predicted_mean.to_string()

    finished_time = datetime.datetime.now().time().strftime("%H:%M:%S")

    # Update database
    task.result = json.dumps(result)
    task.status = "Success"
    task.started = started_time
    task.finished = finished_time
    db.session.commit()  

    return("Success")