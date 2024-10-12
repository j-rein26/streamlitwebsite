
import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("A-lluminaristan")

content = """ 
A-lluminaristan is the place where you can find 
the Loom Bands you're looking for. Whether you're 
looking for colorful bands, designer bands, or bands
that just say "me". Let A-lluminaristan help brighten 
your world. 
"""
st.write(content)

st.subheader("Enter Our World of Loom Bands")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv", sep=";")

with col1:
	for index, row in df[:2].iterrows():
		st.subheader(row["title"])
		st.write(row["description"])
		st.image("images/" + row["image"])

with col2:
	for index, row in df[2:4].iterrows():
		st.subheader(row["title"])
		st.write(row["description"])
		st.image("images/" + row["image"])

with col3:
	for index, row in df[4:].iterrows():
		st.subheader(row["title"])
		st.write(row["description"])
		st.image("images/" + row["image"])




