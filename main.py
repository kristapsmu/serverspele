from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)
produkti = {
  "olas":{
    "cena":20,
    "izdruka": "Olas"
  },
  "piens":{
    "cena":20,
    "izdruka": "Piens"
  },
  "maize":{
    "cena":170,
    "izdruka": "Piens"
  },
}
@app.route('/')
def home():
  return render_template("home.html", name = "PARAMETRS")
@app.route('/ajax')
def ajax():
 	
  return render_template("ajax.html")
 
 
app.run(host='0.0.0.0',port= 8020)