import datetime
import pickle


class AdministradorService:
    def mostrar_estado_parking(self, f_estado_plazas):
        for i in range(1, 61):
            if f_estado_plazas[i] == 'Libre':
                print('Plaza ' + str(i) + ': Libre ✅   ', end='')
            elif f_estado_plazas[i] == 'Ocupada':
                print('Plaza ' + str(i) + ': Ocupada 🚗    ', end='')
            elif f_estado_plazas[i] == 'Reservada libre':
                print('Plaza ' + str(i) + ': Reservada libre 🅿️    ', end='')
            else:
                print('Plaza ' + str(i) + ': Reservada ocupado 🛑️    ', end='')
            if i % 5 == 0:
                print('\n')

    def calcular_recaudacion_entre_horas(self, f_recaudacion):

        sum = 0.0
        cant = 0

        print("Fecha de inicio de la recaudación")
        anho1 = int(input("Año: "))
        mes1 = int(input("Mes: "))
        dia1 = int(input("Día: "))
        hora1 = int(input("Hora: "))
        minuto1 = int(input("Minuto: "))

        print("Fecha final de la recaudación")
        anho2 = int(input("Año: "))
        mes2 = int(input("Mes: "))
        dia2 = int(input("Día: "))
        hora2 = int(input("Hora: "))
        minuto2 = int(input("Minuto: "))

        fecha_inicio = datetime.datetime(anho1, mes1, dia1, hora1, minuto1)
        fecha_fin = datetime.datetime(anho2, mes2, dia2, hora2, minuto2)

        for fecha, cobro in f_recaudacion.items():
            if fecha_inicio < fecha < fecha_fin:
                sum += cobro
                cant += 1
                print("Fecha: {}/{}/{}".format(fecha.day, fecha.month, fecha.year),
                      "- {}:{}:{}".format(fecha.hour, fecha.minute, fecha.second))
                print("Recaudacion: ", str(cobro))
                print("========================")
        print("La recaudación total entre " + str(fecha_inicio) + " y " + str(fecha_fin) + " ha sido de " + str(
            sum) + " € con un total de " + str(cant) + " cobro/s")

    def consultar_abonados(self, f_recaudacion_abonados, f_lista_abonados):

        sum = 0.0

        for k, v in f_recaudacion_abonados.items():
            sum += v

        for a in f_lista_abonados:
            print(a)
            print("==========================================================================")

        print("\n Se han recaudado un total de " + str(sum) + "€")
