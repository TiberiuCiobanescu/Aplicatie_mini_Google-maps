from incarcare_harta import HartaLoader
from vizualizare_harta import VizualizareHarta
from PyQt6.QtGui import QPixmap

class Controller:
    def __init__(self, ui):
        self.ui = ui
        self.loader = HartaLoader()
        self.viewer = VizualizareHarta()

    def calculeaza_ruta(self):
        plecare = self.ui.startLine.text().strip()
        sosire = self.ui.destLine.text().strip()

        if not plecare or not sosire:
            self.ui.mapLabel.setText("Introduceți plecare și sosire!")
            return

        G, ruta = self.loader.incarca_ruta(plecare, sosire)

        if G is None:
            self.ui.mapLabel.setText("Nu am putut calcula ruta.")
            return

        img_path = self.viewer.genereaza_imagine(G, ruta)

        self.ui.mapLabel.setPixmap(QPixmap(img_path))
