import os
import math
import osmnx as ox
import networkx as nx
from geopy.geocoders import Nominatim

class HartaLoader:
    def __init__(self, cache_folder="./date/cache"):
        self.cache_folder = cache_folder
        os.makedirs(cache_folder, exist_ok=True)
        self.geolocator = Nominatim(user_agent="mini_google_maps")

    def geocode_city(self, nume):
        try:
            loc = self.geolocator.geocode(f"{nume}, București, Romania")
            return (loc.latitude, loc.longitude)
        except:
            return None

    def haversine(self, lat1, lon1, lat2, lon2):
        # distanță aproximativă între două coordonate
        R = 6371e3
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
        return 2*R*math.atan2(math.sqrt(a), math.sqrt(1-a))

    def nearest_node_manual(self, G, lat, lon):
        # cautare nod cel mai apropiat (fără SciPy)
        min_dist = float("inf")
        closest_node = None

        for node, data in G.nodes(data=True):
            d = self.haversine(lat, lon, data["y"], data["x"])
            if d < min_dist:
                min_dist = d
                closest_node = node

        return closest_node

    def incarca_ruta(self, plecare, sosire):

        coord1 = self.geocode_city(plecare)
        coord2 = self.geocode_city(sosire)

        if not coord1 or not coord2:
            print("[ERROR] Nu am gasit adresele introduse.")
            return None, None

        harta_path = os.path.join(self.cache_folder, "bucuresti.graphml")

        if os.path.exists(harta_path):
            print("[INFO] Încărcăm harta Bucureștiului din cache.")
            G = ox.load_graphml(harta_path)
        else:
            print("[INFO] Descărcăm harta rutieră a Bucureștiului (o singură dată)...")

            G = ox.graph_from_bbox(
                north=44.57,
                south=44.32,
                east=26.30,
                west=25.95,
                network_type="drive"
            )

            ox.save_graphml(G, harta_path)

        # folosim metoda noastră, FĂRĂ scipy:
        start = self.nearest_node_manual(G, coord1[0], coord1[1])
        end   = self.nearest_node_manual(G, coord2[0], coord2[1])

        try:
            ruta = nx.shortest_path(G, start, end, weight="length")
        except nx.NetworkXNoPath:
            print("[ERROR] Nu există o rută între cele două adrese.")
            return None, None

        return G, ruta
