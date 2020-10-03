from PySide2.QtWidgets import QMainWindow
#Decorador que se llama cuando se ejecute la aplicacion
from PySide2.QtCore import Slot
#clase Vista
from ui_mainwindow import Ui_MainWindow

#Controlador de vista
class MainWindow(QMainWindow):
    def __init__(self):
        #inicializar el objeto QMainWindow
        super(MainWindow, self).__init__()
        #Objeto de la clase Ui_MainWindow
        ui = Ui_MainWindow()
        #Se incrustan las configuraciones de la clase
        ui.setupUi(self)
        #Configurar el evento click del boton
        ui.pushButton.clicked.connect(self.click_agregar)
    
    @Slot()
    def click_agregar(self):
        print('click')
        
