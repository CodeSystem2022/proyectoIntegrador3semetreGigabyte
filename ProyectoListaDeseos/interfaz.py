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

        self.producto_entry = tk.Entry(self.ventana, bg="black", fg="white")
        self.producto_entry.grid(row=1, column=1, padx=5, pady=5)
        # Etiqueta y campo de texto para ingresar la cantidad
        self.cantidad_label = tk.Label(self.ventana, text="Cantidad:", bg="black", fg="white")
        self.cantidad_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.cantidad_entry = tk.Entry(self.ventana, bg="black", fg="white")
        self.cantidad_entry.grid(row=2, column=1, padx=5, pady=5)
        # Etiqueta y campo de texto para ingresar el precio
        self.precio_label = tk.Label(self.ventana, text="Precio:", bg="black", fg="white")
        self.precio_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        self.precio_entry = tk.Entry(self.ventana, bg="black", fg="white")
        self.precio_entry.grid(row=3, column=1, padx=5, pady=5)
        # Botón para agregar un deseo
        self.agregar_button = tk.Button(self.ventana, text="Agregar", command=self.agregar_deseo, bg="black", fg="white")
        self.agregar_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        # Campo de texto para mostrar la lista de deseos
        self.eliminar_label = tk.Label(self.ventana, text="ID Deseo a eliminar:", bg="black", fg="white")
        self.eliminar_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")

        self.eliminar_entry = tk.Entry(self.ventana, bg="black", fg="white")
        self.eliminar_entry.grid(row=5, column=1, padx=5, pady=5)
