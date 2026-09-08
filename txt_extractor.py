import pymupdf
from localLLM import prijevod
from pdf_maker import ZatvoriPDF, napraviStranicu, stvoriPDF

def uzmi_tekst(file):

    doc = pymupdf.open(file)
   

    def podijeli_tekst(tekst, duljina_bloka=300):
        blokovi = []
        
        pocetak = 0

        while pocetak < len(tekst):
            kraj = tekst.find('.', pocetak + duljina_bloka)

            if kraj == -1:
                blok = tekst[pocetak:]
                blokovi.append(blok.strip())
                break

            blok = tekst[pocetak:kraj + 1]
            blokovi.append(blok.strip())
            pocetak = kraj + 1

        return blokovi

    stvoriPDF()
    for page in doc:
        prevedeni_blokovi = []
        tekst_stranice = page.get_text()
        blokovi = podijeli_tekst(tekst_stranice)
        for blok in blokovi:
            if not blok.strip():
                continue
            prevedeni_blokovi.append(prijevod(blok))
        napraviStranicu(prevedeni_blokovi)
    
    ZatvoriPDF()