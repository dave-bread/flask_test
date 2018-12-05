# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, logging, Response, redirect, flash
import requests

#Flaskインスタンス作成
app = Flask(__name__)

#ルーティング
@app.route("/", methods = ["GET", "POST"])
def index():
    #index.htmlをレンダリング
    if request.method == 'POST':
        host_name = request.form['host_name']
        log_date = request.form['log_date']
        payload = { 'host_name': host_name }
        r = requests.get('http://192.168.100.110:3001/get')
        return render_template('index.html', host_name = r.text, log_date = log_date)
    else:
        return render_template('index.html')

#起動
app.run(host="192.168.100.110")
