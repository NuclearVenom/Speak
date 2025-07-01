from tkinter import *
import pyttsx3

root=Tk()
root.geometry("800x250")
root.maxsize(1000, 250)
root.minsize(600, 100)
root.title("Text to Audio")

def clear():
    v.set("")
    txt.update()

def s():
    engine = pyttsx3.init('sapi5')
    engine.setProperty('rate', rate.get())

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    speak(v.get())

Label(root, text="Type to Hear", font="Times_New_Roman 14 bold underline").pack(anchor=W)

v = StringVar()
txt = Entry(root, textvariable=v, font="lucida 12 bold")
txt.pack(fill=X)

m = Menu(root)
m.add_command(label="Exit", command=quit)
root.config(menu=m)

rate = Scale(root, from_=50, to=1000, orient=HORIZONTAL, tickinterval=50, length=1000, width=10)
rate.set(150)
rate.pack(anchor=S, pady=25)

Button(root, text="Clear", font="default 9 bold", borderwidth=3, command=clear).pack(side=RIGHT)
Button(root, text="Speak", font="default 9 bold", borderwidth=3, command=s).pack(side=RIGHT)

root.mainloop()