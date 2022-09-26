from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton

class Calc(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedHeight(200)
        self.setWindowTitle("Кальк")

        self.txtX = QLineEdit(self)
        self.txtX.setGeometry(10,10,100,20)

        self.show()

if __name__ == "__main__":
    app = QApplication([])
    calc = Calc()
    app.exec()
