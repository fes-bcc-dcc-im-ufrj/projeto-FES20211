# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:57:53 2021

@author: Geraldo
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Xexeo/index.html')
def hello_world():
    return render_template('Xexeo/index.html')



