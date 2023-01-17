class Cliente:

    def __init__(self, plaza_parking, vehiculo, fecha_deposito, pin):
        self.__plaza_parking = plaza_parking
        self.__vehiculo = vehiculo
        self.__fecha_deposito = fecha_deposito
        self.__pin = pin

    @property
    def plaza_parking(self):
        return self.__plaza_parking

    @plaza_parking.setter
    def plaza_parking(self, p):
        self.__plaza_parking = p

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, v):
        self.__vehiculo = v

    @property
    def fecha_deposito(self):
        return self.__fecha_deposito

    @fecha_deposito.setter
    def fecha_deposito(self, p):
        self.__fecha_deposito = p

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, v):
        self.__pin = v
