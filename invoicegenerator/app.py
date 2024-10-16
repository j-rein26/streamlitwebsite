import pandas as pd 
from fpdf import FPDF
from pathlib import Path 
import glob

#Create a list of text filepaths
filepaths = glob.glob("Text/*.txt")

#Create one PDF 
pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
	# Add a page for each text file
	pdf.add_page()

	#Get the filename without the extension
	#Convert it to title case (e.g. Cat)
	filename = Path(filepath).stem
	name = filename.title()

	#add name to PDF
	pdf.set_font(family="Times", size=16, style="B")
	pdf.cell(w=50, h=8, txt=name, ln=1)

	with open(filepath, "r") as file:
		content = file.read()

	#add text for each title to PDF
	pdf.set_font(family="Times", size=12)
	pdf.multi_cell(w=0, h=6, txt=content)


pdf.output("animals.pdf")


