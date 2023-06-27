import psycopg2 # Importamos la base de datos, usaremos PostgresSQL
class ConexionDB:#Definimos la clase
 
# Establecemos la conexion con la base de datos
    def init(self):
            self.conexion = psycopg2.connect(
                host="localhost",
                database="proyecto_Python",
                user="postgres",
                password="admin"
            )
            self.crear_tabla()# LLamamos al metodo crear tabla
    
    def crear_tabla(self):
        # Con este metodo creamos la tabla 'deseos' si no existe
        # Utilizara los siguientes campos: id, producto, cantidad, precio
        cursor = self.conexion.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS deseos (
                id SERIAL PRIMARY KEY,
                producto TEXT,
                cantidad INTEGER,
                precio REAL
            )
            """
        )
        self.conexion.commit()
     
     def agregar_deseo(self, producto, cantidad, precio):
        # Insertamos los datos en la tabla 'deseos'
        cursor = self.conexion.cursor()
        cursor.execute(
            """
            INSERT INTO deseos (producto, cantidad, precio)
            VALUES (%s, %s, %s)
            """,
            (producto, cantidad, precio)
        )
        self.conexion.commit()
      
    def eliminar_deseo(self, id_deseo):
        # Eliminamos el registro con el ID proporcionado de la tabla 'deseos'
        cursor = self.conexion.cursor()
        cursor.execute(
            """
            DELETE FROM deseos WHERE id = %s
            """,
            (id_deseo,)
         )
         self.conexion.commit()

    def eliminar_todo(self):
        # Eliminamos todos los registros de la tabla 'deseos'
        cursor = self.conexion.cursor()
        cursor.execute(
            """
            DELETE FROM deseos
            """
        )
        self.conexion.commit()

    def obtener_deseos(self):
        # Obtenemos todos los registros de la tabla 'deseos'
        cursor = self.conexion.cursor()
        cursor.execute(
            """
            SELECT * FROM deseos
            """
        )
        return cursor.fetchall()


