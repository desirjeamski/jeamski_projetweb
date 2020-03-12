from flask import Flask,render_tamplate

app = Flask(__name__)



@app.route('/')
def projetcorrection():
    return render_tamplate(projetcorrection.html)