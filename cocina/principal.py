import tkinter as ventana
from tomate import Tomate
from cebolla import Cebolla
from cuchillo import Cuchillo
from pasta import Pasta
from agua import Agua
from olla import Olla

tomate = Tomate()
cebolla = Cebolla()
cuchillo = Cuchillo()
pasta = Pasta()
agua = Agua()
olla = Olla()

def cortar_tomate():
    if cuchillo.get_filo() > 0:
        cuchillo.cortar(tomate)
    actualizar()

def cortar_cebolla():
    if cuchillo.get_filo() > 0:
        cuchillo.cortar(cebolla)
    actualizar()

def hervir():

    # Si ya murieron (vida 0)
    if tomate.esta_listo() and cebolla.esta_listo():

        mensaje.set(" Todos los ingredientes están en la olla cocinándose")

        while pasta.get_coccion() < 100:
            pasta.hervir()

    else:
        mensaje.set(" Primero debes terminar de cortar los ingredientes")

    actualizar()

def afilar():
    cuchillo.afilar()
    mensaje.set("El cuchillo fue afilado")
    actualizar()

def actualizar():

    estado_cuchillo = ""
    if cuchillo.get_filo() == 0:
        estado_cuchillo = " (Necesita afilarse)"

    estado_tomate = ""
    if tomate.get_vida() == 0:
        estado_tomate = " (En la olla)"

    estado_cebolla = ""
    if cebolla.get_vida() == 0:
        estado_cebolla = " (En la olla)"

    texto.set(
        "Tomate: " + str(tomate.get_vida()) + estado_tomate +
        "Cebolla: " + str(cebolla.get_vida()) + estado_cebolla +
        "Pasta: " + str(pasta.get_coccion()) +
        "Filo cuchillo: " + str(cuchillo.get_filo()) + estado_cuchillo
    )

app = ventana.Tk()
app.title("Cocina")

texto = ventana.StringVar()
ventana.Label(app, textvariable=texto).pack()

mensaje = ventana.StringVar()
ventana.Label(app, textvariable=mensaje).pack()

ventana.Button(app, text="Cortar Tomate", command=cortar_tomate).pack()
ventana.Button(app, text="Cortar Cebolla", command=cortar_cebolla).pack()
ventana.Button(app, text="Hervir", command=hervir).pack()
ventana.Button(app, text="Afilar Cuchillo", command=afilar).pack()

actualizar()
app.mainloop()