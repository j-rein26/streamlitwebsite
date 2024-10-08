
import streamlit as st
import pandas 

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

c = st.container()

with col1:
	st.image("images/justin.jpg")

with col2:
	st.title("Justin Reinhardt")
	content = """
	Hello, I am Justin. I'm an aspiring Python Developer.
	My love for languages, a love to create, and a desire to
	continually learn led me to try coding. My journey started
	with learning Python in 2023. At this time, I'm comptent to
	fulfill the roles of a Junior Developer. I lived in Turkey
	for nearly 20 years working for a non-profit and teaching 
	English. I believed my experience working cross-culturally
	helps me be a better teammate. I would love the opportunity
	to help your team. 
	"""
	st.info(content)

content2 = """ 
Below you can find some of the apps I have built using Python.
Please feel free to contact me via the form below!
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
	for index, row in df[:10].iterrows():
		st.header(row["title"])
		st.write(row["description"])
		st.image("images/" + row["image"])
		st.write(f"[Source Code]({row['url']})")


with col4:
	for index, row in df[10:].iterrows():
		st.header(row["title"])
		st.write(row["description"])
		st.image("images/" + row["image"])
		st.write(f"[Source Code]([{row['url']}])")


