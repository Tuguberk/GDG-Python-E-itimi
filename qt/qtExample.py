from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Qt

def calculate():
    value1 = float(input1.text())
    value2 = float(input2.text())
    result = value1 + value2
    result_label.setText(f"Result: {result}")

app = QApplication([])

window = QWidget()
window.setWindowTitle("Simple Calculator")

layout = QVBoxLayout()

input1 = QLineEdit()
input1.setPlaceholderText("Enter first number")
layout.addWidget(input1)

input2 = QLineEdit()
input2.setPlaceholderText("Enter second number")
layout.addWidget(input2)

calc_button = QPushButton("Calculate")
calc_button.clicked.connect(calculate)
layout.addWidget(calc_button)

result_label = QLabel("Result will be shown here")
result_label.setAlignment(Qt.AlignCenter)
layout.addWidget(result_label)

window.setLayout(layout)

qss_content = """
QWidget {
    background-color: #f0f0f0;
}

QLineEdit {
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

QPushButton {
    background-color: #0078d4;
    color: white;
    padding: 5px;
    border-radius: 5px;
}

QLabel {
    font-size: 14px;
    color: #333;
}

"""
window.setStyleSheet(qss_content)

window.show()

app.exec()
