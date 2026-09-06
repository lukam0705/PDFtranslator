from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
root = Tk()
root.title('Translator')
root.resizable(False, False)
root.geometry('600x460')


def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    global filename
    filename = fd.askopenfilename(
        title='Prenesi PDF',
        initialdir='/',
        filetypes=filetypes)

open_button = ttk.Button(
    root,
    text='Prenesi PDF',
    command=select_file
)


open_button.pack(expand=True)

root.mainloop()

try:
    print(filename)
except:
    print("No Files Selected!")