import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import random
import string


def generate_password():
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = string.digits
    special_chars = string.punctuation
    password_length = random.randint(8, 16)

    characters = lower_case + upper_case + numbers + special_chars
    password = "".join(random.sample(characters, password_length))
    return password


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(300, 250)
        frame = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center)
        self.move(frame.topLeft())
        self.setWindowTitle('Password Generator')

        self.button_generate = QPushButton(self)
        self.button_generate.move(115, 200)
        self.button_generate.setText("Generate!")
        self.button_generate.clicked.connect(self.generate)

        self.title = QLabel(self)
        self.title.setText("Your new password is:")
        self.title.move(87, 120)

        self.generated_password = QLineEdit(self)
        self.generated_password.resize(200, 35)
        self.generated_password.move(50, 140)
        self.generated_password.setAlignment(Qt.AlignCenter)
        self.font = QFont('Calibri', 20)
        self.generated_password.setFont(self.font)
        self.generated_password.setReadOnly(True)

        self.show()

    def generate(self):
        password = generate_password()
        self.generated_password.setText(password)


def main():
    app = QApplication(sys.argv)
    ex = PasswordGenerator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
