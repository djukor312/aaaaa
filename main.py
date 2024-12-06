from UI import Ui_MainWindow
import sys

from PyQt6.QtGui import QPainter, QColor, QBrush
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6 import uic
from random import choice


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.a = []
        
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.do_paint:
            self.draw_flag(qp)

    def paint(self):
        self.color = QColor(choice(range(256)), choice(range(256)), choice(range(256)))
        self.x = choice(range(0, 300))
        self.y = choice(range(0, 300))
        self.d = choice(range(10, 100))
        self.a.append((self.x, self.y, self.d, self.d, self.color))
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        for i in self.a:
            qp.setBrush(QBrush(i[4]))
            qp.drawEllipse(i[0], i[1], i[2], i[3])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()  # меняем название класса
    form.show()
    sys.exit(app.exec())

