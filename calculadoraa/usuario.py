
    
class Usuario:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

    def get_cedula(self):
        return self.cedula

    def set_cedula(self, nueva_cedula):
        self.cedula = nueva_cedula
        
    def set_nombre(self,nuevo_nombre):
        self.nombre = nuevo_nombre
        
    def set_cedula(self, nuevo_cedula):
        self.cedula = nuevo_cedula   
        

    def mostrar_info(self):
        return f"Usuario: {self.nombre}, Cedula: {self.cedula}"

 
        
    

    
            
        
        
        