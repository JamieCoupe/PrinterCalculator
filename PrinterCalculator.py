import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot


class PrinterCalculator(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'Printer Calculator'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.create_input_group()
        self.create_output_group()
        self.material_selector = QComboBox()
        self.material_selector.addItems(['PLA', 'Resin'])
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(QLabel('Material:'))
        windowLayout.addWidget(self.material_selector)
        windowLayout.addWidget(self.inputGroupBox)
        windowLayout.addWidget(self.outputGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def create_input_group(self):
        self.inputGroupBox = QGroupBox("Input")
        layout = QHBoxLayout()

        self.weight_in = QLineEdit()
        self.standard_fee = QLineEdit('0')

        layout.addWidget(QLabel('Weight (g):'))
        layout.addWidget(self.weight_in)
        layout.addWidget(QLabel('Standard Fee(p):'))
        layout.addWidget(self.standard_fee)

        self.inputGroupBox.setLayout(layout)

    def create_output_group(self):
        self.outputGroupBox = QGroupBox("Output")
        layout = QHBoxLayout()

        self.cost_out = QLineEdit()
        self.calculate_button = QPushButton('Calculate')
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)
        layout.addWidget(QLabel('Cost:'))
        layout.addWidget(self.cost_out)

        self.outputGroupBox.setLayout(layout)

    @pyqtSlot()
    def calculate(self):
        material = self.material_selector.currentText()
        standing_fee = 0
        if material in ['PLA']:
            standing_fee = '20'
        elif material in ['Resin']:
            standing_fee = '50'

        self.standard_fee.setText(f'{standing_fee}p')

        cost = (float(self.weight_in.text()) * 10) + int(standing_fee)
        if cost >= 100:
            cost = round(cost/100, 2)
            out = '£' + str(cost)
        else:
            out = str(round(cost, 0)) + 'p'

        self.cost_out.setText(out)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PrinterCalculator()
    sys.exit(app.exec_())
