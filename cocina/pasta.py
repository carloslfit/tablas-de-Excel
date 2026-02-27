class Pasta:

    def __init__(self,nombre,coccion):
        self.nombre=nombre
        self.coccion=coccion

    def hervir(self):
        self.coccion = self.coccion + 20

    def ver_info(self):
        return f"Pasta: {self.nombre}, Coccion: {self.coccion}"