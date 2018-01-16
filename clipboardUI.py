import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import sys


class Signaux(QtCore.QObject):
    def __init__(self):
        super(Signaux,self, ).__init__()

    def click(self):
    
        print "Yeah \m/:",
        print "you get a click"    

    def quitApp(self):
        

        print "Wanna quit ? "
    
class sceneGraph(QtGui.QTabWidget):
    
    def __init__(self, parent =None):
        super(sceneGraph,self, ).__init__(parent)
        #self.setMouseTracking(True)
       
        #Init Signaux class
        self.clickAction = Signaux()
        
        #Init Main windows
        self.setObjectName("SceneGraph")
        self.setWindowTitle("Nuke_Tool")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.resize(640,360)
        self.setMinimumSize(300,150)
        self.setStyleSheet(self.sceneGraphStylesheet())

        #Create Widgets
        #---SCENEGRAPH---
        #Add Scene List widget---
        scenaListlabel = QtGui.QLabel("Scenes")
        self.sceneListWidget = QtGui.QListView()
        self.sceneListWidget.setDragEnabled(True)
        
        #Add LCD TEST SIGNAL
        self.lcd = QtGui.QLCDNumber()
        #self.lcd.setDigitCount(1)
    
    
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
        self.quitbutton.clicked.connect(self.clickAction.quitApp)
        
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
           
           
    def sceneGraphStylesheet(self):
        #import a text file with style sheet
        #text = open("style.txt")
        #self.setStylesheet(text)
        return """ 
        
        *{
        font : bold 11px;
        color : rgb(224,224,224);
        }
        
        QPushButton{
        color : black;
        background-color: orange;
        border-style: inset;
        border-width: 1.6px;
        border-radius: 5px;
        border-color: black;
        font: bold 10px ;
        min-width: 10em;
        padding: 2px;
        }
                
        QPushButton::pressed{        
        background-color : black;
        border-style: inset; 
        border-width: 1px; 
        color : white;     
        }
        
        sceneGraph{
        background: rgb(80,80,80);
        border-color: black;
        }
        
        QLineEdit{
        color :  white;
        font  : bold 10px; 
        background: rgb(112,112,112);
        }
        
        QLineEdit{
        color :  white;
        font  : bold 10px; 
        background: rgb(96,96,96);
        }
        
        QLineEdit:hover{
        background: rgb(8,8,8);
        }
        
        QListWidget,QPlainTextEdit,QListView {
        background : rgb(70,70,70);
        
        }
        
        QLCDNumber{
        background : rgb(40,40,40);
        }
        """
        
class customSlider(QtGui.QSlider):
    def __init__(self, mini=0, maxi=100):
        super(customSlider, self).__init__(QtCore.Qt.Horizontal)
        """Init
        :param  mini: maximum value
        :param  maxi: minimum value
        :param  width : slider's  width
        :param  color: slider's color
        :param  event.x : position of the  mouse on the X axis
        :param  value : set the handle value  for the position
        """
        
        self.setValue(mini)

        self.setMinimum(mini )
        self.setMaximum(maxi )
        self.width = float(maxi - mini)
        self.setMouseTracking(True)
        self.mini = mini
        self.maxi = maxi
        #self.ticks = Ticks(mini, maxi)
        #self.setTickInterval((maxi - mini) / 10)
        #self.setTickPosition(QtGui.QSlider.TicksAbove)
        
        self.setStyleSheet(self.sliderStylesheet())
        
    def mousePressEvent(self, event):
        """Overide the mousePressEvent 
        """
        value = self.width / self.size().width() * event.x() * 1000
        value = value + self.mini * 1000
        self.setValue(value)
        super(customSlider, self).mousePressEvent(event)

    #Layout
    def sliderLayout(self):
        self.slider = customSlider()        
        sliderLayout = QtGui.QVBoxLayout()
        sliderLayout.addWidget(self.slider)
        self.setLayout(sliderLayout)
        
    def sliderStylesheet(self):
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
    
