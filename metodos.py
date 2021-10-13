# Metodo de Clase
class Rectangulo:

    def __init__(self, ancho, altura):
        self.altura = altura
        self.ancho = ancho

    def calcular_area(self):
        area = self.ancho * self.altura
        return area

    @classmethod
    def new_cuadrado(cls, side_length):
        return cls(side_length, side_length)


resultado_area = Rectangulo.new_cuadrado(5)
print(resultado_area.calcular_area())


class Animal:
    volador = True


class Cocodrilo(Animal):

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def new(cls, nombre):
        cls.volador = False
        return Cocodrilo(nombre)


cocodrilo = Cocodrilo.new('coco')
print(cocodrilo.nombre)
print(cocodrilo.volador)

# metodo estatico


class Circulo:

    @staticmethod
    def pi():
        return 3.1416

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.radio * self.radio * self.pi()


circulo = Circulo.pi()
print(circulo)
