from incarcare_harta import HartaLoader
from vizualizare_harta import VizualizareHarta
from PyQt6.QtGui import QPixmap
import osmnx as ox

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

        if plecare.lower() == sosire.lower():
            self.ui.mapLabel.setText("Plecarea și sosirea nu pot fi identice.")
            return

        G, ruta = self.loader.incarca_ruta(plecare, sosire)

        if G is None:
            self.ui.mapLabel.setText("Nu am putut găsi o rută între aceste adrese.")
            return

        lungimi = ox.utils_graph.get_route_edge_attributes(G, ruta, "length")
        dist_m = sum(lungimi)
        dist_km = dist_m / 1000

        viteza_kmh = 30
        timp_ore = dist_km / viteza_kmh
        timp_min = timp_ore * 60


        img_path = self.viewer.genereaza_imagine(G, ruta)
        self.ui.mapLabel.setPixmap(QPixmap(img_path))

        self.ui.statusbar.showMessage(f"Distanta: {dist_km:.2f} km | Timp estimat: {timp_min:.0f} minute")