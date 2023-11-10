from random import randint

x = 15

var = {1: 1,
       2: 1,
       3: 2,
       4: 3,
       5: randint(1, 3),
       6: 1,
       7: 2,
       8: 3,
       9: randint(1, 3),
       10: 1,
       11: 2,
       12: 3,
       13: randint(1, 3),
       14: 1
}

while x > 0:

    # ход игрока
    a = int(input('Введите цифру 1, 2 или 3: '))
    if (a == 1 or a == 2 or a == 3) and x > a:
        x -= a

    # ход программы
        print(f'Я беру {var[x]}')
        x -= var[x]

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
