import datetime
from Models.Vehiculo import Vehiculo


class Ticket:

    def __init__(self, matricula, fecha_deposito, identificador, pin):
        self.__matricula = matricula
        self.__fecha_deposito = fecha_deposito
        self.__identificador = identificador
        self.__pin = pin

    def __str__(self):
        fe = self.__fecha_deposito

        return f"|{self.__pin:^30}|"


    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, m):
        self.__matricula = m

    @property
    def fecha_deposito(self):
        return self.__fecha_deposito

    @fecha_deposito.setter
    def fecha_deposito(self, f):
        self.__fecha_deposito = f

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, i):
        self.__identificador = i

    @property
    def pin(self):
        return self.__matricula

    @pin.setter
    def pin(self, p):
        self.__pin = p