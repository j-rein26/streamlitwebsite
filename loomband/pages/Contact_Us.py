
import streamlit as st
import pandas as pd
from send_email import send_email

df = pd.read_csv("topics.csv")


with st.form(key="email_form"):
	st.header("Contact Us")
	user_email = st.text_input("Your Email")
	option = st.selectbox(
		'What topic would you like to discuss?',
		df['topic'])
	raw_message = st.text_area("Text")
	button = st.form_submit_button('Submit')
	message = f"""\
Subject: New email from {user_email}

From: {user_email}
Topic: {option}
{raw_message}
"""

if button:
	send_email(message)
	st.info("Your message was sent successfully.")


