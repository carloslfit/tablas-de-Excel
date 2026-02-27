import tkinter as ventana
from tomate import Tomate
from cebolla import Cebolla
from cuchillo import Cuchillo



tomate1 = Tomate("Tomate", 100, "Entero")
cebolla1 = Cebolla("Cebolla", 100, "Entero")
cuchi1 = Cuchillo(100, "Scalibu")



def cortar_tomate():
    cuchi1.hacer_corte(tomate1)
    lbl_resultado.config(text=tomate1.ver_info())

def cortar_cebolla():
    cuchi1.hacer_corte(cebolla1)
    lbl_resultado.config(text=cebolla1.ver_info())

def imprimir_info():
    texto = tomate1.ver_info() + "\n" + cebolla1.ver_info()
    lbl_resultado.config(text=texto)



ventana_principal = ventana.Tk()
ventana_principal.title("Juego Cocina")

lbl_titulo = ventana.Label(ventana_principal, text="Juego de Cocina")
lbl_titulo.pack()

btn_tomate = ventana.Button(ventana_principal, text="Cortar Tomate", command=cortar_tomate)
btn_tomate.pack()

btn_cebolla = ventana.Button(ventana_principal, text="Cortar Cebolla", command=cortar_cebolla)
btn_cebolla.pack()

btn_imprimir = ventana.Button(ventana_principal, text="Imprimir Info", command=imprimir_info)
btn_imprimir.pack()

lbl_resultado = ventana.Label(ventana_principal, text="")
lbl_resultado.pack()

ventana_principal.mainloop()
