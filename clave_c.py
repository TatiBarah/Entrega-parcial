import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la multiplicacion de 2 numeros
2*4 = 8
"""


# start-->
def multiplicar(num1, num2):
    return num1 * num2


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros divisibles entre 3 y 5 del 1 al 1000
"""


# start-->
def sumaDivTresYCinco():
    numero = 1
    suma = 0
    while numero <= 1000:
        if (numero % 5 == 0) and (numero % 3 == 0):
            suma += numero
        numero += 1
    return suma


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el generatriz, area y el volumen de un cono
radio = 5 m
altura = 11 m

generatriz: square_root(altura^2 + radio^2)
area: pi*radio*(radio+generatriz)
volumen: (1/3)*pi*radio^2*altura
"""


# start-->
radio1 = 0
altura1 = 0


def definicionCono(radio, altura):
    global radio1
    global altura1
    radio1 = radio
    altura1 = altura
    generatriz = obtenerGeneratriz()
    area = obtenerArea()
    volumen = obtenerVolumen()
    result = tuple(generatriz, area, volumen)
    return result


def obtenerGeneratriz():
    radio = radio1
    altura = altura1
    result = math.sqrt((radio ^ 2) + (altura ^ 2))
    return result


def obtenerArea():
    radio = radio1
    altura = altura1
    result = math.pi * (radio * (radio + math.sqrt((radio ^ 2) + (altura ^ 2))))
    return result


def obtenerVolumen():
    radio = radio1
    altura = altura1
    result = (math.pi * radio ^ 2 * altura) / 3
    return result


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""


# start-->
class Cono:
    def definicionCono(self, generatriz, area, volumen):
        self.__generatriz = obtenerGeneratriz()
        self.__area = obtenerArea()
        self.__volumen = obtenerVolumen()
        result = tuple(self.generatriz, self.area, self.volumen)
        return result


"""
***************************************************************
@@ ejercicio 5 @@
CentroMedico
Paciente
    nombre
    lugar
    descripcion
    costo
    conDescuento
    descuento
"""


class CentroMedico(Paciente):
    def _init_(self):
        self.__listaPacientes = []

    def registrar(self, nombre, lugar, descripcion, costo, conDescuento, descuento):
        actual = Paciente(nombre, lugar, descripcion, costo, conDescuento, descuento)
        self.__listaPacientes.append(actual)

    def totalCostoSanSalvador(self):
        costoSS = 0
        for paciente in self.__listaPacientes:
            if paciente.lugar == "San Salvador":
                costoSS += Paciente.getCosto()
        return costoSS

    def totalCostoConDescuento(self):
        costoConDescuento = 0
        for paciente in self.__listaPacientes:
            if paciente.ConDescuento is True:
                costoConDescuento = Paciente.getCosto() - Paciente.getDescuento()
        return costoConDescuento


class Paciente:
    def _init_registrarPaciente(
        self, nombre, lugar, descripcion, costo, conDescuento, descuento
    ):
        self.__nombre = nombre
        self.__lugar = lugar
        self.__descripcion = descripcion
        self.__costo = costo
        self.__conDescuento = conDescuento
        self.__descuento = descuento

    def getconDescuento(self):
        return self.__conDescuento

    def getCosto(self):
        return self.costo

    def getDescuento(self):
        return self.descuento


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return "https://github.com/TatiBarah/Entrega-parcial"
