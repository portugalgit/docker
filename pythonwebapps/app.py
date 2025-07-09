# app.py

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Render the hello.html template
    return '<h1>Welcome to AWS TrainingwithJagan Session !</h1><p> IN this topic you will how to Cointainerize of your python application using docker image How to host of your application . Please  visit of our website <a href="https://awstrainingwithjagan.com">www.awstrainingwithjagan.com</a> </p>'
