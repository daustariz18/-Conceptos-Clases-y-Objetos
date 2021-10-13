

class Computador():

    pantalla = 14
    teclado = 'alfanumerico'
    mouse = 'touch'  # alambrico o inalambrico
    peso = 500  # gramos
    encendido = False

    def encender(self):
        # self hace referencia al propio objeto pertenciente a la clase
        self.encendido = True

    def estado(self):
        if(self.encendido):
            return "Esta encendido"
        else:
            return "Esta apagado"


mac = Computador()
mac.mouse = 'Inalambrico'
mac.teclado = 'Alfanumerico Inalambrico'
hp = Computador()  # Instaciar una clase
# hp.encender()
mac.encender()
print("el pc esta encendido:", hp.encendido)
print(hp.estado())
print("el mouse del mac es: ", mac.mouse)
print("el mouse del hp es: ", hp.mouse)
print("el mac esta:", mac.estado())
