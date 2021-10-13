class Pc():

    def __init__(self):
        self.__pantalla = 14  # 14 pulgadas
        self.mouse = 'alambrico'
        self.teclado = 'alfanumerico'
        self.encendido = False

    def encender(self):
        self.encendido = True
        return

    def estado_actual(self):

        if self.encendido is True:
            return "Esta Encendido"
        else:
            return "Esta Apagado"


macbook = Pc()
macbook.teclado = 'inalambrico'
hp = Pc()
hp.encender()
print("EL HP ", hp.estado_actual())
print("EL MACKBOOK", macbook.estado_actual())
print("EL MACKBOOK TIENE UNA PANTALLA DE :", macbook.mouse)
