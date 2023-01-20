import random
import datetime

from Models.Cliente import Cliente
from Models.Vehiculo import Vehiculo
from Models.Ticket import Ticket
from Views.ViewsPrint import ViewPrint

views = ViewPrint()


class ParkingService:

    def mostrar_plazas(self, parking):

        print('El total del plazas disponibles es: ', parking.plazas_totales)
        print('Plazas turismos -> ', parking.plazas_turismo)
        print('Plazas motos -> ', parking.plazas_motos)
        print('Plazas movilidad reducida -> ', parking.plazas_minusvalidos)

    def depositar_vehiculo(self, parking, f_estado_plazas, f_lista_clientes):

        if parking.plazas_totales > 0:
            matricula = input('Introduce la matrícula del vehiculo: ')

            it = 0
            existe = False
            while not existe and it < len(f_lista_clientes):
                if f_lista_clientes[it].vehiculo.matricula == matricula:
                    existe = True
                it += 1

            if not existe:
                try:
                    tipo = int(input(views.elegir_tipo_vehiculo()))
                    if tipo != 1 and tipo != 2 and tipo != 3:
                        raise ValueError
                    else:
                        if tipo == 1 and parking.plazas_turismo > 0:
                            nuevo_vehiculo = Vehiculo(matricula, 'Turismo')
                            parking.plazas_turismo -= 1
                            self.comprobar_plazas_depositar(parking=parking, f_estado_plazas=f_estado_plazas,
                                                            f_lista_clientes=f_lista_clientes,
                                                            nuevo_vehiculo=nuevo_vehiculo,
                                                            matricula=matricula)
                        elif tipo == 2 and parking.plazas_motos > 0:
                            nuevo_vehiculo = Vehiculo(matricula, 'Moto')
                            parking.plazas_motos -= 1
                            self.comprobar_plazas_depositar(parking=parking, f_estado_plazas=f_estado_plazas,
                                                            f_lista_clientes=f_lista_clientes,
                                                            nuevo_vehiculo=nuevo_vehiculo,
                                                            matricula=matricula)
                        elif tipo == 3 and parking.plazas_minusvalidos > 0:
                            nuevo_vehiculo = Vehiculo(matricula, 'Movilidad reducidad')
                            parking.plazas_minusvalidos -= 1
                            self.comprobar_plazas_depositar(parking=parking, f_estado_plazas=f_estado_plazas,
                                                            f_lista_clientes=f_lista_clientes,
                                                            nuevo_vehiculo=nuevo_vehiculo,
                                                            matricula=matricula)
                        else:
                            if tipo == 1:
                                print("Lo sentimos, actualmente no hay hueco para turismos en nuestro parking")
                            if tipo == 2:
                                print("Lo sentimos, actualmente no hay hueco para motos en nuestro parking")
                            if tipo == 3:
                                print("Lo sentimos, actualmente no hay hueco para vehiculos con movilidad reducida en "
                                      "nuestro parking")
                except ValueError:
                    print("⚠️ Error. introduce 1, 2 o 3 ⚠️")
            else:
                print("Ya hay un vehiculo que tiene la matrícula introducida")
        else:
            print("Lo sentimos, actualmente no hay hueco en el parking")

    def comprobar_plazas_depositar(self, parking, f_estado_plazas, f_lista_clientes, nuevo_vehiculo, matricula):
        parking.plazas_totales -= 1

        estado_plazas = f_estado_plazas
        it = 1
        salir = False
        while not salir:
            it += 1
            if estado_plazas[it] == "Libre":
                estado_plazas[it] = "Ocupada"
                plaza_asignada = it
                salir = True

        pin = random.randint(100000, 999999)
        cliente = Cliente(plaza_asignada, nuevo_vehiculo, datetime.datetime.now(), pin)
        f_lista_clientes.append(cliente)
        ticket = Ticket(matricula, datetime.datetime.now(), plaza_asignada, pin)
        print(ticket.__str__())

    def depositar_vehiculo_abonado(self, f_lista_abonados, f_estado_plazas, f_lista_clientes):

        matricula = input("Introducza la matrícula de su vehículo: ")
        dni = input("Introduzca su DNI: ")

        it = 0
        existe = False
        while not existe and it < len(f_lista_abonados):
            if f_lista_abonados[it].vehiculo.matricula.upper() == matricula.upper() and f_lista_abonados[it].dni.upper() == dni.upper():
                if f_lista_abonados[it].fecha_caducidad_abono > datetime.datetime.now():
                    f_estado_plazas[f_lista_abonados[it].plaza_parking] = "Reservada Ocupada"
                    f_lista_clientes.append(f_lista_abonados[it])
                    ticket = Ticket(f_lista_abonados[it].vehiculo.matricula, datetime.datetime.now(),
                                    f_lista_abonados[it].plaza_parking,
                                    f_lista_abonados[it].pin)
                    print(ticket.__str__())
                else:
                    print("Tu abono ha caducado")
                    pass
            it += 1

        if not existe:
            print("No se ha encontrado ninguna ralación de un vehiculo con matrícula: " + matricula.upper() +
                  " y abonado con DNI: " + dni.upper())

    def retirar_vehiculo(self, parking, f_lista_clientes, f_estado_plazas, f_recaudacion):

        matricula = input("Introduzca la matrícula de su vehículo: ")
        try:
            plaza_parking = int(input("Introduzca la plaza de garaje: "))
            if 1 > plaza_parking > 60:
                raise ValueError
            else:
                try:
                    pin = int(input("Por último, introduzca el pin que aparece en su ticket de depósito: "))
                    if 100000 > pin > 999999:
                        raise ValueError
                    else:
                        retirado = False
                        for cliente in f_lista_clientes:
                            if cliente.vehiculo.matricula.upper() == matricula.upper() and cliente.plaza_parking == plaza_parking and cliente.pin == pin:
                                f_estado_plazas[plaza_parking] = "Libre"
                                if cliente.vehiculo.tipo == "Turismo":
                                    val = 0.12
                                    parking.plazas_turismo += 1
                                elif cliente.vehiculo.tipo == "Moto":
                                    val = 0.08
                                    parking.plazas_motos += 1
                                else:
                                    val = 0.1
                                    parking.plazas_minusvalidos += 1
                                parking.plazas_totales += 1
                                tiempo_estacionado = \
                                    divmod((datetime.datetime.now() - cliente.fecha_deposito).total_seconds(), 60)[0]
                                f_recaudacion[datetime.datetime.now()] = val * tiempo_estacionado
                                f_lista_clientes.remove(cliente)
                                print("\nVehículo retirado con éxito. A pagar: "+str(val*tiempo_estacionado)+"€\n")
                                retirado = True
                        if not retirado:
                            print("No se ha podido asociar los datos introducidos a un vehículo")
                except ValueError:
                    print("⚠️ Error. Indroduzca un pin válido, de 6 dígitos ⚠️")
        except ValueError:
            print("⚠️ Error. No existe la plaza " + plaza_parking + " ⚠️")

    def retirar_vehiculo_abonado(self, f_lista_clientes, f_estado_plazas):

        matricula = input("Introduzca la matrícula de su vehículo: ")
        try:
            plaza_parking = int(input("Introduzca la plaza de garaje: "))
            if 1 > plaza_parking > 60:
                raise ValueError
            else:
                try:
                    pin = int(input("Por último, introduzca el pin que aparece en su ticket de depósito: "))
                    if 100000 > pin > 999999:
                        raise ValueError
                    else:
                        existe = False
                        for abonado in f_lista_clientes:
                            if abonado.vehiculo.matricula == matricula and abonado.plaza_parking == plaza_parking and abonado.pin == pin:
                                f_estado_plazas[plaza_parking] = "Reservada libre"
                                f_lista_clientes.remove(abonado)
                                print("Muchas gracias " + abonado.nombre + ", vehículo retirado con éxito")
                                existe = True
                                print("Gracias " + abonado.nombre + ", su vehículo ha sido retirado con éxito")

                        if not existe:
                            print("No se ha encontrado ningún vehículo con los datos introducidos")
                except ValueError:
                    print("⚠️ Error. Indroduzca un pin válido, de 6 dígitos ⚠️")
        except ValueError:
            print("⚠️ Error. No existe la plaza " + plaza_parking + " ⚠️")
