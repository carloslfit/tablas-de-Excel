class Cuchillo:
    def __init__(self):
        self.nombre = "Cuchillo"
        self.filo = 100

    def get_nombre(self):
        return self.nombre

    def get_filo(self):
        return self.filo

    def recibir_desgaste(self):
        self.filo = self.filo - 25
        if self.filo < 0:
            self.filo = 0

    def cortar(self, ingrediente):
        if self.filo > 0:
            ingrediente.recibir_corte()
            self.recibir_desgaste()

    def afilar(self):
        self.filo = 100

    def mostrar_info(self):
        return f"Cuchillo Filo: " + str(self.filo)