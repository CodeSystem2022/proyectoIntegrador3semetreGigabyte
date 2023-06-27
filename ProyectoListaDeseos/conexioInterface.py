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
