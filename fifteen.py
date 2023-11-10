x = 15
while x > 0:
    a = int(input('Введите цифру 1, 2 или 3: '))
    if (a == 1 or a == 2 or a == 3) and x >= a:
        x -= a
        if x > 0:
            print(f'Осталось: {x}')
        else:
            print('Игра окончена!')

        if a == 1:
            print('Я беру 1')
            x -= 1
        elif a == 2:
            print('Я беру 1')
            x -= 1
        elif a == 3:
            print('Я беру 3')
            x -= 3

        if x > 0:
            print(f'Осталось: {x}')
        else:
            print('Игра окончена!')
    else:
        print('Некорректный ввод')
        continue
