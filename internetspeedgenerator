from tkinter import *
import speedtest


def speedcheck():
	sp=speedtest.Speedtest()
	sp.get_servers()
	down=str(round(sp.download()/(10**6),3))+"mbps"
	up=str(round(sp.upload()/(10**6),3))+"mbps"
	label2.config(text=down)
	label4.config(text=up)

sp=Tk()
sp.title("Internet Speed")
sp.geometry("500x700")
sp.config(bg="Red")

label=Label(sp,text="Internet Speed test", font=("Time new roman", 30,"bold"),bg="Red",fg="White")
label.place(x=50,y=40,h=50,w=380)

label1=Label(sp,text="Download speed", font=("Time new roman", 30,"bold"))#def same bg and fg
label1.place(x=50,y=130,h=50,w=380)

label2=Label(sp,text="00", font=("Time new roman", 30,"bold"),bg="Black",fg="White")
label2.place(x=50,y=200,h=50,w=380)

label3=Label(sp,text="Upload speed", font=("Time new roman", 30,"bold"))
label3.place(x=50,y=290,h=50,w=380)

label4=Label(sp,text="00", font=("Time new roman", 30,"bold"),bg="Black",fg="White")
label4.place(x=50,y=360,h=50,w=380)

button=Button(sp,text="Check Speed",font=("Time new roman", 30,"bold"),relief=RAISED,bg="Blue",command=speedcheck)
button.place(x=60,y=460,h=50,w=380)


sp.mainloop()
