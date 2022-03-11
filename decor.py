def decor(f):
    def wrapper():
        try:
            h = f()
        except Exception:
            print('Повторите ввод...')
            h = f()
        return h
    return wrapper

@decor
def make():
    enter = float(input('Введите число: '))
    return enter
@decor
def make2():
    enter = float(input('Введите число: '))
    return enter

make2()
make()
