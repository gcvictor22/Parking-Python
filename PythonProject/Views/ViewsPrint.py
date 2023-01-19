class ViewPrint:
    def opciones_zonas(self):
        return "\n¿Donde quieres acceder?" \
               "\n0. Guardar y salir" \
               "\n1. Zona cliente" \
               "\n2. Zona administrador" \
               "\nOpción: "

    def opcion_cliente(self):
        return "\n¿Qué deseas hacer?" \
               "\n0. Salir" \
               "\n1. Depositar vehículo" \
               "\n2. Retirar vehículo" \
               "\n3. Depositar vehículo (abonado)" \
               "\n4. Retirar vehículo (abonado)" \
               "\nOpción: "

    def opcion_admin(self):
        return "\n¿Qué deseas hacer?" \
               "\n0. Salir" \
               "\n1. Ver estado del parking" \
               "\n2. Facturación" \
               "\n3. Consulta de abonados" \
               "\n4. Gestión abonados" \
               "\n5. Caducidad abonos" \
               "\nOpción: "

    def opcion_abono(self):
        return "\n¿Qué deseas hacer?" \
               "\n0. Salir" \
               "\n1. Darme de alta como abonado" \
               "\n2. Modificar información personal" \
               "\n3. Renovar abono" \
               "\n4. Darme de baja" \
               "\nOpción: "

    def elegir_abono(self):
        return "\n¿Qué tipo de abono quieres contratar?" \
               "\n1. Mensual 25€" \
               "\n2. Trimestrar 70€" \
               "\n3. Semestral 130€" \
               "\n4. Anual 200€" \
               "\nOpción: "

    def elegir_tipo_vehiculo(self):
        return "\n¿Qué tipo de vehiculo es?" \
               "\n1. Turismo" \
               "\n2. Moto" \
               "\n3. Movilidad reducida" \
               "\nOpción: "

    def elegir_editar_persona(self):
        return "\n¿Qué deseas editar?" \
               "\n1. Nombre y apellidos" \
               "\n2. Gmail" \
               "\n3. Tarjeta de crédito" \
               "\n4. Todo lo anterior" \
               "\nOpción: "

    def comprobar_abonos(self):
        return "\n¿Qué deseas comprobar: " \
               "\n1. Comprobar abonos que caducan un mes" \
               "\n2. Comprobar abonos que caducan dentro de 10 días" \
               "\nOpción: "
