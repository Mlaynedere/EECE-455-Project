from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')
    
@app.route("/about")
def about():
     return render_template('about.html')

@app.route("/DES")
def DES():
     return render_template('DES.html')

@app.route("/AES-CCM")
def AES():
     return render_template('AES.html')

@app.route("/Polyn")
def Polyn():
     return render_template('Polyn.html')