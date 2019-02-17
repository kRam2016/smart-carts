from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form')
def hello():
    return "Hello World!"

