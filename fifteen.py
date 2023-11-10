from random import randint

x = 15

while x > 0:

    # ход игрока
    a = int(input('Введите цифру 1, 2 или 3: '))
    if (a == 1 or a == 2 or a == 3) and x > a:
        x -= a

    # ход программы
        if x == 14 or x == 10 or x == 6 or x == 2 or x == 1:
            print('Я беру 1')
            x -= 1
        elif x == 11 or x == 7 or x == 3:
            print('Я беру 2')
            x -= 2
        elif x == 12 or x == 8 or x == 4:
            print('Я беру 3')
            x -= 3
        elif x == 0:
            pass
        else:
            n = randint(1, 3)
            print(f'Я беру {n}')
            x -= n

    # конец игры
        if x > 1:
            print(f'Осталось: {x}')
        elif x == 1:
            print(f'Осталось: 1')
            print('Игра окончена! Вы проиграли')
            break
        else:
            print('Игра окончена! Вы выиграли')

    else:
        print('Некорректный ввод')
        continue
