from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from txt_extractor import uzmi_tekst
root = Tk()
root.title('Translator')
root.resizable(False, False)
root.geometry('300x200')


def select_file():
    filetypes = (
        ('text files', '*.pdf'),
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    global filename
    filename = fd.askopenfilename(
        title='Prenesi Tekstualnu Datoteku',
        initialdir='/',
        filetypes=filetypes)

open_button = ttk.Button(
    root,
    text='Prenesi Tekstualnu Datoteku',
    command=select_file
)

def submited_file():
    try:
        uzmi_tekst(filename)
    except:
        print("No Files Selected!")

send_file = ttk.Button(root,text='Pošalji',command=submited_file)

open_button.pack(expand=True)
send_file.pack(expand=True)

root.mainloop()

