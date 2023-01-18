from datetime import datetime
from datetime import timedelta
import pickle

from Models.Abonado import Abonado
from Models.Cliente import Cliente
from Models.Parking import Parking
from Models.Vehiculo import Vehiculo
from Services.ParkingService import ParkingService
from Services.AbonadosService import AbonadosService
from Services.AdministradorService import AdministradorService

opcion = int
parking_service = ParkingService()
abonados_service = AbonadosService()
admin_service = AdministradorService()
parking = Parking(plazas_totales=60, plazas_turismo=42, plazas_motos=9, plazas_minusvalidos=9)

for i in range(1, 61):
    parking.estado_plazas[i] = "Libre"

v1 = Vehiculo(matricula='1234 AAA', tipo='Moto')
fecha_activacion_bono1 = datetime(year=2022, month=10, day=7, hour=12, minute=36, second=51)
fecha_caducidad_abono1 = fecha_activacion_bono1 + timedelta(days=183)
ab1 = Abonado(nombre='John', apellidos='Doe', gmail='johndoe@gmail.com', dni='12345678-A',
              tarjeta='1234 5678 9123 4567',
              tipo_abono='semestral', vehiculo=v1, plaza_parking=42,
              fecha_activacion_abono=fecha_activacion_bono1,
              fecha_caducidad_abono=fecha_caducidad_abono1, fecha_deposito='', pin=478392)
parking.estado_plazas[ab1.plaza_parking] = "Reservada libre"
parking.recaudacion_abonos[ab1.tarjeta] = 130
parking.plazas_motos -= 1
parking.plazas_totales -= 1
parking.lista_abonados.append(ab1)

v2 = Vehiculo(matricula='5678 BBB', tipo='Turismo')
fecha_activacion_bono2 = datetime(year=2023, month=1, day=10, hour=8, minute=47, second=23)
fecha_caducidad_abono2 = fecha_activacion_bono1 + timedelta(days=90)
ab2 = Abonado(nombre='Eladio', apellidos='Carrion', gmail='hugoboss@gmail.com', dni='87654321-Z',
              tarjeta='1111 2222 3333 4444',
              tipo_abono='trimestral', vehiculo=v2, plaza_parking=24,
              fecha_activacion_abono=fecha_activacion_bono2,
              fecha_caducidad_abono=fecha_caducidad_abono2, fecha_deposito='', pin=279053)
parking.estado_plazas[ab2.plaza_parking] = "Reservada libre"
parking.recaudacion_abonos[ab2.tarjeta] = 70
parking.plazas_turismo -= 1
parking.plazas_totales -= 1
parking.lista_abonados.append(ab2)

v3 = Vehiculo(matricula='1601 HTT', tipo='Moto')
c1 = Cliente(fecha_deposito=datetime(year=2021, month=4, day=22, hour=9, minute=21, second=36), plaza_parking=22,
             vehiculo=v3, pin=928492)
parking.estado_plazas[c1.plaza_parking] = "Ocupada"
parking.plazas_motos -= 1
parking.plazas_totales -= 1
parking.lista_clientes.append(c1)

v4 = Vehiculo(matricula='8888 SPT', tipo='Movilidad reducida')
c2 = Cliente(fecha_deposito=datetime(year=2023, month=1, day=17, hour=23, minute=12, second=21), plaza_parking=4,
             vehiculo=v4, pin=498023)
parking.estado_plazas[c2.plaza_parking] = "Ocupada"
parking.plazas_minusvalidos -= 1
parking.plazas_totales -= 1
parking.lista_clientes.append(c2)

v5 = Vehiculo(matricula='1818 KMZ', tipo='Turismo')
c3 = Cliente(fecha_deposito=datetime(year=2023, month=1, day=17, hour=23, minute=12, second=21), plaza_parking=4,
             vehiculo=v5, pin=917034)
parking.estado_plazas[c3.plaza_parking] = "Ocupada"
parking.plazas_turismo -= 1
parking.plazas_totales -= 1
parking.lista_clientes.append(c3)

v6 = Vehiculo(matricula='8342 VPN', tipo='Movilidad reducida')
c4 = Cliente(fecha_deposito=datetime(year=2022, month=12, day=30, hour=14, minute=56, second=2), plaza_parking=1,
             vehiculo=v6, pin=724943)
parking.estado_plazas[c4.plaza_parking] = "Ocupada"
parking.plazas_minusvalidos -= 1
parking.plazas_totales -= 1
parking.lista_clientes.append(c4)

fichero_abonados = open('./Ficheros/listado_abonados', 'wb')
pickle.dump(parking.lista_abonados, fichero_abonados)
fichero_abonados.close()

fichero_clientes = open('./Ficheros/listado_clientes', 'wb')
pickle.dump(parking.lista_clientes, fichero_clientes)
fichero_clientes.close()

while opcion != 0:

    opcion = int(input("\n¿Donde quieres acceder?"
                       "\n0. Salir"
                       "\n1. Zona cliente"
                       "\n2. Zona administrador"
                       "\nOpcion: "))

    if opcion == 0:
        pass
    if opcion == 1:
        opcion_cliente = int(input("¿Qué deseas hacer?"
                                   "\n0. Salir"
                                   "\n1. Depositar vehículo"
                                   "\n2. Retirar vehículo"
                                   "\n3. Depositar vehículo (abonado)"
                                   "\n4. Retirar vehículo (abonado)"
                                   "\nOpcion: "))

        if opcion_cliente == 0:
            pass
        elif opcion_cliente == 1:
            parking_service.mostrar_plazas(parking)
            parking_service.depositar_vehiculo(parking)
        elif opcion_cliente == 2:
            parking_service.retirar_vehiculo(parking)
        elif opcion_cliente == 3:
            parking_service.mostrar_plazas(parking)
            parking_service.depositar_vehiculo_abonado(parking)
        elif opcion_cliente == 4:
            parking_service.retirar_vehiculo_abonado(parking)
        else:
            print("Opción incorrecta")

    elif opcion == 2:
        opcion_admin = int(input("¿Qué deseas hacer?"
                                 "\n0. Salir"
                                 "\n1. Ver estado del parking"
                                 "\n2. Facturación"
                                 "\n3. Consulta de abonados"
                                 "\n4. Gestión abonos"
                                 "\n5. Caducidad abonos"
                                 "\nOpcion: "))

        if opcion_admin == 0:
            pass
        elif opcion_admin == 1:
            admin_service.mostrar_estado_parking(parking)
        elif opcion_admin == 2:
            admin_service.calcular_recaudacion_entre_horas(parking)
        elif opcion_admin == 3:
            admin_service.consultar_abonados(parking)
        elif opcion_admin == 4:

            opcion_abono = int(input("¿Qué deseas hacer?"
                                     "\n0. Salir"
                                     "\n1. Darme de alta como abonado"
                                     "\n2. Modificar información personal"
                                     "\n3. Renovar abono"
                                     "\n4. Darme de baja"
                                     "\nOpcion: "))

            if opcion_abono == 0:
                pass
            elif opcion_abono == 1:
                abonados_service.crear_abonado(parking)
            elif opcion_abono == 2:
                abonados_service.modificar_informacion_personal_abonado(parking)
            elif opcion_abono == 3:
                abonados_service.modificar_abono(parking)
            elif opcion_abono == 4:
                abonados_service.baja_abonado(parking)
            else:
                print("Opción incorrecta")

        elif opcion_admin == 5:
            abonados_service.caducidad_abonos(parking)
        else:
            print("Opción incorrecta")

    else:
        f = open('./Ficheros/listado_abonados', 'rb')
        abonados = pickle.load(f)
        f.close()

        for a in abonados:
            print(a)
