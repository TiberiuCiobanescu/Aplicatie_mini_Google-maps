from incarcare_harta import HartaLoader
from vizualizare_harta import VizualizareHarta
from PyQt6.QtGui import QPixmap, QTransform
from PyQt6.QtCore import Qt
import osmnx as ox

class Controller:
    def __init__(self, ui, main_window):
        self.ui = ui
        self.main_window = main_window
        self.loader = HartaLoader()
        self.viewer = VizualizareHarta()

    def calculeaza_ruta(self):
        plecare = self.ui.startLine.text().strip()
        sosire = self.ui.destLine.text().strip()

        if not plecare or not sosire:
            self.ui.mapLabel.setText("Introduceți plecare și sosire!")
            return

        if plecare.lower() == sosire.lower():
            self.ui.mapLabel.setText("Plecarea și sosirea nu pot fi identice.")
            return

        G, ruta = self.loader.incarca_ruta(plecare, sosire)

        if G is None:
            self.ui.mapLabel.setText("Nu am putut găsi o rută între aceste adrese.")
            return

        lungimi = ox.utils_graph.get_route_edge_attributes(G, ruta, "length")
        dist_m = sum(lungimi)
        dist_km = dist_m/1000

        viteza_masina=35   
        viteza_pieton=5

        timp_masina_min=dist_km/viteza_masina*60
        timp_pieton_min=dist_km/viteza_pieton*60

        img_path = self.viewer.genereaza_imagine(G, ruta)
       
        pix = QPixmap(img_path)

        self.main_window.scene.clear()
        item = self.main_window.scene.addPixmap(pix)

        self.main_window.graphicsView.setTransform(QTransform())  # reset zoom
        self.main_window.graphicsView._zoom = 0 
      
        self.main_window.graphicsView.fitInView(
            item,
            Qt.AspectRatioMode.KeepAspectRatio
        )

        self.ui.statusbar.showMessage(f"Distanță: {dist_km:.2f} km | Mașina: ~{timp_masina_min:.0f} min | Pe jos: ~{timp_pieton_min:.0f} min")