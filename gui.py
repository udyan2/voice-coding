from tkinter import *
import time

def buttoncall():
    pass

master = Tk()
master.title('Voice Coding')
master.geometry("600x400")
variable = StringVar(master)
variable.set("Choose Language") # default value

my_text_label = Label(master, text='Select Your Programming Language From The Drop Down Menu Below \nDeveloped By: Udyan Sharma, Aditi Sheemar', width=100, height=20, bg='white')
my_text_label.pack(padx=10, pady=10)
w = Canvas(master, width=250, height=200, bg='white')
w = OptionMenu(master, variable, "Python", "C++")
print(w)
btn = Button(master, text ="Start Coding", command=buttoncall)
btn.pack()
w.pack()
mainloop()