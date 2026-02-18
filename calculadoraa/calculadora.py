class Calculadora:
    def __init__(self, obj_num1, obj_num2, fecha_uso=None):
        self.obj_num1 = obj_num1
        self.obj_num2 = obj_num2
        self.fecha_uso = fecha_uso

        # Inicializamos resultados
        self.resultado_suma = None
        self.resultado_resta = None
        self.resultado_multi = None
        self.resultado_division = None

    def calcular_suma(self):
        self.resultado_suma = self.obj_num1.get_numero() + self.obj_num2.get_numero()
        return self.resultado_suma

    def calcular_resta(self):
        self.resultado_resta = self.obj_num1.get_numero() - self.obj_num2.get_numero()
        return self.resultado_resta

    def calcular_multi(self):
        self.resultado_multi = self.obj_num1.get_numero() * self.obj_num2.get_numero()
        return self.resultado_multi

    def calcular_division(self):
        if self.obj_num2.get_numero() != 0:
            self.resultado_division = self.obj_num1.get_numero() / self.obj_num2.get_numero()
        else:
            self.resultado_division = "Error: división por cero"
        return self.resultado_division

    def get_fecha_uso(self):
        return self.fecha_uso

    def set_fecha_uso(self, nueva_fecha):
        self.fecha_uso = nueva_fecha

    def mostrar_info(self):
        return (
            f"Numeros: {self.obj_num1.get_numero()} y {self.obj_num2.get_numero()}  "
            f"Suma: {self.resultado_suma}  "
            f"Resta: {self.resultado_resta}  "
            f"Multi: {self.resultado_multi}  "
            f"Division: {self.resultado_division}"
        )

    
    
        
    
    
    
    
    