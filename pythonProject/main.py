from Models.Parking import Parking
from Services.parkingservice import ParkingService
from Services.abonadosservice import AbonadosService
from Services.administradorservice import AdministradorService

opcion = int
parking_service = ParkingService()
abonados_service = AbonadosService()
admin_service = AdministradorService()
parking = Parking(plazas_totales=60, plazas_turismo=42, plazas_motos=9, plazas_minusvalidos=9)

for i in range(1, 61):
    parking.estado_plazas[i] = "Libre"

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
                pass

        elif opcion_admin == 5:
            abonados_service.caducidad_abonos(parking)
        else:
            print("Opción incorrecta")
