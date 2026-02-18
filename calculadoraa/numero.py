class Numero:
    def __init__(self,numero):
        self.numero=numero
        
    def iniciar_control(self):
        self.control.iniciar_control()
        
    def get_numero(self):
        return self.numero
    
    def set_numero(self,nuevo_numero):
        self.numero=nuevo_numero
        
    def mostrar_info(self):
     print(f"numero es:{self.numero}")
     
    