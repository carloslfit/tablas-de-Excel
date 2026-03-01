class Agua:
    def __init__(self):
        self._temperatura = 25
        self._estado = "Fria"

    def get_temperatura(self):
        return self._temperatura

    def hervir(self):
        self._temperatura += 25
        if self._temperatura >= 100:
            self._temperatura = 100
            self._estado = "Hirviendo"

    def get_estado(self):
        return self._estado

    def mostrar_info(self):
        return "Agua Temp: " + str(self._temperatura) + " Estado: " + self._estado