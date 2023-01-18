import pickle


class PickleService:

    def cargar_lista_abonados(self):
        f_abonados = open('Ficheros/listado_abonados.pckl', 'rb')
        lista_fichero_abonados = pickle.load(f_abonados)
        f_abonados.close()
        return lista_fichero_abonados

    def cargar_lista_clientes(self):
        f_clientes = open('Ficheros/listado_clientes.pckl', 'rb')
        lista_fichero_clientes = pickle.load(f_clientes)
        f_clientes.close()
        return lista_fichero_clientes

    def cargar_recaudacion_abonados(self):
        f_recaudacion_abonados = open('Ficheros/recaudacion_abonados.pckl', 'rb')
        fichero_recaudacion_abonados = pickle.load(f_recaudacion_abonados)
        f_recaudacion_abonados.close()
        return fichero_recaudacion_abonados

    def cargar_estado_plazas(self):
        f_estado_plazas = open('Ficheros/estado_plazas.pckl', 'rb')
        estado_plazas = pickle.load(f_estado_plazas)
        f_estado_plazas.close()
        return estado_plazas

    def cargar_recaudacion(self):
        f_recaudacion = open('Ficheros/recaudacion.pckl', 'rb')
        recaudacion = pickle.load(f_recaudacion)
        f_recaudacion.close()
        return recaudacion

    def cargar_parking(self):
        f_parking = open('Ficheros/parking.pckl', 'rb')
        recaudacion = pickle.load(f_parking)
        f_parking.close()
        return recaudacion

    ###########################################################

    def actualizar_lista_abonados(self, lista_abonados):
        fichero_abonados = open('./Ficheros/listado_abonados.pckl', 'wb')
        pickle.dump(lista_abonados, fichero_abonados)
        fichero_abonados.close()

    def actualizar_lista_clientes(self, lista_clientes):
        fichero_clientes = open('./Ficheros/listado_clientes.pckl', 'wb')
        pickle.dump(lista_clientes, fichero_clientes)
        fichero_clientes.close()

    def actualizar_recaudacion_abonados(self, recaudacion_abonos):
        recaudacion_abonados = open('Ficheros/recaudacion_abonados.pckl', 'wb')
        pickle.dump(recaudacion_abonos, recaudacion_abonados)
        recaudacion_abonados.close()

    def actualizar_estado_plazas(self, estado_plazas):
        estados_plazas = open('Ficheros/estado_plazas.pckl', 'wb')
        pickle.dump(estado_plazas, estados_plazas)
        estados_plazas.close()

    def actualizar_recaudacion(self, recaudacion):
        recaudacion_clientes = open('Ficheros/recaudacion.pckl', 'wb')
        pickle.dump(recaudacion, recaudacion_clientes)
        recaudacion_clientes.close()

    def actualizar_parking(self, parking):
        a_parking = open('Ficheros/parking.pckl', 'wb')
        pickle.dump(parking, a_parking)
        a_parking.close()
