#!/usr/bin/python
#-*- coding: utf-8 -*-
#Autor: Luis Angel Ramirez Mendoza

from flask import Flask, render_template, request, Response

from telesign.messaging import MessagingClient


customer_id = "id"
api_key = "llave"

app = Flask(__name__)

@app.route('/')
def route():
	return render_template("index.html")

@app.route('/envia', methods=['GET', 'POST'])
def geo_html():
	if request.method == 'POST':
		contry = request.form['contry']
		message_1 = request.form['message']
		print(contry)
		print(message_1)
		phone_number = contry
		message = message_1
		message_type = "ARN"
		messaging = MessagingClient(customer_id, api_key)
		response = messaging.message(phone_number, message, message_type)
		return render_template("index.html")

if __name__ == '__main__':
	app.run(host='localhost')