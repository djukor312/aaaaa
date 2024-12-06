import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6 import uic
from random import choice


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.a = []
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.do_paint:
            self.draw_flag(qp)

    def paint(self):
        self.x = choice(range(0, 300))
        self.y = choice(range(0, 300))
        self.d = choice(range(10, 100))
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        elip = (self.x, self.y, self.d, self.d)
        self.a.append(elip)
        for i in self.a:
            print(i)
            qp.drawEllipse(i[0], i[1], i[2], i[3])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()  # меняем название класса
    form.show()
    sys.exit(app.exec())
