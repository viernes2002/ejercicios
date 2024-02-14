from figura import Circulo, Punto

circulo_1: Circulo = Circulo(5, Punto(2, 3))
punto_1: Punto = Punto(-2, -3)
print(circulo_1.contiene(punto_1))