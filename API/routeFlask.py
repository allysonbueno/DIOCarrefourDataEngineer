
#python -m venv env - cria a instanvia env
#env\Scripts\activate - instancia (env) para comandos flask
#set FLASK_APP=main.py
#flask run

#pip install flask_restplus - ajuda a desenvolver uma API rest
#pip install Werkzeug=+0.16.0 #lib necessaria

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"