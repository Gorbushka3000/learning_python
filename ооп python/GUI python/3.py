from itertools import count
import tkinter as tk

def say_hello():
    print('hello')

def add_label():
    label = tk.Label(root, text='new')
    label.pack()

def counter():
    global count
    count += 1
    btn4['text'] = f'счетчик: {count}'
    if count % 2 == 0:
        btn1.configure(state=tk.NORMAL)
    else:
        btn1.configure(state=tk.DISABLED)

count = 0

root = tk.Tk()
root.geometry('400x400')
photo = tk.PhotoImage(file='icon.png')
root.iconphoto(False, photo)
root.config(bg='#FFB6C1')

btn1 = tk.Button(root,text='Hello',
                command=say_hello
                )
btn1.pack()

btn2 = tk.Button(root,text='add new label',
                command=add_label
                )
btn2.pack()

btn3 = tk.Button(root,text='add new lambda',
                command=lambda: tk.Label(root, text='new lambda').pack()
                )
btn3.pack()

btn4 = tk.Button(root,text=f'счетчик: {count}',
                command=counter,
                bg='red',
                activebackground= 'blue'
                )
btn4.pack()
root.mainloop()