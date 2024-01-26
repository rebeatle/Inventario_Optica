import sqlite3




class BaseData():
    def __init__(self, db_path="optica_base.db"):
        self.conexion = sqlite3.connect(db_path)
        self.cursor = self.conexion.cursor()

    def insertar_cliente(self, nombre, numero1, numero2, correo, dni, direccion, ruc, fecha, observacion):
        sql = """INSERT INTO clientes (nombre, numero1, numero2, correo, dni, direccion, ruc, fecha, observacion)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        parametros = (nombre, numero1, numero2, correo, dni, direccion, ruc, fecha, observacion)

        try:
            self.cursor.execute(sql, parametros)
            self.conexion.commit()
            print("Cliente insertado correctamente.")
            # Obtener el último ID insertado
            id_cliente = self.cursor.lastrowid

            return id_cliente
        except sqlite3.Error as e:
            print(f"Error al insertar cliente: {e}")

    def insertar_medidas(self, id_cliente, od_esfera, od_cilindro, od_eje, od_adicion, od_esfera_c, od_np, oi_esfera, oi_cilindro, oi_eje, oi_adicion, oi_esfera_c, oi_np):
        query = """
        INSERT INTO medidas (id_cliente,od_esfera,oi_esfera,od_cilindo,oi_cilindo, od_eje, oi_eje,od_adicion, oi_adicion,od_esfera_c, oi_esfera_c,od_np, oi_np)
        VALUES ( ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        medidas = (id_cliente,od_esfera, od_cilindro, od_eje, od_adicion, od_esfera_c, od_np, oi_esfera, oi_cilindro, oi_eje, oi_adicion, oi_esfera_c, oi_np)
        try:
            self.cursor.execute(query, medidas)
            self.conexion.commit()
            print("Cliente insertado correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar medida: {e}")

    def cerrar_conexion(self):
        self.conexion.close()

    def buscar_cliente_por_id(self, id_cliente):
        query_cliente = "SELECT * FROM clientes WHERE id_cliente = ?"
        query_medidas = "SELECT * FROM medidas WHERE id_cliente = ?"
        parametros = (id_cliente,)

        try:
            # Obtener datos del cliente
            self.cursor.execute(query_cliente, parametros)
            cliente = self.cursor.fetchone()

            # Obtener medidas del cliente
            self.cursor.execute(query_medidas, parametros)
            medidas_cliente = self.cursor.fetchone()

            return cliente, medidas_cliente
        except sqlite3.Error as e:
            print(f"Error al buscar cliente por ID: {e}")
            return None
    def buscar_cliente_db(self, nombre_o_dni):
        query = """SELECT * FROM clientes WHERE nombre LIKE ? OR dni = ?"""
        parametros = (f"%{nombre_o_dni}%", nombre_o_dni)

        try:
            self.cursor.execute(query, parametros)
            resultados = self.cursor.fetchall()
            return resultados
        except sqlite3.Error as e:
            print(f"Error al buscar cliente: {e}")
            return []