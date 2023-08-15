from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="English", dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = combotxt.get()
    d = combotxt2.get()
    msg = source.get(1.0, END)
    textget = change(text=msg, src=s, dest=d)
    destn.delete(1.0, END)
    destn.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg='Black')

label = Label(root, text="Translator", font=("Time New Roman", 40, "bold"))
label.place(x=100, y=40, h=50, w=300)

frame = Frame(root)
frame.pack(side=BOTTOM)

label = Label(root, text="Source Text", font=("Time New Roman", 20, "bold"), bg="Black", fg="White")
label.place(x=100, y=100, h=20, w=300)

source = Text(frame, font=("Time New Roman", 40, "bold"), wrap=WORD)
source.place(x=10, y=130, h=150, w=480)

listtext = list(LANGUAGES.values())

combotxt = ttk.Combobox(frame, value=listtext)
combotxt.place(x=10, y=300, h=40, w=150)
combotxt.set("english")

button = Button(frame, text="Translate", relief=RAISED, command=data)
button.place(x=170, y=300, h=40, w=150)

combotxt2 = ttk.Combobox(frame, value=listtext)
combotxt2.place(x=330, y=300, h=40, w=150)
combotxt2.set("english")

label = Label(root, text="Destination Text", font=("Time New Roman", 20, "bold"), bg="Black", fg="White")
label.place(x=100, y=360, h=20, w=300)

destn = Text(frame, font=("Time New Roman", 40, "bold"), wrap=WORD)
destn.place(x=10, y=400, h=150, w=480)

root.mainloop()
