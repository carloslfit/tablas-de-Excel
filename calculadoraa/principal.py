from usuario import Usuario
from calculadora import Calculadora
from numero import Numero

usuario1 = Usuario("1094571212", "Carlos")

numero1 = Numero(10)
numero2 = Numero(5)

Calculadora1 = Calculadora(numero1, numero2)

suma = Calculadora1.calcular_suma()
resta = Calculadora1.calcular_resta()
multi = Calculadora1.calcular_multi()
division = Calculadora1.calcular_division()

fecha_actual = Calculadora1.get_fecha_uso()
Calculadora1.set_fecha_uso("2026-18-02")
fecha_cambiada = Calculadora1.get_fecha_uso()

print(usuario1.mostrar_info())
print(Calculadora1.mostrar_info())
print(numero1.mostrar_info())
print(numero2.mostrar_info())
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multi: {multi}")
print(f"Division: {division}")
print(f"Fecha antes: {fecha_actual}")
print(f"Fecha despues: {fecha_cambiada}")
