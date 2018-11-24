from flask import Flask, render_template, request
import json
import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

#Load model
gnb_load = joblib.load('gnb_HeartDisease_model.joblib')

app = Flask(__name__)

@app.route('/index')
def index():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    data = []
    if request.method == 'POST':
        patient_age = float(request.form['age'])
        patient_sex = float(request.form['sex'])
        patient_cpt = float(request.form['cpt'])
        patient_rbp = float(request.form['rbp'])
        patient_sc = float(request.form['sc'])
        patient_fbs = float(request.form['fbs'])
        patient_re = float(request.form['re'])
        patient_mhra = float(request.form['mhra'])
        patient_eia = float(request.form['eia'])
        patient_std = float(request.form['std'])
        patient_pess = float(request.form['pess'])
        patient_mvcf = float(request.form['mvcf'])
        patient_thal = float(request.form['thal'])
        data = [patient_age, patient_sex, patient_cpt, patient_rbp, patient_sc, patient_fbs, patient_re, patient_mhra, patient_eia, patient_std, patient_pess, patient_mvcf, patient_thal]
        result = gnb_load.predict([data])
        return render_template("result.html",result = str(result[0]))

if __name__ == '__main__':
   app.run(debug = True)
