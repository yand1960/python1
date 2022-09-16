import sys, json

print(sys.path)
print(__file__, __name__)
print(json.__file__)

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedWidth(200)
        self.setFixedHeight(100)
        self.setWindowTitle("Hello")

        self.button = QPushButton(self)
        self.button.setText("Click me")
        self.button.setGeometry(10, 10, 180, 80)
        self.button.clicked.connect(self.button_click)

        self.show()

    def button_click(self):
        # print("Hello, world!")
        # напишите код, который надпись Hello, world! выведет на саму кнопку (11:30)
        self.button.setText("Hello, world!")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    app.exec()