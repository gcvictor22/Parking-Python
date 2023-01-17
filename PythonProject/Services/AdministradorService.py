import datetime


class AdministradorService:
    def mostrar_estado_parking(self, parking):
        for i in range(1, 61):
            if parking.estado_plazas[i] == 'Libre':
                print('Plaza ' + str(i) + ': Libre ✅   ', end='')
            elif parking.estado_plazas[i] == 'Ocupada':
                print('Plaza ' + str(i) + ': Ocupada 🚗    ', end='')
            elif parking.estado_plazas[i] == 'Reservada libre':
                print('Plaza ' + str(i) + ': Reservada libre 🅿️    ', end='')
            else:
                print('Plaza ' + str(i) + ': Reservada ocupado 🛑️    ', end='')
            if i % 5 == 0:
                print('\n')

    def calcular_recaudacion_entre_horas(self, parking):

        sum = 0.0
        cant = 0

        print("Fecha de inicio de la recaudación")
        anho1 = int(input("Año: "))
        mes1 = int(input("Mes: "))
        dia1 = int(input("Día: "))
        hora1 = int(input("Hora: "))
        minuto1 = int(input("Minuto: "))
        segundo1 = int(input("Segundo: "))

        print("Fecha final de la recaudación")
        anho2 = int(input("Año: "))
        mes2 = int(input("Mes: "))
        dia2 = int(input("Día: "))
        hora2 = int(input("Hora: "))
        minuto2 = int(input("Minuto: "))
        segundo2 = int(input("Segundo: "))

        fecha_inicio = datetime.datetime(anho1, mes1, dia1, hora1, minuto1, segundo1)
        fecha_fin = datetime.datetime(anho2, mes2, dia2, hora2, minuto2, segundo2)

        for fecha, cobro in parking.recaudacion.items():
            if fecha_inicio < fecha < fecha_fin:
                sum += cobro
                cant += 1
                print("Fecha: {}/{}/{}".format(fecha.day, fecha.month, fecha.year),
                      "- {}:{}:{}".format(fecha.hour, fecha.minute, fecha.second))
                print("Recaudacion: ", str(cobro))
                print("========================")
        print("La recaudación total entre " + str(fecha_inicio) + " y " + str(fecha_fin) + " ha sido de " + str(
            sum) + " € con un total de " + str(cant) + " cobro/s")

    def consultar_abonados(self, parking):

        sum = 0.0

        for k, v in parking.recaudacion_abonos.items():
            sum += v

        abonados = parking.lista_abonados

        for abonado in abonados:
            abonado.__str__()
            print("=====================================================")

        print("\n Se han recaudado un total de " + str(sum) + "€")
