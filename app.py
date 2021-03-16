from flask import Flask, render_template, request
# import jsonify
import requests
from os import path
import os
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('BN_option_prediction.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('Front_end.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Option_Type = request.form['Option_Type']
        Strike_Price=float(request.form['Strike_Price'])
        Prev_BN_CP=float(request.form['Prev_BN_CP'])
        BankNifty_OP=float(request.form['BankNifty_OP'])
        Change_In_BN=float(request.form['Change_In_BN'])
        Prev_Close=float(request.form['Prev_Close'])
        dist_frm_expiry=int(request.form['dist_frm_expiry'])
        if(Option_Type=='CE'):
                Option_Type=0
        else:
            Option_Type=1
        prediction=model.predict([[Option_Type,Strike_Price,Prev_BN_CP,BankNifty_OP,Change_In_BN,Prev_Close,dist_frm_expiry]])
        output=round(prediction[0],2)
        print(output)
        if output<0:
            return render_template('Front_end.html',prediction_texts="Parameter are not proper or either it a very deep OTM option.")
        else:
            return render_template('Front_end.html',prediction_text=f"Option Opening price is approx. {output}")
    else:
        return render_template('Front_end.html')

if __name__=="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
#     app.run(debug=True)
