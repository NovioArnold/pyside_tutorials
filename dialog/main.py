import sys
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

class Form(QDialog):
    
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")
        #create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show greetings")
        #create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        #set the layout
        self.setLayout(layout)
        #add button signal to greeting slot
        self.button.clicked.connect(self.greetings)

    #greet user
    def greetings(self):
        print(f'Hello {self.edit.text()}')

if __name__ == '__main__':
    #create the application
    app = QApplication(sys.argv)
    #Create and Show the form
    form = Form()
    form.show()
    #Run mainloop
    sys.exit(app.exec())
