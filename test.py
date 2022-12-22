import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import random


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.x = -1
        self.y = -1
        self.check = 0

    def initUI(self):
        self.setWindowTitle('ПОАРВАЛ')
        self.setGeometry(300, 300, random.randint(1, 1200), random.randint(1, 1200))


    def mouseMoveEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.check = 1
        elif event.button() == Qt.RightButton:
            self.check = 2
        self.x = event.x()
        self.y = event.y()
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.check = 3
            self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        if self.x > -1 and self.y > -1 and self.check == 1:
            qp.setBrush(QColor(random.randint(0, 250), random.randint(0, 250), random.randint(0, 250)))
            qp.drawRect(self.x, self.y, random.randint(1, 100), random.randint(1, 100))
        elif self.x > -1 and self.y > -1 and not self.check == 2:
            qp.setBrush(QColor(random.randint(0, 250), random.randint(0, 250), random.randint(0, 250)))
            koord = random.randint(1, 100)
            qp.drawEllipse(self.x, self.y, koord, koord)
        elif self.x > -1 and self.y > -1 and self.check == 3:
            qp.setBrush(QColor(random.choice(self.colors)))
            qp.drawPolygon((self.x + self.x // 2) + random.randint(1, self.x), (self.y - self.y // 2) + random.randint(1, self.y), (self.x, self.y), (self.x // 2, self.y * 2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
