from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_number_book(start, end, filename="number_book.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    for number in range(start, end - 1, -1):
        c.setFont("Helvetica-Bold", 200)
        c.drawCentredString(width / 2.0, height / 2.0 - 100, str(number))
        c.showPage()
    c.save()

generate_number_book(500, 0)
