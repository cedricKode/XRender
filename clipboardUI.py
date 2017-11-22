import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import sys


class Signaux(QtCore.QObject):
    def __init__(self):
        super(Signaux,self, ).__init__()

    def click(self):
    
        print "Simple custom signal:",
        print "No arguments in this type of signal."    

    def quitApp(self):
        
        return 
        """quit()"""
    
    
class sceneGraph(QtGui.QTabWidget):
    
    def __init__(self, parent =None):
        super(sceneGraph,self, ).__init__(parent)
        self.setMouseTracking(True)
       
        #Init Signaux class
        self.clickAction = Signaux()
        
        #Init Main windows
        self.setWindowTitle("XRender")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.resize(640,360)
        self.setMinimumSize(300,150)


        #Create Widgets
        #---SCENEGRAPH---
        #Add Scene List widget---
        scenaListlabel = QtGui.QLabel("Scenes")
        self.sceneListWidget = QtGui.QListView()
        self.sceneListWidget.setDragEnabled(True)
        
        #Add LCD TEST SIGNAL
        self.lcd = QtGui.QLCDNumber(self)
        
        #Add Search widget 
        searchSceneLabel = QtGui.QLabel("Search")
        self.searchSceneWidget = QtGui.QLineEdit()
        
        #import Custom Slider class
        self.customSliderleft = customSlider()
        self.customSliderleft.valueChanged.connect(self.lcd.display)
        
        #Add Stack widget
        stackLabel = QtGui.QLabel("Stack")
        self.stackWidget = QtGui.QListWidget()
        self.stackWidget.setAcceptDrops(True)
        
        #Text No Edit
        self.textNotetextEdit  = QtGui.QPlainTextEdit()
        
        #Set Close Button widget
        self.CloseBtn = QtGui.QPushButton("Close")
        self.CloseBtn.clicked.connect(self.clickAction.click)
        
        #Set Quit button widget
        self.quitbutton = QtGui.QPushButton("Quit" )
        self.quitbutton.clicked.connect(self.clickAction.click)
        
        #Add Main Widget
        self.sceneGraphMainWidget = QtGui.QWidget()
        
        #Add QpushButton  to Layout
        btnLayout = QtGui.QHBoxLayout()
        btnLayout.addWidget(self.CloseBtn ) 
        btnLayout.addWidget(self.quitbutton)
                    
        
        #---Layout init---     
        #MainWindow/Splitter Layout init 
        mainLayout = QtGui.QHBoxLayout()
        self.splitterRight = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.splitterRight.setChildrenCollapsible(False)

        
                   
        # Left Layout
        vboxLeft = QtGui.QVBoxLayout()        
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
        self.splitterRight.addWidget(stackLabel)
        self.splitterRight.addWidget(self.stackWidget)
        self.splitterRight.addWidget(self.textNotetextEdit)
            

        
        # Add Layouts to Main Layout        174
        mainLayout.addLayout(vboxLeft)
        mainLayout.addWidget(self.splitterRight)


        # set main Layout to main Widget
        self.sceneGraphMainWidget.setLayout(mainLayout)
    
        # Add table to Main Window
        self.addTab(self.sceneGraphMainWidget, "SceneGraph")
           
        
class customSlider(QtGui.QSlider):
    def __init__(self, mini=0, maxi=100, color=None):
        super(customSlider, self).__init__(QtCore.Qt.Horizontal)
        
        #self.ticks = Ticks(mini, maxi)
        self.setValue(mini)
        self.mini = mini
        self.maxi = maxi
        self.setMinimum(mini *10)
        self.setMaximum(maxi * 10)
        self.setTickPosition(QtGui.QSlider.TicksAbove)
        #self.setTickInterval((maxi - mini) / 10)
        self.setMouseTracking(True)
        self.setStyleSheet(self.stylesheet())
        
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
        
        QSlider::handle:horizontal {
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
        


             
