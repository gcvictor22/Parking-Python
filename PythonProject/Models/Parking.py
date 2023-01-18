class Parking:

    def __init__(self, plazas_totales, plazas_turismo, plazas_motos, plazas_minusvalidos):
        self.__plazas_turismo = plazas_turismo
        self.__plazas_motos = plazas_motos
        self.__plazas_minusvalidos = plazas_minusvalidos
        self.__plazas_totales = plazas_totales

    @property
    def plazas_totales(self):
        return self.__plazas_totales

    @plazas_totales.setter
    def plazas_totales(self, p):
        self.__plazas_totales = p

    @property
    def plazas_turismo(self):
        return self.__plazas_turismo

    @plazas_turismo.setter
    def plazas_turismo(self, p):
        self.__plazas_turismo = p

    @property
    def plazas_motos(self):
        return self.__plazas_motos

    @plazas_motos.setter
    def plazas_motos(self, p):
        self.__plazas_motos = p

    @property
    def plazas_minusvalidos(self):
        return self.__plazas_minusvalidos

    @plazas_minusvalidos.setter
    def plazas_minusvalidos(self, p):
        self.__plazas_minusvalidos = p
