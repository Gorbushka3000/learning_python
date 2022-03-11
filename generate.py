import os
x = input('Введите название документа ') 
g = [os.path.join(z,i)
     for z,x,c in os.walk('C:\\Users\glebd\Desktop')
     for i in c if x in i]
print(g)
