from tkinter import *
import time

def buttoncall():
    pass

master = Tk()
master.title('Voice Coding')
master.geometry("600x400")



variable = StringVar(master)
variable.set("Choose Language") # default value


txt = Text(master, height=20, borderwidth=0)
txt.insert(1.0, 'def factorial(n): \n\treturn 1 if (n==1 or n==0) else n * factorial(n - 1) \nnum='+'5'+' \nprint("Factorial of",num,"is",factorial(num))')
txt.pack(padx=10, pady=10)
txt.configure(state="disabled")


w = Canvas(master, width=250, height=200, bg='white')
w = OptionMenu(master, variable, "Python", "C++")
print(w)
btn = Button(master, text ="Stop Coding", command=buttoncall)
btn.pack()
w.pack()


w.pack()


mainloop()