from flask import Flask, render_template, request
import json
import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

# Reading Train Data

heartD = pd.read_csv('tubes2_HeartDisease_train.csv')
heartD_target = heartD['Column14']
heartD_data = heartD.loc[:, :'Column13']
heartD_feature_names = ['age', 'sex', 'chest-pain type', 'resting blod presure', 'serum cholestrol', 
                        'fasting blood sugar above 120 mg/dl', 'resting ECG', 'max heart rate achieved', 'exercise induced angina',
                       'ST depression induced', 'peak exercise ST segment', 'member of major vessel', 'thal']

heartD_target_names = ['absence', 'presence', 'presence', 'presence', 'presence']

# # fit a Naive Bayes model to the data
# gnb = GaussianNB()
# gnb_class = gnb.fit(heartD_data, heartD_target)
# print(gnb_class)

# # make predictions
# expected = heartD_target
# predicted = gnb_class.predict(testD)
# # summarize the fit of the model

app = Flask(__name__)

@app.route('/index.html')
def index():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    result = []
    if request.method == 'POST':
        patient_age = request.form['age']
        patient_sex = request.form['sex']
        patient_cpt = request.form['cpt']
        patient_rbp = request.form['rbp']
        patient_sc = request.form['sc']
        patient_fbs = request.form['fbs']
        patient_re = request.form['re']
        patient_mhra = request.form['mhra']
        patient_eia = request.form['eia']
        patient_std = request.form['std']
        patient_pess = request.form['pess']
        patient_mvcf = request.form['mvcf']
        patient_thal = request.form['thal']
        result = [patient_age, patient_sex, patient_cpt, patient_rbp, patient_sc, patient_fbs, patient_re, patient_mhra, patient_eia, patient_std, patient_pess, patient_mvcf, patient_thal]
        return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(debug = True)
