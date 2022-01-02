import tkinter as tk
from tkinter import ttk

def aktionsf():
    label3 = ttk.Label(root, text="Button gedrückt")
    label3.pack()


root = tk.Tk()
root.title("Handwritten Digits")
root.geometry("1000x600")
root.resizable(width=False, height=False)
root.configure(bg="#000056")

label1 = tk.Label(root, text="Hello World", bg="green")
label1.pack()

button1 = ttk.Button(root, text="Geht los", command = aktionsf)
button1.pack()
root.mainloop()