class Controller:
    def __init__(self,ui):
        self.ui=ui
    def calculeaza_ruta(self):
        plecare=self.ui.startLine.text().strip()
        sosire=self.ui.destLine.text().strip()

        if not plecare or not sosire:
            self.ui.mapLabel.setText("COMPLETEAZA PLECARE SI SOSIRE ! ! !")
            return
    
        mesaj=f"Caluleaza ruta de la {plecare} la {sosire}"
        self.ui.mapLabel.setText(mesaj)