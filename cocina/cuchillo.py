class Cuchillo:
    def __init__(self,filo,marca):
         self.filo = filo
         self.marca = marca


    def hacer_corte(self,objeto):
        self.filo = self.filo - 25
        nueva_vida = objeto.get_vida()-50
        objeto.set_vida(nueva_vida)
        return objeto
    
    def afilar(self):
        self.filo = 100