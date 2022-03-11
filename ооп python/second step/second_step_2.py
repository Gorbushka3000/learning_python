from second_step import Verification
from tkinter import Button, Tk

class v2(Verification):

    def __init__(self, login, password, age):
        super().__init__(login, password)
        self.__save()
        self.age = age

    def __save(self):
        with open('users.txt') as r:
            for i in r:
                if f'{self.login, self.password}'+'\n' == i:
                    raise ValueError ('Такой пользователь уже существует')
        super().save()

    def show(self):
        return self.login , self.password

x = v2('gleb2','88888888', '20')

# class My_app(Tk):

#     def __init__(self):
#         Tk.__init__(self)
#         self.geometry('400x400')
#         self.setUI()
    
#     def setUI(self):
#         Button(self, text='OK').pack()

# root = My_app()
# root.mainloop()