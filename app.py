import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from datetime import date

# Supongamos que estas son las clases importadas
from Registrar_Entrenamiento import Registrar_Entrenamiento
from Registrar_Entrenamiento_Futuro import Registrar_Entrenamiento_Futuro
from Seguimiento_Registrado_Anteriormente import Seguimiento_Registrado_Anteriormente
from ClienteDAO_GYM import ClienteDAO_GYM_1  # Función de base de datos para obtener datos

# Clase principal para la ventana de seguimiento
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Sistema de Seguimiento de Entrenamientos')
        self.geometry('300x500')  # Ventana ajustada a 300x500
        
        # Botón para abrir la ventana de seguimiento
        btn_seguimiento = ctk.CTkButton(self, text="Ver Seguimientos", command=self.seguimiento_registrado_anteriormente)
        btn_seguimiento.pack(pady=20)

    # Función para mostrar el seguimiento de entrenamientos
    def seguimiento_registrado_anteriormente(self):
        ventana_seguimiento = ctk.CTkToplevel(self)
        ventana_seguimiento.title('Seguimiento de Entrenamientos')
        ventana_seguimiento.geometry('300x500')  # Ajustado a 300x500

        # Obtener entrenamientos desde la base de datos
        entrenamientos = ClienteDAO_GYM_1.obtener_entrenamientos()  # Esta función debería devolver entrenamientos de la BD

        # Crear tabla para mostrar entrenamientos
        columnas = ("Fecha", "Tipo de Ejercicio", "Duración", "Calorías Quemadas", "Comentarios")
        tabla = ttk.Treeview(ventana_seguimiento, columns=columnas, show="headings", height=5)

        # Configurar las columnas
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, anchor="center", width=70)

        # Insertar datos en la tabla
        for entrenamiento in entrenamientos:
            tabla.insert("", tk.END, values=(entrenamiento["fecha"], entrenamiento["tipo_ejercicio"],
                                             entrenamiento["duracion"], entrenamiento["calorias"],
                                             entrenamiento["comentarios"]))

        tabla.pack(pady=5)

        # Agregar botones para editar y eliminar
        selected_item = tabla.selection()  # Se obtiene el elemento seleccionado

        ctk.CTkButton(ventana_seguimiento, text="Editar", command=lambda: self.editar_entrenamiento(selected_item, tabla, entrenamientos)).pack(pady=10)
        ctk.CTkButton(ventana_seguimiento, text="Eliminar", command=lambda: self.eliminar_entrenamiento(selected_item, tabla, entrenamientos)).pack(pady=10)

        # Filtro por tipo de ejercicio
        ctk.CTkLabel(ventana_seguimiento, text="Filtrar por Tipo de Ejercicio").pack(pady=5)
        tipo_ejercicio = ctk.CTkComboBox(ventana_seguimiento, values=["Todos", "Cardio", "Fuerza", "Flexibilidad"])
        tipo_ejercicio.pack(pady=5)
        tipo_ejercicio.set("Todos")

        # Botón para aplicar el filtro
        ctk.CTkButton(ventana_seguimiento, text="Aplicar Filtro", command=lambda: self.aplicar_filtro(tabla, tipo_ejercicio.get(), entrenamientos)).pack(pady=10)

    def editar_entrenamiento(self, selected_item, tabla, entrenamientos):
        if not selected_item:
            return  # Si no hay selección, salir

        entrenamiento = entrenamientos[int(selected_item[0])]  # Obtiene el entrenamiento seleccionado

        ventana_editar = ctk.CTkToplevel(self)
        ventana_editar.title('Editar Entrenamiento')
        ventana_editar.geometry('300x400')

        # Campos para editar
        ctk.CTkLabel(ventana_editar, text="Tipo de Ejercicio").pack(pady=5)
        tipo_entry = ctk.CTkEntry(ventana_editar)
        tipo_entry.pack(pady=5)
        tipo_entry.insert(0, entrenamiento["tipo_ejercicio"])

        ctk.CTkLabel(ventana_editar, text="Duración").pack(pady=5)
        duracion_entry = ctk.CTkEntry(ventana_editar)
        duracion_entry.pack(pady=5)
        duracion_entry.insert(0, entrenamiento["duracion"])

        ctk.CTkLabel(ventana_editar, text="Calorías").pack(pady=5)
        calorias_entry = ctk.CTkEntry(ventana_editar)
        calorias_entry.pack(pady=5)
        calorias_entry.insert(0, entrenamiento["calorias"])

        ctk.CTkLabel(ventana_editar, text="Comentarios").pack(pady=5)
        comentarios_entry = ctk.CTkEntry(ventana_editar)
        comentarios_entry.pack(pady=5)
        comentarios_entry.insert(0, entrenamiento["comentarios"])

        # Botón para guardar cambios
        ctk.CTkButton(ventana_editar, text="Guardar Cambios", command=lambda: self.guardar_cambios(entrenamiento, tipo_entry.get(), duracion_entry.get(), calorias_entry.get(), comentarios_entry.get(), ventana_editar)).pack(pady=10)

    def guardar_cambios(self, entrenamiento, tipo, duracion, calorias, comentarios, ventana):
        # Aquí se debe actualizar la base de datos
        ClienteDAO_GYM_1.actualizar_entrenamiento(entrenamiento["id"], tipo, duracion, calorias, comentarios)

        # Cerrar la ventana
        ventana.destroy()

        # Actualizar la tabla de seguimientos
        self.seguimiento_registrado_anteriormente()

    def eliminar_entrenamiento(self, selected_item, tabla, entrenamientos):
        if not selected_item:
            return  # Si no hay selección, salir

        entrenamiento = entrenamientos[int(selected_item[0])]  # Obtiene el entrenamiento seleccionado
        ClienteDAO_GYM_1.eliminar_entrenamiento(entrenamiento["id"])

        # Actualizar la tabla de seguimientos
        self.seguimiento_registrado_anteriormente()

    # Función para aplicar filtros
    def aplicar_filtro(self, tabla, tipo, entrenamientos):
        # Limpiar la tabla
        for item in tabla.get_children():
            tabla.delete(item)

        # Filtrar los entrenamientos por tipo
        if tipo == "Todos":
            datos_filtrados = entrenamientos
        else:
            datos_filtrados = [e for e in entrenamientos if e["tipo_ejercicio"] == tipo]

        # Insertar los datos filtrados en la tabla
        for entrenamiento in datos_filtrados:
            tabla.insert("", tk.END, values=(entrenamiento["fecha"], entrenamiento["tipo_ejercicio"],
                                             entrenamiento["duracion"], entrenamiento["calorias"],
                                             entrenamiento["comentarios"]))


# Ejecución del programa principal
if __name__ == "__main__":
    app = App()
    app.mainloop()
