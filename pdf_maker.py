import textwrap

from fpdf import FPDF
pdf = None


def stvoriPDF():
    global pdf

    pdf = FPDF()
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf")
    pdf.set_font("DejaVu", size=8)

def napraviStranicu(blokovi):
    pdf.add_page()
    for blok in blokovi:
        if not blok.strip():
            continue
            
        # textwrap prisilno reže riječi duže od 100 znakova kako ne bi razbile PDF
        siguran_tekst = textwrap.fill(blok, width=100, break_long_words=True)
        
        try:
            pdf.multi_cell(0, 5, siguran_tekst)
            # Dodajemo prazan red između blokova radi lakšeg čitanja
            pdf.ln(2) 
        except Exception as e:
            print(f"Preskočen problematičan blok teksta. Razlog: {e}")

def ZatvoriPDF():
    pdf.output("prevedeni.pdf")
    print("Done")