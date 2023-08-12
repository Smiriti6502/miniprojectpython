from tkinter import *
import os

def restart():
	os.system("shutdown /r /t 1")

def restart_time():
	os.system("shutdown /r/t 20")

def logout():
	os.system("shutdown -1")

def shutdown():
	os.system("shutdown /s /t 1")

st=Tk()
st.title("shutdown app")
st.geometry("500x500")
st.config(bg="Blue")

r_button = Button(st,text="RESTART",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus", command=restart)
r_button.place(x=150,y=40,h=50,w=200)

rt_button = Button(st,text="RESTART TIME",font=("Time New Roman",18,"bold"),relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,h=50,w=200)


l_button = Button(st,text="LOG OUT",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=logout)
l_button.place(x=150,y=280,h=50,w=200)


s_button = Button(st,text="SHUT DOWN",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
s_button.place(x=150,y=390,h=50,w=200)

st.mainloop()
