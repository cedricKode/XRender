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
        #---SCENEGRAPH
        #Scene List widget
        scenaListlabel = QtGui.QLabel("Scenes")
        self.sceneListWidget = QtGui.QListView()
        self.sceneListWidget.setDragEnabled(True)
        #Search widget 
        searchSceneLabel = QtGui.QLabel("Search")
        self.searchSceneWidget = QtGui.QLineEdit()
        #Custom Slider
        self.customSliderleft = customSlider()
        self.customSliderRight = customSlider()
        #Stack widget
        stackLabel = QtGui.QLabel("Stack")
        self.stackWidget = QtGui.QListWidget()
        self.stackWidget.setAcceptDrops(True)
        #Text No Edit
        self.textNotetextEdit  = QtGui.QPlainTextEdit()
        #Add Button widget
        self.Addbutton = QtGui.QPushButton("Add")
        #Remove button widget
        self.Rmvbutton = QtGui.QPushButton("Remove")
        
        #Main Widget
        self.sceneGraphMainWidget = QtGui.QWidget()
        
        
        
        #---Layout ---     
        #Main Layout
        mainLayout = QtGui.QHBoxLayout()
        
        # Main  Left Layout
        mainLayoutLeft = QtGui.QVBoxLayout()
        mainLayoutLeft.addWidget(scenaListlabel)
        mainLayoutLeft.addWidget(self.sceneListWidget)
        searchLayout = QtGui.QHBoxLayout()
        searchLayout.addWidget(searchSceneLabel)
        searchLayout.addWidget(self.searchSceneWidget)
        mainLayoutLeft.addLayout(searchLayout)
        mainLayoutLeft.addWidget(self.customSliderleft)
        
        # Main Right Layout
        mainLayoutRight = QtGui.QVBoxLayout()
        mainLayoutRight.addWidget(stackLabel)
        mainLayoutRight.addWidget(self.stackWidget)
        mainLayoutRight.addWidget(self.textNotetextEdit)
        mainLayoutRight.addWidget(self.customSliderRight)
        btnLayout = QtGui.QHBoxLayout()
        btnLayout.addWidget(self.Addbutton) 
        btnLayout.addWidget(self.Rmvbutton)
        mainLayoutRight.addLayout(btnLayout)
             
        # Add Layout to main Layout 
        mainLayout.addLayout(mainLayoutLeft)
        mainLayout.addLayout(mainLayoutRight)
        
        # set main Layout to main Widget
        self.sceneGraphMainWidget.setLayout(mainLayout)
        
        # Add table to Clipboard
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


             
