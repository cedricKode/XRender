import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import sys
from clipboardUi import ClipboardTab


class ClipboardCore(ClipboardTab):
    def __init__(self):
        super(ClipboardCore,self).__init__()
        
        self.setWindowTitle("XRender")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.resize(1200,600)
        self.setMinimumSize(600,300)
        
        #Widgets


        
app = QtGui.QApplication(sys.argv)
tool = ClipboardCore()
tool.show()
app.exec_()
