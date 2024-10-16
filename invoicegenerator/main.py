import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

#get the data from the files
for filepath in filepaths:
	
	pdf = FPDF(orientation="P", unit="mm", format="A4")
	pdf.add_page()

	#getting file name and outputing invoice num.
	filename = Path(filepath).stem
	invoice_nr, date = filename.split("-")
	
	pdf.set_font(family="Times", size=16, style="B")
	pdf.cell(w=50, h=8, txt=f"Invoice #: {invoice_nr}", ln=1)

	pdf.set_font(family="Times", size=16, style="B")
	pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)

	#read the dataframe and iterrate over it to produce cells
	df = pd.read_excel(filepath, sheet_name="Sheet 1")

	#add a header
	columns = df.columns
	columns = [item.replace("_", " ").title() for item in columns]
	pdf.set_font(family="Times", size=10, style="B")
	pdf.set_text_color(80, 80, 80)
	pdf.cell(w=30, h=8, txt=columns[0], border=1)
	pdf.cell(w=70, h=8, txt=columns[1], border=1)
	pdf.cell(w=30, h=8, txt=columns[2], border=1)
	pdf.cell(w=30, h=8, txt=columns[3], border=1)
	pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

	#add rows to the table
	for index, row in df.iterrows():
		pdf.set_font(family="Times", size=10)
		pdf.set_text_color(80, 80, 80)
		pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
		pdf.cell(w=70, h=8, txt=str(row["product_name"]), border=1)
		pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), border=1)
		pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
		pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1)


	pdf.output(f"PDFs/{filename}.pdf")






