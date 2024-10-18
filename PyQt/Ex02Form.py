from qtpy.QtWidgets import QApplication, QWidget, QFormLayout, QMessageBox
from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout

class SecondForm(QWidget):
    def __init__(self, name, address):
        super().__init__()
        self.setWindowTitle('Display Inputs')
        #self.resize(400, 400)

        #Field for name:
        self.name_label = QLabel(f'Name: {name}', self)

        #Field for Address:
        self.addr_label = QLabel(f'Address: {address}', self)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.addr_label)
        self.setLayout(layout)


class SampleForm(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QFormLayout()

        #Field for name:
        self.name_label = QLabel('Name')
        self.name_input = QLineEdit()
        self.layout.addRow(self.name_label, self.name_input)

        #Field for address
        self.addr_label = QLabel('Address')
        self.addr_input = QLineEdit()
        self.layout.addRow(self.addr_label, self.addr_input)

        #Creating Buttons
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.on_click)
        self.layout.addRow(self.submit_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Sample Form for UI')

    def on_click(self):
        name = self.name_input.text()
        addr = self.addr_input.text()
        # msg_box = QMessageBox()
        # msg_box.setText(f"Name: {name} from {addr}")
        # msg_box.exec_()

        second = SecondForm(name, addr)
        second.show()


if __name__ == '__main__':
    app = QApplication([])

    form = SampleForm()
    form.show()

    app.exec_()