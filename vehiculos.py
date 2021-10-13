class Vehiculos():

    def __init__(self, marca, modelo) -> None:

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enmarcha = True

    def acelerar(self):

        self.acelera = True

    def frenar(self):

        self.frena = True

    def estado(self):
        print("marca :", self.marca, "\nModelo :", self.modelo, "\nEn Marcha:",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado:",
              self.frena)


class Moto(Vehiculos):
    hcaballito = ""

    def caballito(self):
        self.hcaballito = "voy haciendo el caballito"

    def estado(self):
        print("marca :", self.marca, "\nModelo :", self.modelo, "\nEn Marcha:",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenado:",
              self.frena, "\n", self.hcaballito)


miMoto = Moto('suzuki', 'jkt')
miMoto.caballito()
miMoto.estado()

Carro = Vehiculos('mazda', 2008)
Carro.arrancar()
Carro.acelerar()
Carro.estado()
