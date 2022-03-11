import sys

url_list = ['text.txt', 'text2.txt', 'text25.txt', 'text3.txt']

list_defect = []
list_info = []

try:
    for url in url_list:
        try:
            r = open(url)
            list_info.append(r.read())
            print('тут')

        except Exception:
            list_defect.append(url)
            print('там')
            sys.exit()
            continue
finally:
    r = open('save.txt', 'a')
    for i in list_info:
        r.write(i)
    r.write(str(list_defect))
    r.close()
    print('Я все записал несмотря ни на что!!!!')
    
