import tkinter as tk


root = tk.Tk()
root.title("Handwritten Digits")
root.geometry("1000x600")
root.resizable(width=False, height=False)
root.configure(bg="#000056")

headline = tk.Label(root, text="Handwritten Digits", fg="white", bg="#000056")
headline.pack()

canvas = tk.Canvas(root, width=100, height=100)
canvas.create_rectangle(0,0,100,100)
canvas.pack()

root.mainloop()