import pymupdf
from GUI import filename as file
from localLLM import answer_question
doc = pymupdf.open(file)

for page in doc:
    global text
    text = page.get_text()
    print(answer_question(text))