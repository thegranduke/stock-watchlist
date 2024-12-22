from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/', methods = ['GET','POST'])
def index():
    pass

@app.route('remove/<ticker>')
def remove(ticker):
    pass