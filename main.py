import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from random import randint
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


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        uic.loadUi('form.ui', self)
        self.select.clicked.connect(self.sel)
        self.reset.clicked.connect(self.res)


    def sel(self):

        x = 15
        # global x
        print(f'x={x}')
        l = [0,
            self.c1_1.isChecked(),
            self.c1_2.isChecked(),
            self.c1_3.isChecked(),
            self.c1_4.isChecked(),
            self.c1_5.isChecked(),
            self.c1_6.isChecked(),
            self.c1_7.isChecked(),
            self.c1_8.isChecked(),
            self.c1_9.isChecked(),
            self.c1_10.isChecked(),
            self.c1_11.isChecked(),
            self.c1_12.isChecked(),
            self.c1_13.isChecked(),
            self.c1_14.isChecked(),
            self.c1_15.isChecked(),]


    # ход игрока
        b = sum(l)
        print(f'b={b}')
        a = 15 - b # взял игрок
        print(f'Игрок выбрал {a}')
        x -= a # осталось

        for i, j in enumerate(l, start=0):
            if not j and i != 0:
                exec(f'self.c1_{i}.setCheckable(False)')


    # ход программы
        k = 0
        for i, j in enumerate(l, start=0):
            if j and i != 0 and k < var[x]:
                k +=1
                exec(f'self.c1_{i}.setChecked(False)')
                exec(f'self.c1_{i}.setCheckable(False)')

        print(f'Я беру {var[x]}')
        x -= var[x]


     # конец игры
        if x > 1:
            print(f'Осталось: {x}')
            self.log.setText(f'Осталось {x}')

        elif x == 1:
            print(f'Осталось: 1')
            self.log.setText(f'Осталось {1}')
            print('Игра окончена! Вы проиграли')
            self.select.setText('Вы проиграли')
            self.select.setEnabled(False)
            self.reset.setEnabled(True)

        elif x == 0:
            print('Игра окончена! Вы выиграли')
            self.select.setText('Вы выиграли')
            self.select.setEnabled(False)
            self.reset.setEnabled(True)


    def res(self):
        for i in range(1, 16):
            exec(f'self.c1_{i}.setCheckable(True)')
            exec(f'self.c1_{i}.setChecked(True)')
            self.select.setEnabled(True)
            self.select.setText('Подтвердить выбор')
            self.reset.setEnabled(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
