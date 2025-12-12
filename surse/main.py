import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QGraphicsView,
    QGraphicsScene
)
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtCore

from ui_interfata import Ui_MainWindow
from controller import Controller


#  MAP VIEW (ZOOM + DRAG) 
class MapView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setTransformationAnchor(
            QGraphicsView.ViewportAnchor.AnchorUnderMouse
        )

        self._zoom = 0
        self._zoom_min = -5
        self._zoom_max = 15

    def wheelEvent(self, event):
        delta = event.angleDelta().y()

        if delta > 0 and self._zoom < self._zoom_max:
            self._zoom += 1
            self.scale(1.25, 1.25)

        elif delta < 0 and self._zoom > self._zoom_min:
            self._zoom -= 1
            self.scale(0.8, 0.8)


#  MAIN WINDOW 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # INFO LABEL
        self.infoLabel = QtWidgets.QLabel()
        self.infoLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.infoLabel.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: 500;
                padding: 8px;
            }
        """)

        # LOADING LABEL 
        self.loadingLabel = QtWidgets.QLabel("Calculăm ruta…")
        self.loadingLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.loadingLabel.setStyleSheet("""
            QLabel {
                font-size: 15px;
                color: #4c8bf5;
                padding: 6px;
            }
        """)
        self.loadingLabel.hide()

        # Adăugăm în layout (FĂRĂ insert index)
        self.ui.verticalLayout.addWidget(self.loadingLabel)
        self.ui.verticalLayout.addWidget(self.infoLabel)

        # CONTROLLER 
        self.controller = Controller(self.ui, self)
        self.ui.calcButton.clicked.connect(self.controller.calculeaza_ruta)
        self.ui.startLine.returnPressed.connect(self.controller.calculeaza_ruta)
        self.ui.destLine.returnPressed.connect(self.controller.calculeaza_ruta)

        self.ui.mapLabel.hide()

        # (HARTĂ) 
        self.graphicsView = MapView(self.ui.centralwidget)
        self.scene = QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.scene)

        self.ui.verticalLayout.addWidget(self.graphicsView)

        self.resize(1200, 800)


#  APPLICATION 
app = QApplication(sys.argv)

#  DARK THEME PRO 
app.setStyleSheet("""
QWidget {
    background-color: #0f1115;
    color: #e6e6e6;
    font-family: "Segoe UI", Arial;
    font-size: 14px;
}

/* INPUT-uri */
QLineEdit {
    background-color: #1a1d24;
    border: 1px solid #2a2f3a;
    border-radius: 8px;
    padding: 8px;
    color: #ffffff;
}

QLineEdit:focus {
    border: 1px solid #4c8bf5;
}

/* BUTOANE */
QPushButton {
    background-color: #1f2430;
    border: 1px solid #2f3545;
    border-radius: 8px;
    padding: 8px 14px;
    font-weight: 500;
}

QPushButton:hover {
    background-color: #2a3040;
}

QPushButton:pressed {
    background-color: #151922;
}

/* LABEL-uri */
QLabel {
    color: #dcdcdc;
}
""")


window = MainWindow()
window.show()
sys.exit(app.exec())
