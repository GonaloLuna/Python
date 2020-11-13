import math

class Forma:

    def __init__(self, color, coordCentro, nombre):
        self.color = color
        self.coordCentro = coordCentro
        self.nombre = nombre

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Color: ", self.color)
        print("Coordenadas del centro: ", self.coordCentro)

    def obtenerColor(self):
        self.color
        print("El color es: ", self.color)

    def cambiarColor(self, color):
        self.color = color
        print("El nuevo color es: ", self.color)

    def moverCentro(self, coord):
        self.coordCentro = coord
        print("El nuevo centro es: ", coord)

class Rectangulo(Forma):

    def __init__(self, color, coordCentro, nombre, ladoMayor, ladoMenor):
        Forma.__init__(self, color, coordCentro, nombre)
        self.ladoMayor = ladoMayor
        self.ladoMenor = ladoMenor

    def imprimir(self):
        Forma.imprimir(self)
        print("Lado Mayor: ", self.ladoMayor)
        print("Lado Menor: ", self.ladoMenor)

    def calcArea(self):
        area = self.ladoMayor * self.ladoMenor
        print("El área es: ", area)

    def calcPerimetro(self):
        perimetro = (self.ladoMayor * 2) + (self.ladoMenor * 2)
        print("El perímetro es: ", perimetro)

    def cambiarTamaño(self, escala):
        area = self.ladoMayor * self.ladoMenor
        tamaño = area * escala
        print("El tamaño nuevo es: ", tamaño)

class Elipse(Forma):

    def __init__(self, color, coordCentro, nombre, R, r):
        Forma.__init__(self, color, coordCentro, nombre)
        self.R = R
        self.r = r

    def imprimir(self):
        Forma.imprimir(self)
        print("Radio mayor: ", self.R)
        print("Radio menos: ", self.r)

    def calcArea(self):
        pi = 3.14
        area = pi * (self.R * self.r)
        print("El área es: ", area)

    def calcPerimetro(self):
        pi = 3.14
        op1 = (self.R * self.R) + (self.r * self.r)
        op2 = op1 / 2
        op3 = math.sqrt(op2)
        perimetro = (2 * pi) * op3
        print("El perímetro es: ", perimetro)

class Cuadrado(Rectangulo):

    def __init__(self, color, coordCentro, nombre, ladoMayor, ladoMenor):
        Rectangulo.__init__(self, color, coordCentro, nombre, ladoMayor, ladoMenor)
        Forma.__init__(self, color, coordCentro, nombre)

    def imprimir(self):
        Rectangulo.imprimir(self)

    def calcArea(self):
        Rectangulo.calcArea(self)

    def calcPerimetro(self):
        Rectangulo.calcPerimetro(self)

class Circulo(Elipse):

    def __init__(self, color, coordCentro, nombre, R, r, D):
        Elipse.__init__(self, color, coordCentro, nombre, R, r)
        Forma.__init__(self, color, coordCentro, nombre)
        self.D = D

    def imprimir(self):
        Elipse.imprimir(self)
        print("Diámetro: ", self.D)

    def calcArea(self):
        pi = 3.14
        area = pi * (math.sqrt(self.r))
        print("El área es: ", area)

    def calcPerimetro(self):
        pi = 3.14
        perimetro = 2 * pi * self.r
        print("Perímetro: ", perimetro)

rect1 = Rectangulo("Verde", "0,0", "Rectangulo", 8, 5)
elip1 = Elipse("Azul", "0,0", "Elipse", 4, 2)
cuad1 = Cuadrado("Rojo", "0,0", "Cuadrado", 4, 4)
circ1 = Circulo("Morado", "0,0", "Circulo", 2, 3, 6)

listaFormas = [rect1, elip1, cuad1, circ1]

for forma in listaFormas:
    forma.imprimir()
    print("")

print("")
print("")

for forma in listaFormas:
    forma.cambiarColor("Naranja")
    forma.moverCentro("3,6")
    forma.imprimir()
    print("")














