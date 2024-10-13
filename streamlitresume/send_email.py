import smtplib, ssl
import os

def send_email(user_message):
	host = "smtp.gmail.com"
	port = 465

	username = os.getenv("USERNAME")
	password = os.getenv("PASSWORD")


	receiver = "grow435@gmail.com"
	context = ssl.create_default_context()


	with smtplib.SMTP_SSL(host, port, context=context) as server:
		server.login(username, password)
		server.sendmail(username, receiver, user_message)



