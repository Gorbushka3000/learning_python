import tkinter as tk
from tkinter import RAISED, RIGHT, font

root = tk.Tk()
root.geometry('400x400')
photo = tk.PhotoImage(file='icon.png')
root.iconphoto(False, photo)
root.config(bg='#FFB6C1')

label_1 = tk.Label(root, text='Hello world!',
                    bg='red',
                    fg='white',
                    font=('Arial', 15, 'bold'),
                    width=20,
                    height=10,
                    anchor='sw',
                    padx= 20,
                    pady=20,
                    relief=tk.RAISED,
                    bd=10,
                    justify=tk.RIGHT
                    )

label_1.pack()

root.mainloop()