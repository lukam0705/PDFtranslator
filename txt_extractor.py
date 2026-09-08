import pymupdf
from GUI import filename as file
from localLLM import prijevod

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


for page in doc:
    tekst_stranice = page.get_text()
    blokovi = podijeli_tekst(tekst_stranice)
    for blok in blokovi:
        if not blok.strip():
            continue
        print(prijevod(blok))
