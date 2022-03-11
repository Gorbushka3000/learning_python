import os
import time


list_1 = []
list_2 = []
for adress, dirs, files in os.walk('C:\\Users\glebd\Desktop\Tor Browser'):
    for file in files:
        full = os.path.join(adress, file)
        if '.txt' in full:
            list_1.append(full)
            
print(list_1)

for adress, dirs, files in os.walk('C:\\Users\glebd\Desktop'):
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86400:
            list_2.append(full)
            
print(list_2)
            
