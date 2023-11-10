x = 15
while x > 0:
    # ход игрока

    a = int(input('Введите цифру 1, 2 или 3: '))
    if (a == 1 or a == 2 or a == 3) and x >= a:
        x -= a

    # конец игры на ходе игрока
        if x > 0:
            print(f'Осталось: {x}')
        else:
            print('Игра окончена! Вы проиграли')
            break

    # ход программы
        if x == 14 or x == 10 or x == 6 or x == 2:
            print('Я беру 1')
            x -= 1
        elif x == 11 or x == 7 or x == 3:
            print('Я беру 2')
            x -= 2
        elif x == 12 or x == 8 or x == 4:
            print('Я беру 3')
            x -= 3
        else:
            print('Я беру 1')
            x -= 1


    # конец игры на ходе программы
        if x > 0:
            print(f'Осталось: {x}')
        else:
            print('Игра окончена! Вы выиграли')

    else:
        print('Некорректный ввод')
        continue
