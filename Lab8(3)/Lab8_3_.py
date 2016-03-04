import sys
from PySide.QtCore import *
from PySide.QtGui import *

def main():
    app = QtAPPlication(sys.argv)
    w = Simple_drawing_window()
    w.show()
 
class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QImage("images/rabbit.png")



    

