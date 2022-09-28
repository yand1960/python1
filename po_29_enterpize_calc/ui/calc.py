from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
from po_29_enterpize_calc.buslog.calculations import Calculations

class Calc(QWidget):

    def __init__(self):
        super().__init__()
        # self.setFixedHeight(200)
        self.setWindowTitle("Кальк")

        self.txtX = QLineEdit(self)
        self.txtX.setGeometry(10, 10, 100, 20)

        self.txtY = QLineEdit(self)
        self.txtY.setGeometry(10, 40, 100, 20)

        btnPlus = QPushButton(self)
        btnPlus.setText("+")
        btnPlus.setGeometry(10, 70, 40, 40)
        btnPlus.clicked.connect(self.btnPlus_click)

        btnMinus = QPushButton(self)
        btnMinus.setText("-")
        btnMinus.setGeometry(70, 70, 40, 40)


        self.txtZ = QLineEdit(self)
        self.txtZ.setGeometry(10, 120, 100, 20)

        self.show()

        self.calculations = Calculations("calcs.csv")

    def btnPlus_click(self):
        x = int(self.txtX.text())
        y = int(self.txtY.text())
        z = self.calculations.plus(x, y)
        self.txtZ.setText(str(z))


if __name__ == "__main__":
    app = QApplication([])
    calc = Calc()
    app.exec()
