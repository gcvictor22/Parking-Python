import datetime
from Models.Vehiculo import Vehiculo


class Ticket:

    def __init__(self, matricula, fecha_deposito, identificador, pin):
        self.__matricula = matricula
        self.__fecha_deposito = fecha_deposito
        self.__identificador = identificador
        self.__pin = pin

    def __str__(self):
        f = self.__fecha_deposito

        return f" ________________________\n"\
            f"|  {'Fecha: ':<10}{'{}-{}-{}'.format(f.day, f.month, f.year):>10}  |\n" \
            f"|  {'Hora: ':<10}{'{}:{}:{}'.format(f.hour, f.minute, f.second):>10}  |\n" \
            f"|  {'-----------':^20}  |\n"\
            f"|  {'Plaza: ':<10}{'%02d' % self.__identificador:>10}  |\n"\
            f"|  {'Pin: ':<10}{self.__pin:>10}  |\n"\
            f"|________________________|"\

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