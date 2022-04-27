fin = 1
exs = 0
while fin == 1:
    exs += 1
    print(f'\nВаше колличетво попыток: {exs}\n')
    mode = int(input('Фигуры для расчета:   Король_1    Ферзь_2     Конь_3:  '))
    x = int(input('Начало x: '))
    y = int(input('Начало y: '))
    x1 = int(input('Конец x: '))
    y1 = int(input('Конец y: '))


    if mode == 1:
        if x > 8 or x1 > 8 or y > 8 or y1 > 8:
            print('КЛЕТОЧКИ ПОСЧИТАЙ!!!')
        else:
            if x == x1 or y == y1 or (x == (x1 + 1) or x1 == (x + 1)) and (y == (y1 + 1) or y1 == (y + 1)):
                print('Ход возможен __ 1')
            else:
                print('Ход невозможен __ 0')

    elif mode == 2:
        if x > 8 or x1 > 8 or y > 8 or y1 > 8:
            print('КЛЕТОЧКИ ПОСЧИТАЙ!!!')
        else:
            if (x == y and x1 == y1) or(x == x1 or y == y1):
                print('Ход возможен __ 1')
            else:
                print('Ход невозможен __ 0')

    elif mode == 3:
        if x > 8 or x1 > 8 or y > 8 or y1 > 8:
            print('КЛЕТОЧКИ ПОСЧИТАЙ!!!')
        else:
            if x1 == (x + 1) and y1 == (y + 2) or x1 == (x + 2) and y1 == (y + 1) or x1 == (x - 1) and y1 == (y - 2) or x1 == (x - 2) and y1 == (y - 1):
                print('Ход возможен __ 1')
            elif x1 == (x + 1) and y1 == (y - 2) or x1 == (x + 2) and y1 == (y - 1) or x1 == (x - 1) and y1 == (y + 2) or x1 == (x - 2) and y1 == (y + 1):
                print('Ход возможен __ 1')
            else:
                print('Ход невозможен __ 0')
    fin = int(input('Хотите продолжить__1, хотите прервать__0 '))
