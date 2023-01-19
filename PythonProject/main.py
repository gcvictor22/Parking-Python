from datetime import datetime
from datetime import timedelta

from Services.MainService import MainService
from Services.ParkingService import ParkingService
from Services.AbonadosService import AbonadosService
from Services.AdministradorService import AdministradorService
from Services.PickleService import PickleService
from Views.ViewsPrint import ViewPrint
from threading import Thread
import time

parking_service = ParkingService()
abonados_service = AbonadosService()
admin_service = AdministradorService()
main_service = MainService()
pickle_service = PickleService()
views = ViewPrint()

# lista_abonados = pickle_service.cargar_lista_abonados()
# lista_clientes = pickle_service.cargar_lista_clientes()
# estado_plazas = pickle_service.cargar_estado_plazas()
# recaudacion_abonados = pickle_service.cargar_recaudacion_abonados()
# recaudacion = pickle_service.cargar_recaudacion()
# parking = pickle_service.cargar_parking()


lista_abonados = main_service.lista_abonados
lista_clientes = main_service.lista_clientes
estado_plazas = main_service.estado_plazas
recaudacion_abonados = main_service.recaudacion_abonos
recaudacion = main_service.recaudacion
parking = main_service.parking


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

        abonados_service.comprobar_baja_abonado(f_lista_abonados=lista_abonados, f_estado_plazas=estado_plazas)

        pickle_service.actualizar_lista_abonados(lista_abonados)
        pickle_service.actualizar_lista_clientes(lista_clientes)
        pickle_service.actualizar_estado_plazas(estado_plazas)
        pickle_service.actualizar_recaudacion_abonados(recaudacion_abonados)
        pickle_service.actualizar_recaudacion(recaudacion)
        pickle_service.actualizar_parking(parking)
        print("\nActualizando sistema...")


def main_de_verdad():
    abonados_service.comprobar_baja_abonado(f_lista_abonados=lista_abonados, f_estado_plazas=estado_plazas)
    opcion = int
    while opcion != 0:
        try:
            opcion = int(input(views.opciones_zonas()))
            if opcion != 0 and opcion != 1 and opcion != 2:
                raise ValueError
            else:
                if opcion == 0:
                    pickle_service.actualizar_lista_abonados(lista_abonados)
                    pickle_service.actualizar_lista_clientes(lista_clientes)
                    pickle_service.actualizar_estado_plazas(estado_plazas)
                    pickle_service.actualizar_recaudacion_abonados(recaudacion_abonados)
                    pickle_service.actualizar_recaudacion(recaudacion)
                    pickle_service.actualizar_parking(parking)
                    pass
                if opcion == 1:
                    try:
                        opcion_cliente = int(input(views.opcion_cliente()))
                        if opcion_cliente != 0 and opcion_cliente != 1 and opcion_cliente != 2 and opcion_cliente != 3 and opcion_cliente != 4:
                            raise ValueError
                        else:
                            if opcion_cliente == 0:
                                pass
                            elif opcion_cliente == 1:
                                parking_service.mostrar_plazas(parking=parking)
                                parking_service.depositar_vehiculo(parking=parking, f_estado_plazas=estado_plazas,
                                                                   f_lista_clientes=lista_clientes)
                            elif opcion_cliente == 2:
                                parking_service.retirar_vehiculo(parking=parking, f_lista_clientes=lista_clientes,
                                                                 f_estado_plazas=estado_plazas,
                                                                 f_recaudacion=recaudacion)
                            elif opcion_cliente == 3:
                                parking_service.mostrar_plazas(parking=parking)
                                parking_service.depositar_vehiculo_abonado(f_estado_plazas=estado_plazas,
                                                                           f_lista_clientes=lista_clientes,
                                                                           f_lista_abonados=lista_abonados)
                            elif opcion_cliente == 4:
                                parking_service.retirar_vehiculo_abonado(f_estado_plazas=estado_plazas,
                                                                         f_lista_clientes=lista_clientes)
                    except ValueError:
                        print("⚠️ ️Error. Introduce 0, 1, 2, 3 o 4 ⚠️")

                elif opcion == 2:
                    try:
                        opcion_admin = int(input(views.opcion_admin()))
                        if opcion_admin != 0 and opcion_admin != 1 and opcion_admin != 2 and opcion_admin != 3 and opcion_admin != 4 and opcion_admin != 5:
                            raise ValueError
                        else:
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

                                try:
                                    opcion_abono = int(input(views.opcion_abono()))
                                    if opcion_abono != 0 and opcion_abono != 1 and opcion_abono != 2 and opcion_abono != 3 and opcion_abono != 4:
                                        raise ValueError
                                    else:
                                        if opcion_abono == 0:
                                            pass
                                        elif opcion_abono == 1:
                                            abonados_service.crear_abonado(f_estado_plazas=estado_plazas,
                                                                           f_lista_abonados=lista_abonados,
                                                                           f_recaudacion_abonados=recaudacion_abonados,
                                                                           parking=parking)
                                        elif opcion_abono == 2:
                                            abonados_service.modificar_informacion_personal_abonado(
                                                f_lista_abonados=lista_abonados)
                                        elif opcion_abono == 3:
                                            abonados_service.modificar_abono(f_lista_abonados=lista_abonados,
                                                                             f_recaudacion_abonados=recaudacion_abonados)
                                        elif opcion_abono == 4:
                                            abonados_service.baja_abonado(f_estado_plazas=estado_plazas,
                                                                          f_listado_abonados=lista_abonados)
                                except ValueError:
                                    print("⚠️ Error. Introduce 0, 1, 2, 3 o 4 ⚠️")

                            elif opcion_admin == 5:
                                abonados_service.caducidad_abonos(f_listado_abonados=lista_abonados)
                    except ValueError:
                        print("⚠️ Error. Introduce 0, 1, 2, 3, 4 o 5 ⚠️")
        except ValueError:
            print("⚠️ Error. Introduce 0, 1 o 2 ⚠️")


main_thread = Thread(target=main_de_verdad)
actualizado_thread = Thread(target=actualizado_automatico)

main_thread.start()
actualizado_thread.start()
