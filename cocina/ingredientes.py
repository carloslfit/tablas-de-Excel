class Ingredientes:

    def __init__(self,nombre,vida):
        self.nombre_vege=nombre
        self.vida_vege=vida

    def ver_info(self):
        info = f"nombre: {self.nombre_vege}, vida: {self.vida_vege}"
        return info
        
    def get_vida(self):
        return self.vida_vege
    
    def set_vida(self,nueva_vida):
        self.vida_vege = nueva_vida