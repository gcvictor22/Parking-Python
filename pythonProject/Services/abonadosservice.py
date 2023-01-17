from Models.Abonado import Abonado
from Models.Vehiculo import Vehiculo
from datetime import datetime
from datetime import timedelta


class AbonadosService:

    def crear_abonado(self, parking):
        print("Datos personales\n"
              "----------------")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        gmail = input("Gmail: ")
        dni = input("DNI: ")
        tajeta = input("Tarjeta de pago: ")

        print("Abono\n"
              "-----")
        tipo_a = int(input("¿Qué tipo de abono quieres contratar?"
                           "\n1. Mensual 25€"
                           "\n2. Trimestrar 70€"
                           "\n3. Semestral 130€"
                           "\n4. Anual 200€"
                           "\nOpcion: "))
        if tipo_a == 1:
            tipo_abono = "mensual"
        elif tipo_a == 2:
            tipo_abono = "trimestral"
        elif tipo_a == 3:
            tipo_abono = "semestral"
        else:
            tipo_abono = "anual"

        print("Vehiculo\n"
              "--------")
        matricula = input("Matrícula del vehiculo: ")
        print('¿Qué tipo de vehiculo es?'
              '\n1. Turismo'
              '\n2. Moto'
              '\n3. Minusvalido')

        tipo_v = int(input('\nOpcion: '))
        if tipo_v == 1 and parking.plazas_turismo > 0:
            nuevo_vehiculo = Vehiculo(matricula, 'Turismo')
            parking.plazas_turismo -= 1
        elif tipo_v == 2 and parking.plazas_motos > 0:
            nuevo_vehiculo = Vehiculo(matricula, 'Moto')
            parking.plazas_motos -= 1
        elif tipo_v == 3 and parking.plazas_minusvalidos > 0:
            nuevo_vehiculo = Vehiculo(matricula, 'Minusvalido')
            parking.plazas_minusvalidos -= 1

        parking.plazas_totales -= 1

        for i in range(1, 61):
            plaza = parking.estado_plazas[i]
            if plaza == "Libre":
                print("Plaza " + str(i) + ": Libre    ", end='')
                if i % 5 == 0:
                    print('\n')

        plaza_parking = int(input("\n\nPara terminar, elije una de las siguientes plazas: "))

        parking.estado_plazas[plaza_parking] = "Reservada libre"

        fecha_activacion_abono = datetime.now()
        fecha_caducidad_abono = datetime.now() + timedelta(days=30)
        nuevo_abonado = Abonado(nombre=nombre, apellidos=apellidos, gmail=gmail, dni=dni, tarjeta=tajeta,
                                tipo_abono=tipo_abono, vehiculo=nuevo_vehiculo, plaza_parking=plaza_parking,
                                fecha_activacion_abono=fecha_activacion_abono,
                                fecha_caducidad_abono=fecha_caducidad_abono, fecha_deposito='', pin=0)

        parking.lista_abonados.append(nuevo_abonado)
