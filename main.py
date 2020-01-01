from flask import Flask, render_template, request
import requests
import json
import random 

app = Flask(__name__)

jautajumi = { 
    0: { "jautajums": "Latvijas galvaspilsēta ir ?", "atbildes": "Rīga|Maskava|Pēterburga|Jelgava", "c": 0,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Latvia.png","j": 0}, 
    1: { "jautajums": "Afganistānas galvaspilsēta ir ?", "atbildes": "Luanda|Maskava|Kabula|Jelgava", "c": 2,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Afghanistan.png","j": 1}, 
    2: { "jautajums": "Albānijas galvaspilsēta ir ?", "atbildes": "Tirāna|Maskava|Pēterburga|Jelgava", "c": 0,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Albania.png","j": 2}, 
    3: { "jautajums": "Alžīrijas galvaspilsēta ir ?", "atbildes": "Rīga|Luanda|Pēterburga|Alžīra", "c": 3,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Algeria.png","j": 3}, 
    4: { "jautajums": "Andoras galvaspilsēta ir ?", "atbildes": "Rīga|Andora la Velja|Pēterburga|Buenosairesa", "c": 1,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Andorra.png","j": 4}, 
    5: { "jautajums": "Angolas galvaspilsēta ir ?", "atbildes": "Luanda|Maskava|Pēterburga|Jelgava", "c": 0,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Angola.png","j": 5}, 
    6: { "jautajums": "Argentīnas galvaspilsēta ir ?", "atbildes": "Rīga|Maskava|Pēterburga|Buenosairesa", "c": 3,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Argentina.png","j":6}, 
    7: { "jautajums": "Armēnijas galvaspilsēta ir ?", "atbildes": "Rīga|Erevāna|Pēterburga|Jelgava", "c": 1,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Armenia.png","j":7}, 
    8: { "jautajums": "ASV galvaspilsēta ir ?", "atbildes": "Rīga|Maskava|Pēterburga|Vašingtona", "c": 3,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-United-States-of-America.png","j": 8}, 
    9: { "jautajums": "Austrālijas galvaspilsēta ir ?", "atbildes": "Kanbera|Maskava|Pēterburga|Vašingtona", "c": 0,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Austria.png","j": 9}, 
    10: { "jautajums": "Baltkrievijas galvaspilsēta ir ?", "atbildes": "Rīga|Minska|Bridžtauna|Jelgava", "c": 1,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Belarus.png","j": 10}, 
    11: { "jautajums": "Bangladešas galvaspilsēta ir ?", "atbildes": "Daka|Maskava|Pēterburga|Jelgava", "c": 0,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Bangladesh.png","j": 11}, 
    12: { "jautajums": "Barbadosas galvaspilsēta ir ?", "atbildes": "Rīga|Maskava|Brisele|Bridžtauna", "c": 3,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Barbados.png","j": 12}, 
    13: { "jautajums": "Beļģijas galvaspilsēta ir ?", "atbildes": "Brisele|Maskava|Pēterburga|Jelgava", "c": 0,"flag":"https://www.countries-ofthe-world.com/flags-normal/flag-of-Belgium.png","j": 13},    
}
@app.route('/')
def home():
  return render_template("home.html", name = "PARAMETRS")
@app.route('/ajax')
def ajax():
 
  return json.dumps(produkti)
@app.route('/jautajums')
def jautajums():
  r = jautajumi[random.randint(0, 13)]
  return json.dumps(r)
@app.route('/atbilde', methods=["POST"])
def atbilde():
	j = request.args.get('j')
	atb = request.args.get('sk')
	if int(jautajumi[int(j)]["c"]) == int(atb):
		return '1'
	else:
		return '0'
 
 

app.run(host='0.0.0.0',port= 8020)