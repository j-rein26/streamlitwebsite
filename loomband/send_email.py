
import smtplib, ssl
import os

host = "smtp.gmail.com"
port = 465
username = "grow435@gmail.com"
password = os.getenv("PASSWORD")
receiver = "grow435@gmail.com"
context = ssl.create_default_context()


def send_email(message):
	with smtplib.SMTP_SSL(host, port, context=context) as server:
		server.login(username, password)
		server.sendmail(username, receiver, message)