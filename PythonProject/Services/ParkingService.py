import random
import datetime

from Models.Cliente import Cliente
from Models.Vehiculo import Vehiculo
from Models.Ticket import Ticket


class ParkingService:

    def mostrar_plazas(self, parking):

        print('El total del plazas disponibles es: ', parking.plazas_totales)
        print('Plazas turismos -> ', parking.plazas_turismo)
        print('Plazas motos -> ', parking.plazas_motos)
        print('Plazas movilidad reducida -> ', parking.plazas_minusvalidos)

    def depositar_vehiculo(self, parking, f_estado_plazas, f_lista_clientes):

        if parking.plazas_totales > 0:
            matricula = input('Introduce la matrícula del vehiculo: ')
            nuevo_vehiculo = any

            print('¿Qué tipo de vehiculo es?'
                  '\n1. Turismo'
                  '\n2. Moto'
                  '\n3. Movilidad reducidad')

            tipo = int(input('Opcion: '))
            if tipo == 1 and parking.plazas_turismo > 0:
                nuevo_vehiculo = Vehiculo(matricula, 'Turismo')
                parking.plazas_turismo -= 1
            elif tipo == 2 and parking.plazas_motos > 0:
                nuevo_vehiculo = Vehiculo(matricula, 'Moto')
                parking.plazas_motos -= 1
            elif tipo == 3 and parking.plazas_minusvalidos > 0:
                nuevo_vehiculo = Vehiculo(matricula, 'Movilidad reducidad')
                parking.plazas_minusvalidos -= 1

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
            ticket.__str__()

    def depositar_vehiculo_abonado(self, f_lista_abonados, f_estado_plazas, f_lista_clientes):

        matricula = input("Introducza la matrícula de su vehículo: ")
        dni = input("Introduzca su DNI: ")

        for abonado in f_lista_abonados:
            if abonado.vehiculo.matricula.upper() == matricula.upper() and abonado.dni == dni:
                if abonado.fecha_caducidad_abono > datetime.datetime.now():
                    f_estado_plazas[abonado.plaza_parking] = "Reservada Ocupada"
                    f_lista_clientes.append(abonado)
                    ticket = Ticket(abonado.vehiculo.matricula, datetime.datetime.now(), abonado.plaza_parking,
                                    abonado.pin)
                    ticket.__str__()
                else:
                    print("Tu abono ha caducado")
            else:
                print("No se ha encontrado ninguna ralación de un vehiculo con matrícula: " + matricula.upper() +
                      "y abonado con DNI: " + dni)

    def retirar_vehiculo(self, parking, f_lista_clientes, f_estado_plazas, f_recaudacion):

        matricula = input("Introduzca la matrícula de su vehículo: ")
        plaza_parking = int(input("Introduzca la plaza de garaje: "))
        pin = int(input("Por último, introduzca el pin que aparece en su ticket de depósito: "))

        for cliente in f_lista_clientes:
            if cliente.vehiculo.matricula == matricula and cliente.plaza_parking == plaza_parking and cliente.pin == pin:
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
                tiempo_estacionado = divmod((datetime.datetime.now() - cliente.fecha_deposito).total_seconds(), 60)[0]
                f_recaudacion[datetime.datetime.now()] = val * tiempo_estacionado
                f_lista_clientes.remove(cliente)
                print("\nVehículo retirado con éxito\n")

    def retirar_vehiculo_abonado(self, f_lista_clientes, f_estado_plazas):

        matricula = input("Introduzca la matrícula de su vehículo: ")
        plaza_parking = int(input("Introduzca la plaza de garaje: "))
        pin = int(input("Por último, introduzca el pin que aparece en su ticket de depósito: "))

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
