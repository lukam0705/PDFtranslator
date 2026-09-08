import pymupdf
from GUI import filename as file

doc = pymupdf.open(file)

for page in doc:
    global text
    text = page.get_text()
    
