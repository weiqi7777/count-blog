import ui
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Ui(QWidget,ui.Ui_Form):
    def __init__(self,parent=None):
        super(Ui,self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
ui = Ui()
ui.show()
app.exec_()
