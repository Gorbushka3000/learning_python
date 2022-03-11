import tkinter as tk

root = tk.Tk()
root.geometry('400x400')
photo = tk.PhotoImage(file='icon.png')
root.iconphoto(False, photo)
root.config(bg='#FFB6C1')

# btn1 = tk.Button(root, text='hello 1')
# btn2 = tk.Button(root, text='hello 2')
# btn3 = tk.Button(root, text='hello 3')
# btn4 = tk.Button(root, text='hello 4')



# btn1.grid(row = 0, column=0)
# btn2.grid(row = 0, column=1)
# btn3.grid(row = 1, column=0, columnspan=2, stick='we')
# btn4.grid(row = 0, column=2, rowspan=2, stick='ns')


for i in range(5):
    for x in range(2):
        tk.Button(root, text=f'hello {i} {x}').grid(row=i, column=x, stick='we')

root.grid_columnconfigure(0, minsize=200)
root.grid_columnconfigure(1, minsize=100)

root.mainloop()