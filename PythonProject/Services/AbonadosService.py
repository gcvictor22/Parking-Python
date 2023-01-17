import random

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
            fecha_caducidad_abono = datetime.now() + timedelta(days=30)
            parking.recaudacion_abonos[tajeta] = 25
        elif tipo_a == 2:
            tipo_abono = "trimestral"
            fecha_caducidad_abono = datetime.now() + timedelta(days=90)
            parking.recaudacion_abonos[tajeta] = 70
        elif tipo_a == 3:
            tipo_abono = "semestral"
            fecha_caducidad_abono = datetime.now() + timedelta(days=183)
            parking.recaudacion_abonos[tajeta] = 130
        else:
            tipo_abono = "anual"
            fecha_caducidad_abono = datetime.now() + timedelta(days=365)
            parking.recaudacion_abonos[tajeta] = 200

        print("Vehiculo\n"
              "--------")
        matricula = input("Matrícula del vehiculo: ")
        print('¿Qué tipo de vehiculo es?'
              '\n1. Turismo'
              '\n2. Moto'
              '\n3. Movilidad reducida')

        tipo_v = int(input('\nOpcion: '))
        if tipo_v == 1 and parking.plazas_turismo > 0:
            nuevo_vehiculo = Vehiculo(matricula, 'Turismo')
            parking.plazas_turismo -= 1
        elif tipo_v == 2 and parking.plazas_motos > 0:
            nuevo_vehiculo = Vehiculo(matricula, 'Moto')
            parking.plazas_motos -= 1
        elif tipo_v == 3 and parking.plazas_minusvalidos > 0:
            nuevo_vehiculo = Vehiculo(matricula, 'Movilidad reducida')
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
        pin = random.randint(100000, 999999)

        fecha_activacion_abono = datetime.now()
        nuevo_abonado = Abonado(nombre=nombre, apellidos=apellidos, gmail=gmail, dni=dni, tarjeta=tajeta,
                                tipo_abono=tipo_abono, vehiculo=nuevo_vehiculo, plaza_parking=plaza_parking,
                                fecha_activacion_abono=fecha_activacion_abono,
                                fecha_caducidad_abono=fecha_caducidad_abono, fecha_deposito='', pin=pin)

        parking.lista_abonados.append(nuevo_abonado)

    def modificar_informacion_personal_abonado(self, parking):

        dni = input("Introduce tu DNI: ")

        abonados = parking.lista_abonados
        existe = False
        for abonado in abonados:
            if abonado.dni == dni:
                edit_abonado = abonado
                existe = True

        if not existe:
            print("No se ha encontrado ningún usuario con DNI: "+dni)
        else:
            opcion_editar = int(input("\n¿Qué deseas editar?"
                                      "\n1. Nombre y apellidos"
                                      "\n2. Gmail"
                                      "\n3. Tarjeta de crédito"
                                      "\n4. Todo lo anterior"
                                      "\nOpcion: "))

            if opcion_editar == 1:
                edit_abonado.nombre = input("Escribe el nuevo nombre: ")
                edit_abonado.apellidos = input("Escribe los nuevos apellidos: ")
            elif opcion_editar == 2:
                edit_abonado.gmail = input("Escribe el nuevo gmail: ")
            elif opcion_editar == 3:
                edit_abonado.tarjeta = input("Introduce el número de tarjeta: ")
            elif opcion_editar == 4:
                edit_abonado.nombre = input("Escribe el nuevo nombre: ")
                edit_abonado.apellidos = input("Escribe los nuevos apellidos: ")
                edit_abonado.gmail = input("Escribe el nuevo gmail: ")
                edit_abonado.tarjeta = input("Introduce el número de tarjeta: ")
            else:
                print("Opción incorrecta")

    def modificar_abono(self, parking):

        dni = input("Introduce tu DNI: ")

        abonados = parking.lista_abonados
        existe = False
        for abonado in abonados:
            if abonado.dni == dni:
                edit_abonado = abonado
                existe = True

        if not existe:
            print("No se ha encontrado ningún usuario con DNI: " + dni)
        else:
            opcion_abono = int(input("Elije un tipo de abono para renovar: "
                                     "\n1. Mensual - 25€"
                                     "\n2. Trimestral - 70€"
                                     "\n3. Semestral - 130€"
                                     "\n4. Anual - 200€"
                                     "\nOpcion: "))
            if opcion_abono == 1:
                edit_abonado.tipo_abono = 'mensual'
                edit_abonado.fecha_caducidad_abono = datetime.now() + timedelta(days=30)
                edit_abonado.fecha_activacion_abono = datetime.now()
                parking.recaudacion_abonos[edit_abonado.tarjeta] = parking.recaudacion_abonos[edit_abonado.tarjeta] + 25
            elif opcion_abono == 2:
                edit_abonado.tipo_abono = 'trimestral'
                edit_abonado.fecha_caducidad_abono = datetime.now() + timedelta(days=90)
                edit_abonado.fecha_activacion_abono = datetime.now()
                parking.recaudacion_abonos[edit_abonado.tarjeta] = parking.recaudacion_abonos[edit_abonado.tarjeta] + 70
            elif opcion_abono == 3:
                edit_abonado.tipo_abono = 'semestral'
                edit_abonado.fecha_caducidad_abono = datetime.now() + timedelta(days=183)
                edit_abonado.fecha_activacion_abono = datetime.now()
                parking.recaudacion_abonos[edit_abonado.tarjeta] = parking.recaudacion_abonos[edit_abonado.tarjeta] + 130
            if opcion_abono == 4:
                edit_abonado.tipo_abono = 'anual'
                edit_abonado.fecha_caducidad_abono = datetime.now() + timedelta(days=365)
                edit_abonado.fecha_activacion_abono = datetime.now()
                parking.recaudacion_abonos[edit_abonado.tarjeta] = parking.recaudacion_abonos[edit_abonado.tarjeta] + 200

    def baja_abonado(self, parking):

        dni = input("Introduce tu DNI: ")

        abonados = parking.lista_abonados
        existe = False
        for abonado in abonados:
            if abonado.dni == dni:
                elim_abonado = abonado
                existe = True

        if not existe:
            print("No se ha encontrado ningún usuario con DNI: " + dni)
        else:
            parking.lista_abonados.remove(elim_abonado)

    def caducidad_abonos(self, parking):

        opcion = int(input("¿Qué deseas comprobar: "
                                 "\n1. Comprobar abonos que caducan un mes"
                                 "\n2. Comprobar abonos que caducan dentro de 10 días"
                                 "\nOpcion: "))

        if opcion == 1:
            anho = int(input("Introduce un año: "))
            mes = int(input("Introduce un mes: "))

            mes_comprobar = datetime(year=anho, month=mes, day=1)
            mes_fin = mes_comprobar + timedelta(days=30)

            for abonado in parking.lista_abonados:
                if mes_comprobar < abonado.fecha_caducidad_abono < mes_fin:
                    resto = abonado.fecha_caducidad_abono - datetime.now()
                    print("El abono del usuario con Gmail: "+abonado.gmail+" caduca este mes.")
                    print("El abono caduca dentro de: "+str(resto[0]))

        elif opcion == 2:

            fecha_final = datetime.now() + timedelta(days=30)
            for abonado in parking.lista_abonados:
                if datetime.now() < abonado.fecha_caducidad_abono < fecha_final:
                    resto = abonado.fecha_caducidad_abono - datetime.now()
                    print("El abono del usuario con Gmail: "+abonado.gmail+" caduca este en menos de 10 días.")
                    print("El abono caduca dentro de: "+str(resto[0]))

        else:
            print("Opcion incorrecta")