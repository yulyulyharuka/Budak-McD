from flask import Flask, render_template, request
import json
import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

#Load model
gnb_load = joblib.load('gnb_HeartDisease_model.joblib')

app = Flask(__name__)

@app.route('/index.html')
def index():
   return render_template('index')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    data = []
    if request.method == 'POST':
        patient_age = int(request.form['age'])
        patient_sex = int(request.form['sex'])
        patient_cpt = int(request.form['cpt'])
        patient_rbp = int(request.form['rbp'])
        patient_sc = int(request.form['sc'])
        patient_fbs = int(request.form['fbs'])
        patient_re = int(request.form['re'])
        patient_mhra = int(request.form['mhra'])
        patient_eia = int(request.form['eia'])
        patient_std = int(request.form['std'])
        patient_pess = int(request.form['pess'])
        patient_mvcf = int(request.form['mvcf'])
        patient_thal = int(request.form['thal'])
        data = [patient_age, patient_sex, patient_cpt, patient_rbp, patient_sc, patient_fbs, patient_re, patient_mhra, patient_eia, patient_std, patient_pess, patient_mvcf, patient_thal]
        result = gnb_load.predict([data])
        return render_template("result.html",result = str(result[0]))

if __name__ == '__main__':
   app.run(debug = True)
