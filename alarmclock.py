from tkinter import *
from PIL import Image, ImageTk
import datetime
import time
from pygame import mixer
from tkinter import messagebox

root = Tk()
root.title("Alarm clock")
root.geometry("500x300")

alarm=StringVar()
rem=StringVar()
head = Label(root, text="Alarm Clock", font=('comic sans', 20,"bold"))
head.grid(row=0, columnspan=3,pady=10)


def setalarm():
	mixer.init()
	a=alarm.get()
	Alarmt=a
	currenttime=time.strftime("%H:%M")

	while Alarmt !=currenttime:
		currenttime=time.strftime("%H:%M")

	if Alarmt==currenttime:
		mixer.music.load('tone.mp3')
		mixer.music.play()
		msg=messagebox.showinfo('Reminder',f'{rem.get()}')
		if msg=='yes':
			mixer.music.stop()


image = Image.open("Alarm.png")
resizedimage = image.resize((200,200), Image.LANCZOS)
image_tk = ImageTk.PhotoImage(resizedimage)

img = Label(root, image=image_tk)
img.grid(rowspan=4, column=0)

inputt=Label(root,text="alarm time",font=('comic sans',18,"italic"))
inputt.grid(row=1,column=1)

alarmtime=Entry(root,textvariable=alarm,font=('comic sans',18,"italic"),width=6)
alarmtime.grid(row=1,column=2)

message=Label(root,text="Reminder",font=('comic sans',18,))
message.grid(row=2,column=1,columnspan=2)

messagein=Entry(root,textvariable=rem,font=('comic sans',18,"italic"))
messagein.grid(row=3,column=1,columnspan=2)

submit=Button(root,text="SUBMIT",font=('comic sans',18),command=setalarm)
submit.grid(row=4,column=1,columnspan=2)

root.mainloop()
