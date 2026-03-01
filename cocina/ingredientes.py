class Ingredientes:

    def __init__(self, nombre, vida):
        self.nombre_vege = nombre
        self.vida_vege = vida

    def get_vida(self):
        return self.vida_vege

    def set_vida(self, nueva_vida):
        self.vida_vege = nueva_vida

    def recibir_corte(self):
        nueva = self.get_vida() - 50
        if nueva < 0:
            nueva = 0
        self.set_vida(nueva)

    def esta_listo(self):
        return self.vida_vege == 0

    def ver_info(self):
        info = "nombre: " + self.nombre_vege + ", vida: " + str(self.vida_vege) + " "
        return info