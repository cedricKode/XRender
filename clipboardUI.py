import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import sys


class Signaux(QtCore.QObject):
    def __init__(self):
        super(Signaux,self, ).__init__()

    def click(self):    
        print "Simple custom signal:",
        print "No arguments in this type of signal."    
        
        
class sceneGraph(QtGui.QTabWidget):       
    def __init__(self):
        super(sceneGraph,self, ).__init__()
        
        #Init Signaux Class
        self.clickAction = Signaux()
        
        self.setWindowTitle("XRender")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.resize(1200,600)
        self.setMinimumSize(600,300)

        #Widgets
        #---SCENEGRAPH
        #Scene List widget---
        scenaListlabel = QtGui.QLabel("Scenes")
        self.sceneListWidget = QtGui.QListView()
        self.sceneListWidget.setDragEnabled(True)
        
        #LCD TEST SIGNAL
        self.lcd = QtGui.QLCDNumber(self)
        
        #Search widget 
        searchSceneLabel = QtGui.QLabel("Search")
        self.searchSceneWidget = QtGui.QLineEdit()
        
        #Custom Slider
        self.customSliderleft = customSlider()
           
        #Stack widget
        stackLabel = QtGui.QLabel("Stack")
        self.stackWidget = QtGui.QListWidget()
        self.stackWidget.setAcceptDrops(True)
        
        #Text No Edit
        self.textNotetextEdit  = QtGui.QPlainTextEdit()
        
        #Close Button widget
        self.CloseBtn = QtGui.QPushButton("Close")
        self.CloseBtn.clicked.connect(self.clickAction.click)
        
        #Quit button widget
        self.quitbutton = QtGui.QPushButton("Quit" )
        self.quitbutton.clicked.connect(self.clickAction.click)
        #Main Widget
        self.sceneGraphMainWidget = QtGui.QWidget()
        
        #QpushButton
        btnLayout = QtGui.QHBoxLayout()
        btnLayout.addWidget(self.CloseBtn ) 
        btnLayout.addWidget(self.quitbutton)
                    
        
        #---Layout init---     
        #Main Layout
        mainLayout = QtGui.QHBoxLayout()
        vboxLeft = QtGui.QVBoxLayout()
        vboxRight = QtGui.QVBoxLayout()
                   
        # Left Layout        
        vboxLeft.addWidget(scenaListlabel)
        vboxLeft.addWidget(self.sceneListWidget)
        vboxLeft.addWidget(self.lcd)
        vboxLeft.addWidget(self.customSliderleft)
        searchLayout = QtGui.QHBoxLayout()
        searchLayout.addWidget(searchSceneLabel)
        searchLayout.addWidget(self.searchSceneWidget)
        vboxLeft.addLayout(btnLayout)
        vboxLeft.addLayout(searchLayout)
                
        # Right Layout
        vboxRight.addWidget(stackLabel)
        vboxRight.addWidget(self.stackWidget)
        vboxRight.addWidget(self.textNotetextEdit)
            
        # Add Layouts to main Layout        
        mainLayout.addLayout(vboxLeft)
        #mainLayout.addLayout(vboxRight)
        #mainLayout.addLayout(mainLayoutRight)
             
        # set main Layout to main Widget
        self.sceneGraphMainWidget.setLayout(mainLayout)
        
        # Add table to Main Window
        self.addTab(self.sceneGraphMainWidget, "SceneGraph")
        
        

       
class customSlider(QtGui.QSlider):
    def __init__(self, mini=0, maxi=100, color=None):
        super(customSlider, self).__init__()
        
        self.mini = mini
        self.maxi = maxi
        self.setStyleSheet(self.stylesheet())
        self.setOrientation(QtCore.Qt.Horizontal)
        self.setTickPosition(QtGui.QSlider.TicksAbove)
        self.setMouseTracking(True)
        self.setMouseTracking(True)
             
    #Layout
    def sliderLayout(self):
        self.slider = customSlider()        
        sliderLayout = QtGui.QVBoxLayout()
        sliderLayout.addWidget(self.slider)
        self.setLayout(sliderLayout)
        
    def stylesheet(self):
        return """ 
        QSlider::groove:horizontal {
        height: 4px;
        border: 1px solid black;
        border-radius: 3px;
        background: orange;
        }
        
        QSlider::handle:horizontal {        # Slots connector
28

        border: 1px solid black;
        height: 4px;
        width: 3px;
        border-radius: 1px ;
        background: darkGray;
        margin-top: -4px;
        margin-bottom: -4px;
        }
        QSlider::sub-page:horizontal {
        background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,stop: 0 white, stop: 1 orange);
        background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1, stop: 0 white, stop: 1 orange);
        height: 5px;
        border: 1px solid black;
        border-radius: 3px;
        }
        
        
        """


             
