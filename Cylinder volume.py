import math

PI = math.pi

def radius():
    n = float(input('Диаметр цилиндра: '))
    n /=2
    return n

def height():
    m =float(input('Высота цилиндра: '))
    return m

def volume():
    r = radius()
    h = height()
    s = PI*r**2
    v = s*h
    
    return v

#print('Обьем цилиндра ', volume())

def mass(g):
    n = float(input('Удельный вес '))
    return g*n/1000

print('Вес цилиндра в кг: ', mass(volume()))
