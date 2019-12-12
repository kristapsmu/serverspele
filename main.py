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
@app.route('/about')
def about():
  return render_template("about.html")
@app.route('/contact')
def contact():
  return render_template("contact.html")
@app.route('/shop')
def shop():
  return render_template("shop.html",produkts = produkti,produktugarums=len(produkti),summa = 0)
@app.route('/prametri')
def prametri():
  parametri = request.args
   
  return (json.dumps(parametri, sort_keys=True))
@app.route('/nauda')
def nauda():
  r = ""
  url = 'https://api.exchangerate-api.com/v4/latest/EUR'
  headers = {'content-type': 'application/json'}
  r = requests.post(url, '', headers=headers)
  uzjson = r.json()
  return render_template("nauda.html",masivs = uzjson)
@app.route('/bilde')
def bilde():
  r = ""
  url = 'https://dog.ceo/api/breeds/image/random'
  headers = {'content-type': 'application/json'}
  r = requests.get(url, '', headers=headers)
  uzjson = r.json()
  return render_template("bilde.html",masivs = uzjson)
app.run(host='0.0.0.0',port= 8020)