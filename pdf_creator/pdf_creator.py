from fpdf import FPDF

name = input("Name:")


pdf = FPDF(orientation='portrait', unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(txt = 'CS50 Shirtificate', align="C")
pdf.cell(50, 50, name + ' took CS50', align="C")

pdf.output("tuto1.pdf")
