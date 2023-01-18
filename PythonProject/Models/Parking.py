class Parking:

    def __init__(self, plazas_totales, plazas_turismo, plazas_motos, plazas_minusvalidos, recaudacion={},
                 lista_clientes=[], estado_plazas={}, lista_abonados=[], recaudacion_abonos={}):
        self.__plazas_turismo = plazas_turismo
        self.__plazas_motos = plazas_motos
        self.__plazas_minusvalidos = plazas_minusvalidos
        self.__lista_clientes = lista_clientes
        self.__plazas_totales = plazas_totales
        self.__estado_plazas = estado_plazas
        self.__lista_abonados = lista_abonados
        self.__recaudacion = recaudacion
        self.__recaudacion_abonos = recaudacion_abonos

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

    @property
    def lista_clientes(self):
        return self.__lista_clientes

    @lista_clientes.setter
    def lista_clientes(self, p):
        self.__lista_clientes = p

    @property
    def estado_plazas(self):
        return self.__estado_plazas

    @estado_plazas.setter
    def estado_plazas(self, p):
        self.__estado_plazas = p

    @property
    def lista_abonados(self):
        return self.__lista_abonados

    @lista_abonados.setter
    def lista_abonados(self, p):
        self.__lista_abonados = p

    @property
    def recaudacion(self):
        return self.__recaudacion

    @recaudacion.setter
    def recaudacion(self, p):
        self.__recaudacion = p

    @property
    def recaudacion_abonos(self):
        return self.__recaudacion_abonos

    @recaudacion_abonos.setter
    def recaudacion_abonos(self, r):
        self.__recaudacion_abonos = r
