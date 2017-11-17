import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import sys


class ClipboardTab(QtGui.QTabWidget):
    def __init__(self):
        super(ClipboardTab,self, ).__init__()
        
        
        self.setWindowTitle("XRender")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.resize(1200,600)
        self.setMinimumSize(600,300)
        
        
        
        #Widgets
        renderSettingsLabel = QtGui.QLabel("Render Settings")
        self.renderSettingsLabel_widget = QtGui.QTreeView()
        self.renderSettingsLabel_widget.setDragEnabled(True)
        
        search_label = QtGui.QLabel("Search")
        self.search_label_edit = QtGui.QLineEdit()
        renderView_label = QtGui.QLabel("Renderview")
        self.renderView_label_Frame = QtGui.QFrame()
        self.renderView_label_Frame.setAcceptDrops(True)
        self.text_note_text_edit = QtGui.QPlainTextEdit()
        self.render_button = QtGui.QPushButton("Render")
        
        self.main_widget = QtGui.QWidget()
            
        #Layout
        hlayout = QtGui.QVBoxLayout()
        hlayout.addWidget(renderSettingsLabel)
        hlayout.addWidget(self.renderSettingsLabel_widget)
        
        #received Layout 
        received_Layout = QtGui.QHBoxLayout()
        received_Layout.addLayout(hlayout)
        
             
