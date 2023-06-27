from conexionInterface import ConexionDB
from interfaz import InterfazListaDeseos

if __name__ == '__main__':
    conexion = ConexionDB()    # Se crea una variable de la clase ConexionDB
    interfaz = InterfazListaDeseos(conexion)  # se crea una variable de la clase InterfazListaDeseos
    interfaz.iniciar() #se inicia la interfaz grafica
