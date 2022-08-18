import numpy as np
from flask import Flask, request, jsonify, render_template
#from flask_ngrok import run_with_ngrok
import pickle
#from jinja2 import Template

app = Flask(__name__)

#run_with_ngrok(app)

@app.route('/')
def home():
  
    return render_template("index1.html")
#------------------------------About us-------------------------------------------
@app.route('/aboutus')

def aboutusnew():
    return render_template('aboutus.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Svm')
def svm():

    return render_template('Svm.html')

@app.route('/Decision')
def decisiontree():
 
    return render_template('decision.html')

@app.route('/knn')
def knn():
    return render_template('knn.html')

@app.route('/linear')
def linear():
    return render_template('linear.html')

@app.route('/Rf')
def randomforest():
    return render_template('Rf.html')

@app.route('/nvb')
def naivebayes():
    return render_template('nvb.html')

@app.route('/inter')

def internship():
    return render_template('internship.html')
  
@app.route('/code')

def QR():
    return render_template('QR.html')


@app.route('/predict',methods=['GET'])
def predict():
  age=float(request.args.get('age'))
  workclass =float(request.args.get('workclass'))
  education=float(request.args.get('education'))
  marital_status=float(request.args.get('marital_status'))
  occupation=float(request.args.get('occupation'))
  relationship=float(request.args.get('relationship'))
  race=float(request.args.get('race'))
  sex=float(request.args.get('sex'))
  hours_per_week=float(request.args.get('hours_per_week'))



  model=pickle.load(open('mp_decision_model.pkl','rb'))

  prediction = model.predict([[age,workclass,education,marital_status,occupation,relationship,race,sex,hours_per_week]])
    
        
  if prediction==0:
     message="Decision Tree model has predicted: Salary is less than 50,000"
  else:
     message="Decision Tree model has predicted: Salary is more than 50,000"
    
        
  return render_template('predict.html', prediction_text='{}'.format(message))

@app.route('/predict1',methods=['GET'])
def predict1():
    age=float(request.args.get('age'))
    workclass =float(request.args.get('workclass'))
    education=float(request.args.get('education'))
    marital_status=float(request.args.get('marital_status'))
    occupation=float(request.args.get('occupation'))
    relationship=float(request.args.get('relationship'))
    race=float(request.args.get('race'))
    sex=float(request.args.get('sex'))
    hours_per_week=float(request.args.get('hours_per_week'))
 


    model=pickle.load(open('mp_svm.pkl','rb'))
    
    prediction = model.predict([[age,workclass,education,marital_status,occupation,relationship,race,sex,hours_per_week]])
    
        
    if prediction==0:
      message="Support Vector Model has predicted : Salary is less than 50,000"
    else:
      message="Support Vector Model has predicted : Salary is more than 50,000"
    
        
    return render_template('predict.html', prediction_text=' {}'.format(message))


@app.route('/predict2',methods=['GET'])
def predict2():
  age=float(request.args.get('age'))
  workclass =float(request.args.get('workclass'))
  education=float(request.args.get('education'))
  marital_status=float(request.args.get('marital_status'))
  occupation=float(request.args.get('occupation'))
  relationship=float(request.args.get('relationship'))
  race=float(request.args.get('race'))
  sex=float(request.args.get('sex'))
  hours_per_week=float(request.args.get('hours_per_week'))



  model=pickle.load(open('mp_knn.pkl','rb'))
  
  prediction = model.predict([[age,workclass,education,marital_status,occupation,relationship,race,sex,hours_per_week]])
    
        
  if prediction==0:  
     message="K-Nearest Neighbour Model has predicted : Salary is less than 50,000"
    
  else:
     message="K-Nearest Neighbour Model has predicted : Salary is more than 50,000"
    
        
  return render_template('predict.html', prediction_text=' {}'.format(message))



@app.route('/predict3',methods=['GET'])
def predict3():
    age=float(request.args.get('age'))
    workclass =float(request.args.get('workclass'))
    education=float(request.args.get('education'))
    marital_status=float(request.args.get('marital_status'))
    occupation=float(request.args.get('occupation'))
    relationship=float(request.args.get('relationship'))
    race=float(request.args.get('race'))
    sex=float(request.args.get('sex'))
    hours_per_week=float(request.args.get('hours_per_week'))
   


    model=pickle.load(open('mp_random_forest.pkl','rb'))

    prediction = model.predict([[age,workclass,education,marital_status,occupation,relationship,race,sex,hours_per_week]])
    
        
    if prediction==0:
      message="Random Forest Model has predicted : Salary is less than 50,000"
    else:
      message="Random Forest Model has predicted : Salary is more than 50,000"
    
        
    return render_template('predict.html', prediction_text=' {}'.format(message))


@app.route('/predict4',methods=['GET'])
def predict4():
    age=float(request.args.get('age'))
    workclass =float(request.args.get('workclass'))
    education=float(request.args.get('education'))
    marital_status=float(request.args.get('marital_status'))
    occupation=float(request.args.get('occupation'))
    relationship=float(request.args.get('relationship'))
    race=float(request.args.get('race'))
    sex=float(request.args.get('sex'))
    hours_per_week=float(request.args.get('hours_per_week'))
  

    model=pickle.load(open('mp_naive.pkl','rb'))

    prediction = model.predict([[age,workclass,education,marital_status,occupation,relationship,race,sex,hours_per_week]])
    
        
    if prediction==0:
      message="Naive Bayes Model has predicted : Salary is less than 50,000"
    else:
      message="Naive Bayes Model has predicted :  Salary is more than 50,000"
    
        
    return render_template('predict.html', prediction_text=' {}'.format(message))

@app.route('/predict5',methods=['GET'])
def predict5():
    age=float(request.args.get('age'))
    workclass =float(request.args.get('workclass'))
    education=float(request.args.get('education'))
    marital_status=float(request.args.get('marital_status'))
    occupation=float(request.args.get('occupation'))
    relationship=float(request.args.get('relationship'))
    race=float(request.args.get('race'))
    sex=float(request.args.get('sex'))
    hours_per_week=float(request.args.get('hours_per_week'))
  

    model=pickle.load(open('mp_linear.pkl','rb'))

    prediction = model.predict([[age,workclass,education,marital_status,occupation,relationship,race,sex,hours_per_week]])
    
        
    if prediction==0:
      message="Linear Regression Model has predicted : Salary is less than 50,000"
    else:
      message="Linear Regression Model has predicted : Salary is more than 50,000"
    
        
    return render_template('predict.html', prediction_text=' {}'.format(message))




if __name__ == "__main__":
  app.run(debug=True)

