import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

#Greetings
@Slot()
def say_hello():
    print("Button clicked, Hello!")

#Create the application
app = QApplication(sys.argv)

#Create a button
button = QPushButton('plzz click me :)')

#Connect the button to the function
button.clicked.connect(say_hello)

#Show button in app
button.show()

#Run the main loop
app.exec()