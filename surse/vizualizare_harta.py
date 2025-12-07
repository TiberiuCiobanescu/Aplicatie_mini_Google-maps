import os
import matplotlib.pyplot as plt
import osmnx as ox

class VizualizareHarta:
    def __init__(self, output_folder="./date/imagini"):
        self.output_folder = output_folder
        os.makedirs(output_folder, exist_ok=True)

    def genereaza_imagine(self, G, ruta):
        img_path = os.path.join(self.output_folder, "ruta.png")

        # coordonatele nodurilor de pe rută
        ruta_nodes = [(G.nodes[n]['x'], G.nodes[n]['y']) for n in ruta]
        xs = [p[0] for p in ruta_nodes]
        ys = [p[1] for p in ruta_nodes]

        x_start, y_start = ruta_nodes[0]
        x_end, y_end = ruta_nodes[-1]


        fig, ax = ox.plot_graph(
            G,
            bgcolor="#EFEFEF",
            node_size=0,
            edge_color="#808080",
            edge_linewidth=0.8,
            show=False,
            close=False,
            figsize=(12, 9), 
        )

        # ruta
        ax.plot(xs, ys, linewidth=3, color="red", label="Ruta")

        ax.scatter([x_start], [y_start], c="green", s=40, label="Start")
        ax.scatter([x_end], [y_end], c="blue", s=40, label="Sosire")

        ax.legend(loc="upper right")

        plt.savefig(img_path, dpi=200)
        plt.close(fig)

        return img_path
