from conexionInterface import ConexionDB  #Importamos la clase ConexionDB
from interfaz import InterfazListaDeseos  #Importamos la clase InterfazListaDeseos

if __name__ == '__main__':
    conexion = ConexionDB()    # Se crea una variable de la clase ConexionDB
    interfaz = InterfazListaDeseos(conexion)  # Se crea una variable de la clase InterfazListaDeseos
    interfaz.iniciar() #se inicia la interfaz grafica
