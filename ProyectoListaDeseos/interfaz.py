import tkinter as tk
from conexionInterface import ConexionDB
from tkinter import messagebox
class InterfazListaDeseos:
    def __init__(self, conexion):
        self.conexion = conexion

        self.ventana = tk.Tk()
        self.ventana.title("Lista de Deseos")
        self.ventana.configure(bg="black")  # Configurar el color de fondo para tema oscuro

        self.crear_interfaz()# Creamos la interfaz gráfica

    def crear_interfaz(self):
        # Crear los elementos de la interfaz
        # Título de la Interfaz
        self.titulo_label = tk.Label(self.ventana, text="Lista de Deseos Grupo GIGABYTE", font=("Arial", 16), bg="black", fg="white")
        self.titulo_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        # Etiqueta y campo de texto para ingresar el producto
        self.producto_label = tk.Label(self.ventana, text="Producto:", bg="black", fg="white")
        self.producto_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
