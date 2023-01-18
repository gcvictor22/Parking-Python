from Services.MainService import MainService
from Services.ParkingService import ParkingService
from Services.AbonadosService import AbonadosService
from Services.AdministradorService import AdministradorService
from Services.PickleService import PickleService
from threading import Thread
import time

parking_service = ParkingService()
abonados_service = AbonadosService()
admin_service = AdministradorService()
main_service = MainService()
pickle_service = PickleService()

lista_abonados = pickle_service.cargar_lista_abonados()
lista_clientes = pickle_service.cargar_lista_clientes()
estado_plazas = pickle_service.cargar_estado_plazas()
recaudacion_abonados = pickle_service.cargar_recaudacion_abonados()
recaudacion = pickle_service.cargar_recaudacion()
parking = pickle_service.cargar_parking()


# lista_abonados = main_service.lista_abonados
# lista_clientes = main_service.lista_clientes
# estado_plazas = main_service.estado_plazas
# recaudacion_abonados = main_service.recaudacion_abonos
# recaudacion = main_service.recaudacion
# parking = main_service.parking


def actualizado_automatico():
    on = True
    while on:
        i = 0
        while i < 300:
            if main_thread.is_alive():
                time.sleep(1)
                i += 1
            else:
                i = 300
                on = False
        open("Ficheros/estado_plazas.pckl", "w").close()
        open("Ficheros/listado_abonados.pckl", "w").close()
        open("Ficheros/listado_clientes.pckl", "w").close()
        open("Ficheros/parking.pckl", "w").close()
        open("Ficheros/recaudacion_abonados.pckl", "w").close()
        open("Ficheros/recaudacion.pckl", "w").close()

        pickle_service.actualizar_lista_abonados(lista_abonados)
        pickle_service.actualizar_lista_clientes(lista_clientes)
        pickle_service.actualizar_estado_plazas(estado_plazas)
        pickle_service.actualizar_recaudacion_abonados(recaudacion_abonados)
        pickle_service.actualizar_recaudacion(recaudacion)
        pickle_service.actualizar_parking(parking)
        print("\nActualizando sistema...")


def main_de_verdad():
    opcion = 9
    while opcion != 0:

        opcion = int(input("\n¿Donde quieres acceder?"
                           "\n0. Salir"
                           "\n1. Zona cliente"
                           "\n2. Zona administrador"
                           "\nOpcion: "))

        if opcion == 0:
            pickle_service.actualizar_lista_abonados(lista_abonados)
            pickle_service.actualizar_lista_clientes(lista_clientes)
            pickle_service.actualizar_estado_plazas(estado_plazas)
            pickle_service.actualizar_recaudacion_abonados(recaudacion_abonados)
            pickle_service.actualizar_recaudacion(recaudacion)
            pickle_service.actualizar_parking(parking)
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
                parking_service.mostrar_plazas(parking=parking)
                parking_service.depositar_vehiculo(parking=parking, f_estado_plazas=estado_plazas,
                                                   f_lista_clientes=lista_clientes)
            elif opcion_cliente == 2:
                parking_service.retirar_vehiculo(parking=parking, f_lista_clientes=lista_clientes,
                                                 f_estado_plazas=estado_plazas, f_recaudacion=recaudacion)
            elif opcion_cliente == 3:
                parking_service.mostrar_plazas(parking=parking)
                parking_service.depositar_vehiculo_abonado(f_estado_plazas=estado_plazas,
                                                           f_lista_clientes=lista_clientes,
                                                           f_lista_abonados=lista_abonados)
            elif opcion_cliente == 4:
                parking_service.retirar_vehiculo_abonado(f_estado_plazas=estado_plazas, f_lista_clientes=lista_clientes)
            else:
                print("Opción incorrecta")

        elif opcion == 2:
            opcion_admin = int(input("¿Qué deseas hacer?"
                                     "\n0. Salir"
                                     "\n1. Ver estado del parking"
                                     "\n2. Facturación"
                                     "\n3. Consulta de abonados"
                                     "\n4. Gestión abonados"
                                     "\n5. Caducidad abonos"
                                     "\nOpcion: "))

            if opcion_admin == 0:
                pass
            elif opcion_admin == 1:
                admin_service.mostrar_estado_parking(f_estado_plazas=estado_plazas)
            elif opcion_admin == 2:
                admin_service.calcular_recaudacion_entre_horas(f_recaudacion=recaudacion)
            elif opcion_admin == 3:
                admin_service.consultar_abonados(f_lista_abonados=lista_abonados,
                                                 f_recaudacion_abonados=recaudacion_abonados)
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
                    abonados_service.crear_abonado(f_estado_plazas=estado_plazas, f_lista_abonados=lista_abonados,
                                                   f_recaudacion_abonados=recaudacion_abonados, parking=parking)
                elif opcion_abono == 2:
                    abonados_service.modificar_informacion_personal_abonado(f_lista_abonados=lista_abonados)
                elif opcion_abono == 3:
                    abonados_service.modificar_abono(f_lista_abonados=lista_abonados,
                                                     f_recaudacion_abonados=recaudacion_abonados)
                elif opcion_abono == 4:
                    abonados_service.baja_abonado(f_estado_plazas=estado_plazas, f_listado_abonados=lista_abonados)
                else:
                    print("Opción incorrecta")

            elif opcion_admin == 5:
                abonados_service.caducidad_abonos(f_listado_abonados=lista_abonados)
            else:
                print("Opción incorrecta")


main_thread = Thread(target=main_de_verdad)
actualizado_thread = Thread(target=actualizado_automatico)

main_thread.start()
actualizado_thread.start()
