# Pizza Sales Prediction
Project's purpose is prediction of future values in a time series which are sales of a pizza company. To implement forecasts SARIMA model fitting is used.

## Project setup
Python Flask web framework was used to implement API functionalities. You need to use following packages to run API module:
```
flask
flask-cors
flask-bcrypt
pandas
statsmodels
xlrd
openpyxl
```
To install them easily run the commands bellow on the terminal:
```
$ cd server
$ pip install -r requirements.txt
```
App needs to a database for store user and task data. To create database schema run the following command:
```
$ python database_creator.py
```
Move the database file to `api` directory.
Front-end functionalities implemented with Vue.js framework. To install related modules run the following command:
```
$ npm install
```
We installed server-side packages and created a database. Also installed front-end packages. Setup is completed now.

### Compiles and hot-reloads for development
Open two terminals and go to `server` directory on one of them. Run the `$ python run.py` command.
On the other terminal run the `$ npm run serve` command.

## Usage
Open your browser and go to `http://127.0.0.1:8080` address.
App will greet you with a login screen. Default login credentials are 
```
username: admin
password: 123456
```
You can create a new user from `http://127.0.0.1:8080/register` address.
To create a new task go to `Create Task` page from navbar. 
Dataset files must be in `server` directory. 
