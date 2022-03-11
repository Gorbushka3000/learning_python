import tkinter as tk

def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')

def delete_entry():
    name.delete(0, tk.END)
    password.delete(0, tk.END)

def sumbit():
    print(name.get())
    print(password.get())
    delete_entry()

root = tk.Tk()
root.geometry('400x400')
photo = tk.PhotoImage(file='icon.png')
root.iconphoto(False, photo)
root.config(bg='#FFB6C1')

tk.Label(root, text='Name').grid(row=0, column=0,stick='w')
name = tk.Entry(root)
password = tk.Entry(root, show='#')
name.grid(row=0, column=1)
password.grid(row=1, column=1)

tk.Button(root, text='get', command=get_entry).grid(row=2, column=0, stick='we')
tk.Button(root, text='delete', command=delete_entry).grid(row=2, column=1, stick='we')
tk.Button(root, text='sumbit', command=sumbit).grid(row=3, column=0, stick='we')
tk.Button(root, text='insert', command=lambda : name.insert(1,'hello')) \
    .grid(row=2, column=2, stick='we')


root.grid_columnconfigure(0, minsize=100)
root.grid_columnconfigure(1, minsize=100)
root.grid_columnconfigure(2, minsize=100)


root.mainloop()