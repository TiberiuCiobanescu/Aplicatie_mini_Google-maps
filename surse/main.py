import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTransform
from ui_interfata import Ui_MainWindow
from controller import Controller


class MapView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)

        self._zoom = 0
        self._zoom_min = -5   
        self._zoom_max = 15

    def wheelEvent(self, event):
        delta = event.angleDelta().y()

        if delta > 0:
            # zoom IN
            if self._zoom < self._zoom_max:
                factor = 1.25
                self._zoom += 1
                self.scale(factor, factor)
        elif delta < 0:
            # zoom OUT
            if self._zoom > self._zoom_min:
                factor = 0.8
                self._zoom -= 1
                self.scale(factor, factor)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.controller = Controller(self.ui, self)
        self.ui.calcButton.clicked.connect(self.controller.calculeaza_ruta)
        self.ui.destLine.returnPressed.connect(self.controller.calculeaza_ruta)
        self.ui.startLine.returnPressed.connect(self.controller.calculeaza_ruta)

        self.ui.mapLabel.hide()

        self.graphicsView = MapView(self.ui.centralwidget)
        self.scene = QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.scene)

        self.ui.verticalLayout.addWidget(self.graphicsView)

        self.graphicsView.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.graphicsView.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)

        self.resize(1200, 800)


app = QApplication(sys.argv)
f = MainWindow()
f.show()
sys.exit(app.exec())
