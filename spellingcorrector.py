from textblob import TextBlob
import tkinter as tkwindow
from tkinter import *
def check():
    b=TextBlobe(e.get())
    corrected_text =Label(root,text=str(b.correct()))
    corrected_text.pack()
root=Tk()
root.title("SpellCheck")
root.geometry("400*200")

head=Lable(root,text='SpellCheck',font=('helvetica',14,'bold'))
head.pack()
e=Entry(root,width=200,borderwidth=5)
e.pack()
b=Button(root,text='Check',font=('helvetica',8,'bold'),fg='white',bg='brown',command=check)
b.pack()