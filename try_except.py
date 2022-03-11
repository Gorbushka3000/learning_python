while True:
    try:
        enter = float(input('Введите число '))
        print(100/enter)
        break

    except ValueError:
        print('Вы ввели не число')

    except ZeroDivisionError:
        print('Делить на ноль нельзя')

    else:
        print('С первого раза')

    finally:
        print('finally')

print('Все норм')
