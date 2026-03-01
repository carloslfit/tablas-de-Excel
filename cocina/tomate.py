from ingredientes import Ingredientes

class Tomate(Ingredientes):

    def __init__(self):
        super().__init__("Tomate", 100)
        self.estado_vege = "Crudo"

    def imprimir_info(self):
        info = ""
        info = info + super().ver_info()
        info = info + "estado: " + self.estado_vege
        return info