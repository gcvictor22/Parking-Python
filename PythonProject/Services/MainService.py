from datetime import datetime
from datetime import timedelta

from Models.Abonado import Abonado
from Models.Cliente import Cliente
from Models.Parking import Parking
from Models.Vehiculo import Vehiculo


class MainService:
    parking = Parking(plazas_totales=60, plazas_turismo=42, plazas_motos=9, plazas_minusvalidos=9)
    recaudacion_abonos = {}
    estado_plazas = {}
    lista_abonados = []
    lista_clientes = []
    recaudacion = {}

    for i in range(1, 61):
        estado_plazas[i] = "Libre"

    v1 = Vehiculo(matricula='1234 AAA', tipo='Moto')
    fecha_activacion_bono1 = datetime(year=2022, month=10, day=7, hour=12, minute=36, second=51)
    fecha_caducidad_abono1 = fecha_activacion_bono1 + timedelta(days=183)
    ab1 = Abonado(nombre='John', apellidos='Doe', gmail='johndoe@gmail.com', dni='12345678-A',
                  tarjeta='1234 5678 9123 4567',
                  tipo_abono='semestral', vehiculo=v1, plaza_parking=42,
                  fecha_activacion_abono=fecha_activacion_bono1,
                  fecha_caducidad_abono=fecha_caducidad_abono1, fecha_deposito='', pin=478392)
    estado_plazas[ab1.plaza_parking] = "Reservada libre"
    recaudacion_abonos[ab1.tarjeta] = 130
    parking.plazas_motos -= 1
    parking.plazas_totales -= 1
    lista_abonados.append(ab1)

    v2 = Vehiculo(matricula='5678 BBB', tipo='Turismo')
    fecha_activacion_bono2 = datetime(year=2023, month=1, day=10, hour=8, minute=47, second=23)
    fecha_caducidad_abono2 = fecha_activacion_bono1 + timedelta(days=90)
    ab2 = Abonado(nombre='Eladio', apellidos='Carrion', gmail='hugoboss@gmail.com', dni='87654321-Z',
                  tarjeta='1111 2222 3333 4444',
                  tipo_abono='trimestral', vehiculo=v2, plaza_parking=24,
                  fecha_activacion_abono=fecha_activacion_bono2,
                  fecha_caducidad_abono=fecha_caducidad_abono2, fecha_deposito='', pin=279053)
    estado_plazas[ab2.plaza_parking] = "Reservada libre"
    recaudacion_abonos[ab2.tarjeta] = 70
    parking.plazas_turismo -= 1
    parking.plazas_totales -= 1
    lista_abonados.append(ab2)

    v3 = Vehiculo(matricula='1601 HTT', tipo='Moto')
    c1 = Cliente(fecha_deposito=datetime(year=2021, month=4, day=22, hour=9, minute=21, second=36), plaza_parking=22,
                 vehiculo=v3, pin=928492)
    estado_plazas[c1.plaza_parking] = "Ocupada"
    parking.plazas_motos -= 1
    parking.plazas_totales -= 1
    lista_clientes.append(c1)

    v4 = Vehiculo(matricula='8888 SPT', tipo='Movilidad reducida')
    c2 = Cliente(fecha_deposito=datetime(year=2023, month=1, day=17, hour=23, minute=12, second=21), plaza_parking=4,
                 vehiculo=v4, pin=498023)
    estado_plazas[c2.plaza_parking] = "Ocupada"
    parking.plazas_minusvalidos -= 1
    parking.plazas_totales -= 1
    lista_clientes.append(c2)

    v5 = Vehiculo(matricula='1818 KMZ', tipo='Turismo')
    c3 = Cliente(fecha_deposito=datetime(year=2023, month=1, day=17, hour=23, minute=12, second=21), plaza_parking=49,
                 vehiculo=v5, pin=917034)
    estado_plazas[c3.plaza_parking] = "Ocupada"
    parking.plazas_turismo -= 1
    parking.plazas_totales -= 1
    lista_clientes.append(c3)

    v6 = Vehiculo(matricula='8342 VPN', tipo='Movilidad reducida')
    c4 = Cliente(fecha_deposito=datetime(year=2022, month=12, day=30, hour=14, minute=56, second=2), plaza_parking=1,
                 vehiculo=v6, pin=724943)
    estado_plazas[c4.plaza_parking] = "Ocupada"
    parking.plazas_minusvalidos -= 1
    parking.plazas_totales -= 1
    lista_clientes.append(c4)
