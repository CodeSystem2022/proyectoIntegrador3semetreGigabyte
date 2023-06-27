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
        # Botón para eliminar un deseo por ID
        self.eliminar_button = tk.Button(self.ventana, text="Eliminar por ID", command=self.eliminar_deseo, bg="black", fg="white")
        self.eliminar_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        # Botón para eliminar todos los deseos
        self.eliminar_todo_button = tk.Button(self.ventana, text="Eliminar Todo", command=self.eliminar_todo, bg="black", fg="white")
        self.eliminar_todo_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.lista_deseos_text = tk.Text(self.ventana, bg="black", fg="white")  # Configurar colores para tema oscuro
        self.lista_deseos_text.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        self.actualizar_lista_deseos()  # Mostrar la lista de deseos al iniciar la interfaz

    def actualizar_lista_deseos(self):
        deseos = self.conexion.obtener_deseos()

        self.lista_deseos_text.delete("1.0", tk.END)  # Limpiar el campo de texto

        if deseos:
            for deseo in deseos:
                texto = f"ID: {deseo[0]}, Producto: {deseo[1]}, Cantidad: {deseo[2]}, Precio: {deseo[3]}\n"
                self.lista_deseos_text.insert(tk.END, texto)
        else:
            self.lista_deseos_text.insert(tk.END, "No hay elementos en la lista de deseos.")

    def agregar_deseo(self):
        # Código para agregar un deseo a la base de datos
        producto = self.producto_entry.get()
        cantidad = int(self.cantidad_entry.get())
        precio = float(self.precio_entry.get())

        self.conexion.agregar_deseo(producto, cantidad, precio)
        print("Deseo agregado exitosamente.")

        self.actualizar_lista_deseos()  # Actualizar la lista mostrada en la interfaz
