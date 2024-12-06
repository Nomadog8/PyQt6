import sys
import random
from PyQt6.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsEllipseItem
from PyQt6.QtGui import QColor
from PyQt6 import uic

class Form(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.view = QGraphicsScene()
        self.graphicsView.setScene(self.view)

        self.pushButton.clicked.connect(self.action)

    def action(self):

        act = random.randint(0, 5)

        for k in range(act):

            diametr = random.randint(0, 150)

            circle = QGraphicsEllipseItem(0, 0, diametr, diametr)
            circle.setBrush(QColor('yellow'))
            circle.setPos(random.randint(0, 500), random.randint(0, 500))
            self.view.addItem(circle)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())