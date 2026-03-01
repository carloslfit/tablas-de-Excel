class Olla:
    def __init__(self):
        self.agua = None
        self.ingredientes = []

    def agregar_agua(self, agua):
        self.agua = agua

    def tiene_agua(self):
        return self.__agua is not None

    def agregar_ingrediente(self, ingrediente):
        if self.tiene_agua():
            self.ingredientes.append(ingrediente)

    def todos_dentro(self):
        return len(self.ingredientes) == 3