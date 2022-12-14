import sys
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication(sys.argv)
label = QLabel('<h1>Hello world</h1>')
label.show()
app.exec()