import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.setGeometry(0, 0, 1200, 900)
        self.do_paint = False
        self.first = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint and not self.first:
            print(1)
            self.qp = QPainter()
            self.first = True
        if self.do_paint:
            self.qp.begin(self)
            self.draw_flag(self.qp)
            self.qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        count = randint(2, 10)
        for i in range(count):
            x = randint(10, 1100)
            y = randint(10, 800)
            w = randint(10, 1200 - x)
            h = randint(10, 900 - y)
            qp.drawEllipse(x, y, w, h)
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
