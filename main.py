class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
    
    def cantidadAsientos(self):
        n=0
        for i in self.asientos:
            if i!=None:
                n+=1
        return n

    def verificarIntegridad(self):
        for i in self.asientos:
            if i!=None:
                if i.registro==self.registro:
                    pass
                if self.registro==self.motor.registro:
                    return ('Auto original')
        return ("Las piezas no son originales")

    


class Asiento:
    def __init__(self, color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro

    def cambiarColor(self,color):
        colores=["rojo", "amarillo", "verde", "blanco",  "negro"]
        if color in colores:
            self.color=color


class Motor:
    def __init__(self, numero, tipo, registro):
        self.numero=numero
        self.tipo=tipo
        self.registro=registro

    def asignarTipo(self,tipo):
        if tipo=='gasolina' or tipo=='electrico':
            self.tipo=tipo

    def cambiarRegistro(self,registro):
        self.registro=registro
