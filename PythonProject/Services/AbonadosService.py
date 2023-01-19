import random

from Models.Abonado import Abonado
from Models.Vehiculo import Vehiculo
from datetime import datetime
from datetime import timedelta


class AbonadosService:

    def crear_abonado(self, parking, f_lista_abonados, f_recaudacion_abonados, f_estado_plazas):

        for i in f_estado_plazas:
            plaza = f_estado_plazas[i]
            if plaza == "Libre":
                print("Plaza " + str(i) + ": Libre    ", end='')
            if i % 5 == 0:
                print('\n')

        try:
            plaza_parking = int(input("\n\n¿Qué plaza te gustaría reservar?: "))
            if plaza_parking < 1 and plaza_parking < 60:
                raise ValueError
            else:
                if f_estado_plazas[plaza_parking] == 'Libre':
                    print("Datos personales\n"
                          "----------------")
                    nombre = input("Nombre: ")
                    apellidos = input("Apellidos: ")
                    gmail = input("Gmail: ")
                    try:
                        dni = input("DNI: ")
                        if len(dni) != 10 or 65 <= ord(dni[8]) <= 90 or 97 <= ord(dni[8]) <= 122:
                            raise ValueError
                        else:
                            try:
                                tarjeta = int(input("Tarjeta de pago: "))
                                if len(tarjeta) != 16:
                                    raise ValueError
                                else:
                                    print("Abono\n"
                                          "-----")
                                    try:
                                        tipo_a = int(input("¿Qué tipo de abono quieres contratar?"
                                                           "\n1. Mensual 25€"
                                                           "\n2. Trimestrar 70€"
                                                           "\n3. Semestral 130€"
                                                           "\n4. Anual 200€"
                                                           "\nOpcion: "))
                                        if tipo_a != 1 and tipo_a != tipo_a != 2 and tipo_a != 3 and tipo_a != 4:
                                            raise ValueError
                                        else:
                                            if tipo_a == 1:
                                                tipo_abono = "mensual"
                                                fecha_caducidad_abono = datetime.now() + timedelta(days=30)
                                                f_recaudacion_abonados[tarjeta] = 25
                                            elif tipo_a == 2:
                                                tipo_abono = "trimestral"
                                                fecha_caducidad_abono = datetime.now() + timedelta(days=90)
                                                f_recaudacion_abonados[tarjeta] = 70
                                            elif tipo_a == 3:
                                                tipo_abono = "semestral"
                                                fecha_caducidad_abono = datetime.now() + timedelta(days=183)
                                                f_recaudacion_abonados[tarjeta] = 130
                                            else:
                                                tipo_abono = "anual"
                                                fecha_caducidad_abono = datetime.now() + timedelta(days=365)
                                                f_recaudacion_abonados[tarjeta] = 200

                                            print("Vehiculo\n"
                                                  "--------")
                                            matricula = input("Matrícula del vehiculo: ")
                                            print('¿Qué tipo de vehiculo es?'
                                                  '\n1. Turismo'
                                                  '\n2. Moto'
                                                  '\n3. Movilidad reducida')

                                            try:
                                                tipo_v = int(input('\nOpcion: '))
                                                if tipo_v != 1 and tipo_v != tipo_v != 2 and tipo_v != 3:
                                                    raise ValueError
                                                else:
                                                    if tipo_v == 1 and parking.plazas_turismo > 0:
                                                        nuevo_vehiculo = Vehiculo(matricula, 'Turismo')
                                                        parking.plazas_turismo -= 1
                                                        self.crear_abonado_comprobar_plazas(parking, f_estado_plazas,
                                                                                            nombre, apellidos, gmail,
                                                                                            dni, tarjeta, tipo_abono,
                                                                                            nuevo_vehiculo,
                                                                                            plaza_parking,
                                                                                            fecha_caducidad_abono,
                                                                                            f_lista_abonados)
                                                    elif tipo_v == 2 and parking.plazas_motos > 0:
                                                        nuevo_vehiculo = Vehiculo(matricula, 'Moto')
                                                        parking.plazas_motos -= 1
                                                        self.crear_abonado_comprobar_plazas(parking, f_estado_plazas,
                                                                                            nombre, apellidos, gmail,
                                                                                            dni, tarjeta, tipo_abono,
                                                                                            nuevo_vehiculo,
                                                                                            plaza_parking,
                                                                                            fecha_caducidad_abono,
                                                                                            f_lista_abonados)
                                                    elif tipo_v == 3 and parking.plazas_minusvalidos > 0:
                                                        nuevo_vehiculo = Vehiculo(matricula, 'Movilidad reducida')
                                                        parking.plazas_minusvalidos -= 1
                                                        self.crear_abonado_comprobar_plazas(parking, f_estado_plazas,
                                                                                            nombre, apellidos, gmail,
                                                                                            dni, tarjeta, tipo_abono,
                                                                                            nuevo_vehiculo,
                                                                                            plaza_parking,
                                                                                            fecha_caducidad_abono,
                                                                                            f_lista_abonados)
                                            except ValueError:
                                                print("Error. introduce 1, 2 o 3")
                                    except ValueError:
                                        print("Error. introduce 1, 2, 3 o 4")
                            except ValueError:
                                print("Error. La tarjeta de crédito debe tener 16 dígitos")
                    except ValueError:
                        print("Error. Formato de DNI incorrecto, debe de ser XXXXXXXXY (X -> numero, Y -> letra)")
                else:
                    print("Esta plaza no se puede reservar actualmente")
        except ValueError:
            print("Error. Nuestro parking tiene 60 plazas, escoge una de las plazas disponibles")

    def crear_abonado_comprobar_plazas(self, parking, f_estado_plazas, nombre, apellidos, gmail, dni, tarjeta,
                                       tipo_abono, nuevo_vehiculo, plaza_parking, fecha_caducidad_abono,
                                       f_lista_abonados):
        parking.plazas_totales -= 1

        f_estado_plazas[plaza_parking] = "Reservada libre"
        pin = random.randint(100000, 999999)

        fecha_activacion_abono = datetime.now()
        nuevo_abonado = Abonado(nombre=nombre, apellidos=apellidos, gmail=gmail, dni=dni,
                                tarjeta=tarjeta,
                                tipo_abono=tipo_abono, vehiculo=nuevo_vehiculo,
                                plaza_parking=plaza_parking,
                                fecha_activacion_abono=fecha_activacion_abono,
                                fecha_caducidad_abono=fecha_caducidad_abono,
                                fecha_deposito='', pin=pin)

        f_lista_abonados.append(nuevo_abonado)

    def modificar_informacion_personal_abonado(self, f_lista_abonados):

        dni = input("Introduce tu DNI: ")

        existe = False
        for abonado in f_lista_abonados:
            if abonado.dni == dni:
                edit_abonado = abonado
                existe = True
        if not existe:
            print("No se ha encontrado ningún usuario con DNI: " + dni)
        else:
            try:
                opcion_editar = int(input("\n¿Qué deseas editar?"
                                          "\n1. Nombre y apellidos"
                                          "\n2. Gmail"
                                          "\n3. Tarjeta de crédito"
                                          "\n4. Todo lo anterior"
                                          "\nOpcion: "))
                if opcion_editar != 1 and opcion_editar != opcion_editar != 2 and opcion_editar != 3 and opcion_editar != 4:
                    raise ValueError
                else:
                    if opcion_editar == 1:
                        edit_abonado.nombre = input("Escribe el nuevo nombre: ")
                    elif opcion_editar == 2:
                        edit_abonado.apellidos = input("Escribe los nuevos apellidos: ")
                    elif opcion_editar == 3:
                        edit_abonado.gmail = input("Escribe el nuevo gmail: ")
                    elif opcion_editar == 4:
                        edit_abonado.nombre = input("Escribe el nuevo nombre: ")
                        edit_abonado.apellidos = input("Escribe los nuevos apellidos: ")
                        edit_abonado.gmail = input("Escribe el nuevo gmail: ")
                    else:
                        print("Opción incorrecta")
            except ValueError:
                print("Error. introduce 1, 2, 3 o 4")

    def modificar_abono(self, f_lista_abonados, f_recaudacion_abonados):

        dni = input("Introduce tu DNI: ")

        existe = False
        for abonado in f_lista_abonados:
            if abonado.dni == dni:
                edit_abonado = abonado
                existe = True

        if not existe:
            print("No se ha encontrado ningún usuario con DNI: " + dni)
        else:
            try:
                opcion_abono = int(input("Elije un tipo de abono para renovar: "
                                         "\n1. Mensual - 25€"
                                         "\n2. Trimestral - 70€"
                                         "\n3. Semestral - 130€"
                                         "\n4. Anual - 200€"
                                         "\nOpcion: "))
                if opcion_abono != 1 and opcion_abono != opcion_abono != 2 and opcion_abono != 3 and opcion_abono != 4:
                    raise ValueError
                else:
                    if opcion_abono == 1:
                        edit_abonado.tipo_abono = 'mensual'
                        edit_abonado.fecha_caducidad_abono = datetime.now() + timedelta(days=30)
                        edit_abonado.fecha_activacion_abono = datetime.now()
                        f_recaudacion_abonados[edit_abonado.tarjeta] = f_recaudacion_abonados[
                                                                           edit_abonado.tarjeta] + 25
                    elif opcion_abono == 2:
                        edit_abonado.tipo_abono = 'trimestral'
                        edit_abonado.fecha_caducidad_abono = datetime.now() + timedelta(days=90)
                        edit_abonado.fecha_activacion_abono = datetime.now()
                        f_recaudacion_abonados[edit_abonado.tarjeta] = f_recaudacion_abonados[
                                                                           edit_abonado.tarjeta] + 70
                    elif opcion_abono == 3:
                        edit_abonado.tipo_abono = 'semestral'
                        edit_abonado.fecha_caducidad_abono = datetime.now() + timedelta(days=183)
                        edit_abonado.fecha_activacion_abono = datetime.now()
                        f_recaudacion_abonados[edit_abonado.tarjeta] = f_recaudacion_abonados[
                                                                           edit_abonado.tarjeta] + 130
                    if opcion_abono == 4:
                        edit_abonado.tipo_abono = 'anual'
                        edit_abonado.fecha_caducidad_abono = datetime.now() + timedelta(days=365)
                        edit_abonado.fecha_activacion_abono = datetime.now()
                        f_recaudacion_abonados[edit_abonado.tarjeta] = f_recaudacion_abonados[
                                                                           edit_abonado.tarjeta] + 200
            except ValueError:
                print("Error. introduce 1, 2, 3 o 4")

    def baja_abonado(self, f_listado_abonados, f_estado_plazas):

        dni = input("Introduce tu DNI: ")

        existe = False
        for abonado in f_listado_abonados:
            if abonado.dni == dni:
                elim_abonado = abonado
                existe = True

        if not existe:
            print("No se ha encontrado ningún usuario con DNI: " + dni)
        else:
            f_listado_abonados.remove(elim_abonado)
            f_estado_plazas[elim_abonado.plaza_parking] = 'Libre'

    def caducidad_abonos(self, f_listado_abonados):

        try:
            opcion = int(input("¿Qué deseas comprobar: "
                               "\n1. Comprobar abonos que caducan un mes"
                               "\n2. Comprobar abonos que caducan dentro de 10 días"
                               "\nOpcion: "))
            if opcion != 1 and opcion != 2:
                raise ValueError
            else:
                if opcion == 1:
                    try:
                        anho = int(input("Introduce un año: "))
                        mes = int(input("Introduce un mes: "))
                        if 0 >= mes >= 12:
                            raise ValueError
                        else:
                            mes_comprobar = datetime(year=anho, month=mes, day=1)
                            mes_fin = mes_comprobar + timedelta(days=30)

                            for abonado in f_listado_abonados:
                                if mes_comprobar < abonado.fecha_caducidad_abono < mes_fin:
                                    resto = abonado.fecha_caducidad_abono - datetime.now()
                                    print("El abono del usuario con Gmail: " + abonado.gmail + " caduca ese mes.")
                                    print("El abono caduca dentro de: " + str(resto))
                                    print(
                                        "=============================================================================")
                    except ValueError:
                        print("Error. Introduce un mes correcto Enero -> 1 ... Diciembre -> 12")

                elif opcion == 2:

                    fecha_final = datetime.now() + timedelta(days=10)
                    for abonado in f_listado_abonados:
                        if datetime.now() < abonado.fecha_caducidad_abono < fecha_final:
                            resto = abonado.fecha_caducidad_abono - datetime.now()
                            print("El abono del usuario con Gmail: " + abonado.gmail + " caduca en menos de 10 días.")
                            print("El abono caduca dentro de: " + str(resto))
                            print("=============================================================================")
        except ValueError:
            print("Error. introduce 1 o 2")
