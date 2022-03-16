import numpy as np
import pandas as pd
import sklearn
import pickle
from flask import Flask, request, render_template


app= Flask(__name__)


@app.route('/')

def home():
    return render_template('input.html')

# prediction function 
def Predictor(input_list): 
    to_predict = np.array(input_list).reshape(1, 20) 
    loaded_model = pickle.load(open("attrition.pkl", "rb")) 
    result = loaded_model.predict(to_predict) 
    return result[0] 
  
@app.route('/result', methods = ['POST']) 

# result function
def result(): 
    if request.method == 'POST':
        # listing the inputs 
        input_dict = request.form.to_dict() 
        input_list = list(input_dict.values()) 
        input_list = list(map(int, input_list))
        result = Predictor(input_list)         
        if int(result)== 1: 
            prediction ='Employee Attrites'
        else: 
            prediction ='Employee Will Not Attrite'            
        return render_template("output.html", prediction = prediction) 

if __name__ == "__main__":
    app.run(debug=True)
    app.config['TEMPLATES_AUTO_RELOAD'] = True