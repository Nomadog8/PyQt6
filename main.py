import sys
import random
from PyQt6.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsEllipseItem
from UI import Ui_MainWindow
from PyQt6.QtGui import QColor


class Form(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.view = QGraphicsScene()
        self.graphicsView.setScene(self.view)

        self.pushButton.clicked.connect(self.action)

    def action(self):

        act = random.randint(0, 5)

        for k in range(act):

            diametr = random.randint(0, 150)

            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            circle = QGraphicsEllipseItem(0, 0, diametr, diametr)
            circle.setBrush(color)
            circle.setPos(random.randint(0, 500), random.randint(0, 500))
            self.view.addItem(circle)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Form()
    ex.show()
    sys.exit(app.exec())