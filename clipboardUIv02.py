import PyQt4.QtGui as QtGui
import PyQt4.QtCore as QtCore
import sys



class Signaux(QtCore.QObject):
    def __init__(self):
        super(Signaux,self, ).__init__()

    def click(self):
        print 'Yeaahh you create a Click \o/'
    def quitApp(self):

        return
        """python quit()"""

    def nukeTheme(self):
        #import a text file with style sheet
        #text = open("style.txt")
        #self.setStylesheet(text)
        return """

        *{
        font : bold 11px;
        color : rgb(224,224,224);
        }
        QComboBox{

        background : rgb(60,60,60);
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

    def defaultTheme(self):
        return """ """
class sceneGraph(QtGui.QMainWindow):

    def __init__(self, parent =None):
        super(sceneGraph,self, ).__init__(parent)
        #self.setMouseTracking(True)

        #Init Signaux class
        self.clickAction = Signaux()

        #Init MainWindow
        self.setObjectName("mainWindow")
        self.setWindowTitle("XRender")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.sizeHint()
        self.setMinimumSize(500,200)
        self.setStyleSheet(self.nukeTheme())
        
        """Menu Actions""" 
        #Exit
        self.exitAction = QtGui.QAction('Exit',self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Quit App')
        self.exitAction.triggered.connect(self.close)
        
        #Edit menu 
        self.editAction = QtGui.QAction('Edit',self)
        
        #Render Menu
        self.renderAction = QtGui.QAction('Render',self) 
        
        #Tools Menu 
        self.renderAction = QtGui.QAction('Tools',self)
        
         #Help Menu 
        self.renderAction = QtGui.QAction('Help',self)
        #Set Menu Bar 
        self.statusBar()
        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('File')
        self.editMenu = self.menubar.addMenu('Edit')
        self.renderMenu = self.menubar.addMenu('Render')
        self.ToolsMenu = self.menubar.addMenu('Tools')
        self.ToolsMenu = self.menubar.addMenu('Help')
        #Set Action Menu 
        self.fileMenu.addAction(self.exitAction )
            


        #Create Widgets
        #---SCENEGRAPH WIDGETS---
                
        #Add sceneGraph Tab widget
        self.sceneGraphlabel = QtGui.QLabel("Scenegraph")
        self.sceneGraphTab = QtGui.QTabWidget()
        
        #Add scene List widget---
        self.sceneListlabel = QtGui.QLabel("Scenes")
        self.sceneListWidget = QtGui.QListView()
        self.sceneListWidget.setDragEnabled(True)


        #--- LAYOUT---
        #Set Right Splitter 
        self.rightSplitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.rightSplitter.addWidget(self.sceneListlabel)
        self.rightSplitter.addWidget(self.sceneListWidget )  

        #Set Main Splitter
        self.mainSplitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.mainSplitter.addWidget(self.sceneGraphTab)
        self.mainSplitter.addWidget(self.rightSplitter)
        
        #Set Central widget 
        self.setCentralWidget(self.mainSplitter)

    #--- UI THEMES
    def nukeTheme(self):
        #import a text file with style sheet
        #text = open("style.txt")
        #self.setStylesheet(text)
        return """
        *{
        font : bold 12px;
        color : orange;
        }

        QMenuBar{      
        spacing:  6px;          
        border-width: 0.5px;
        border-radius: 3px;
        border-color: orange;
        background-color : rgb(25,25,25);
        }
        
        QMenu::item{ 
        font = 9px;       
        border-radius: 5px;
        background-color : black;
        color: orange;
        }
        
        QTabWidget{
        background-color : rgb(20,20,20);
        }


        """
    def defaultTheme(self):
        return """ """
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
        self.setStyleSheet(self.sliderStylesheet())

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
