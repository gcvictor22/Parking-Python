class Vehiculo:

    def __init__(self, matricula, tipo):
        self.__matricula = matricula
        self.__tipo = tipo

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, m):
        self.__matricula = m

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, t):
        self.__tipo = t
