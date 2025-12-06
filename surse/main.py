import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui_interfata import Ui_MainWindow
from controller import Controller

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.controller = Controller(self.ui)
        self.ui.calcButton.clicked.connect(self.controller.calculeaza_ruta)
        
        self.ui.destLine.returnPressed.connect(self.controller.calculeaza_ruta)
        self.ui.startLine.returnPressed.connect(self.controller.calculeaza_ruta)

        self.ui.mapLabel.setScaledContents(True)
        self.resize(1200, 800)


app = QApplication(sys.argv)
f = MainWindow()
f.show()
sys.exit(app.exec())
