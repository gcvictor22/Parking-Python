from Models.Cliente import Cliente


class Abonado(Cliente):

    def __init__(self, nombre, apellidos, gmail, dni, tarjeta, tipo_abono, fecha_activacion_abono,
                 fecha_caducidad_abono, plaza_parking, vehiculo, fecha_deposito, pin):
        super().__init__(plaza_parking, vehiculo, fecha_deposito, pin)
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__gmail = gmail
        self.__dni = dni
        self.__tarjeta = tarjeta
        self.__tipo_abono = tipo_abono
        self.__fecha_activacion_abono = fecha_activacion_abono
        self.__fecha_caducidad_abono = fecha_caducidad_abono

    def __str__(self):
        return "Nombre: "+self.__nombre+"; Apellidos: "+self.__apellidos+"; Gmail: "+self.__gmail+";\n"\
            "Tipo de abono: "+self.__tipo_abono+"; Matricula vehículo: "+self.vehiculo.matricula+"; Plaza parking: "+str(self.plaza_parking)+";\n"


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, n):
        self.__nombre = n

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, n):
        self.__apellidos = n

    @property
    def gmail(self):
        return self.__gmail

    @gmail.setter
    def gmail(self, n):
        self.__gmail = n

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, n):
        self.__dni = n

    @property
    def tarjeta(self):
        return self.__tarjeta

    @tarjeta.setter
    def tarjeta(self, n):
        self.__tarjeta = n

    @property
    def tipo_abono(self):
        return self.__tipo_abono

    @tipo_abono.setter
    def tipo_abono(self, n):
        self.__tipo_abono = n

    @property
    def fecha_activacion_abono(self):
        return self.__fecha_activacion_abono

    @fecha_activacion_abono.setter
    def fecha_activacion_abono(self, n):
        self.__fecha_activacion_abono = n

    @property
    def fecha_caducidad_abono(self):
        return self.__fecha_caducidad_abono

    @fecha_caducidad_abono.setter
    def fecha_caducidad_abono(self, n):
        self.__fecha_caducidad_abono = n

