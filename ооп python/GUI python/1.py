import tkinter as tk

root = tk.Tk()
photo = tk.PhotoImage(file='icon.png')
root.iconphoto(False, photo)
root.config(bg='#FFB6C1')
root.title('первое GUI приложение')
root.geometry('400x400')
root.minsize(300, 300)
root.maxsize(600, 600)
root.resizable(True, True)
root.mainloop()
