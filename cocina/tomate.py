from ingredientes import Ingredientes

class Tomate (Ingredientes):

    def __init__(self,nombre,vida,estado):
        super ().__init__(nombre,vida)
        self.estado_vege = estado


    def imprimir_info(self):
        info = super().ver_info()
        info = info + f",Estado: + {self.estado_vege}"
        return info