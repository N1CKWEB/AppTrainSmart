from ClienteDAO_GYM import ClienteDAO_GYM_1
from Cliente_GYM import Cliente_1
import customtkinter as ctk
from customtkinter import CTkImage, CTkScrollableFrame
import tkinter as tk
from tkinter import messagebox
from PIL import Image
import os

class ScrollBar_1(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []
        self.pack(pady=23)

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=5, pady=5, sticky="ew")
            self.checkboxes.append(checkbox)

    def obtener(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes
    
class ScrollBar_2(ctk.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []
        
        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=5, pady=5, sticky='ew')
            self.checkboxes.append(checkbox)
            
    def obtener(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes         

class ScrollBar_3(ctk.CTkScrollableFrame):
    
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []
        
        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=5, pady=5, sticky='ew')
            self.checkboxes.append(checkbox)
            
    def obtener(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes         

class TrainSmart(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_imagen()
        self.mostrar_formulario()
        self.mostrar_botones()
        self.mostrar_link_registro()
        
    def configurar_ventana(self):
        self.geometry('300x500')
        self.resizable(0, 0)
        self.configure(bg='#0F1111')

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)

    def mostrar_imagen(self):
        ruta_imagen = 'C:/Users/LENOVO/OneDrive/Documentos/AppTrainSmart_GYM/Imagenes/Trainsmart.png'
        if not os.path.isfile(ruta_imagen):
            messagebox.showerror("Error", f"No se encontró el archivo: {ruta_imagen}")
            return

        imagen = Image.open(ruta_imagen)
        imagen_redimensionada = imagen.resize((100, 100))  # Ajusta el tamaño según sea necesario
        imagen_tk = CTkImage(imagen_redimensionada)
        imagen_label = ctk.CTkLabel(self, image=imagen_tk, text="")
        imagen_label.image = imagen_tk
        imagen_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    def mostrar_formulario(self):
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.grid(row=1, column=0, padx=20, pady=(10, 10))

        usuario_etiqueta = ctk.CTkLabel(self.frame_form, text='Usuario')
        usuario_etiqueta.grid(row=0, column=0, padx=10, pady=10)

        self.usuario_caja_de_texto = ctk.CTkEntry(self.frame_form)
        self.usuario_caja_de_texto.grid(row=0, column=1, padx=10, pady=10)

        contraseña_etiqueta = ctk.CTkLabel(self.frame_form, text='Contraseña')
        contraseña_etiqueta.grid(row=1, column=0, padx=20, pady=10)

        self.contraseña_caja_de_texto = ctk.CTkEntry(self.frame_form, show="*")
        self.contraseña_caja_de_texto.grid(row=1, column=1, padx=10, pady=10)

    def mostrar_botones(self):
        login_boton = ctk.CTkLabel(self, text='Iniciar sesión', text_color='blue', cursor='hand2', bg_color='black')
        login_boton.grid(row=2, column=0, padx=20, pady=(10, 5))
        login_boton.bind('<Button-1>', self.Segunda_Ventana)

    def loguarse_y_guardar_cliente_en_la_bd(self):
        pass

    def Segunda_Ventana(self, event=None):
        ventana_registro_de_entrenamiento = ctk.CTkToplevel(self)
        ventana_registro_de_entrenamiento.title('Registrar entrenamiento')
        ventana_registro_de_entrenamiento.geometry('300x500')
        ventana_registro_de_entrenamiento.resizable(0, 0)
        ventana_registro_de_entrenamiento.columnconfigure(0, weight=1)

        imagen_original_1 = Image.open('C:/Users/LENOVO/OneDrive/Documentos/AppTrainSmart_GYM/Imagenes/1.png')
        imagen_redimensionada_1 = imagen_original_1.resize((410, 200))
        imagen_tk_1 = CTkImage(imagen_redimensionada_1)
        boton_registrar_entrenamiento = ctk.CTkLabel(ventana_registro_de_entrenamiento, image=imagen_tk_1, fg_color="transparent", bg_color="transparent", text='')
        boton_registrar_entrenamiento.image = imagen_tk_1
        boton_registrar_entrenamiento.grid(row=0, column=0, padx=20, pady=(5, 10), sticky="n")
        boton_registrar_entrenamiento.bind("<Button-1>", self.registrar_entrenamiento)

        imagen_original_2 = Image.open('C:/Users/LENOVO/OneDrive/Documentos/AppTrainSmart_GYM/Imagenes/2.png')
        imagen_redimensionada_2 = imagen_original_2.resize((410, 200))
        imagen_tk_2 = CTkImage(imagen_redimensionada_2)
        boton_registrar_entrenamiento_futuro = ctk.CTkLabel(ventana_registro_de_entrenamiento, image=imagen_tk_2, fg_color="transparent", bg_color="transparent", text='')
        boton_registrar_entrenamiento_futuro.image = imagen_tk_2
        boton_registrar_entrenamiento_futuro.grid(row=1, column=0, padx=20, pady=(5, 10), sticky="n")
        boton_registrar_entrenamiento_futuro.bind("<Button-1>", self.registrar_entrenamiento_futuro)

        imagen_original_3 = Image.open('C:/Users/LENOVO/OneDrive/Documentos/AppTrainSmart_GYM/Imagenes/3.png')
        imagen_redimensionada_3 = imagen_original_3.resize((410, 200))
        imagen_tk_3 = CTkImage(imagen_redimensionada_3)
        boton_seguimiento_registrado_anteriormente = ctk.CTkLabel(ventana_registro_de_entrenamiento, image=imagen_tk_3, fg_color='transparent', bg_color='transparent', text='')
        boton_seguimiento_registrado_anteriormente.image = imagen_tk_3
        boton_seguimiento_registrado_anteriormente.grid(row=2, column=0, padx=20, pady=(5, 10), sticky="n")
        boton_seguimiento_registrado_anteriormente.bind("<Button-1>", self.seguimiento_registrado_anteriormente)

        scroll_frame1 = ScrollBar_1(ventana_registro_de_entrenamiento, 'Ejercicios', ['Ejercicio 1', 'Ejercicio 2', 'Ejercicio 3'])
        scroll_frame1.grid(row=3, column=0, padx=20, pady=(5, 10))

        scroll_frame2 = ScrollBar_2(ventana_registro_de_entrenamiento, 'Repeticiones', ['Repetición 1', 'Repetición 2', 'Repetición 3'])
        scroll_frame2.grid(row=4, column=0, padx=20, pady=(5, 10))

        scroll_frame3 = ScrollBar_3(ventana_registro_de_entrenamiento, 'Series', ['Serie 1', 'Serie 2', 'Serie 3'])
        scroll_frame3.grid(row=5, column=0, padx=20, pady=(5, 10))


   
   
   
    def registrar_entrenamiento(self, event=None):
        ventana_del_primer_boton = ctk.CTkToplevel(self)
        ventana_del_primer_boton.title('Registrar entrenamiento realizado')
        ventana_del_primer_boton.geometry('300x500')
        ventana_del_primer_boton.columnconfigure(0, weight=1)
        ventana_del_primer_boton.rowconfigure([0, 1, 2], weight=1)

        values_1 = ["Cardio", "Fuerza", "Flexibilidad"]
        self.scrollable_checkbox_frame = ScrollBar_1(ventana_del_primer_boton, title="Tipo de Ejercicio", values=values_1)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=3, pady=5, sticky="nsew")

        values_2 = ['Pecho', 'Espalda', 'Piernas', 'Hombros', 'Biceps', 'Triceps', 'Gluteos']
        self.scrollable_checkbox_frame_2 = ScrollBar_2(ventana_del_primer_boton, title="Parte del Cuerpo Entrenada", values=values_2)
        self.scrollable_checkbox_frame_2.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        values_3 = ["Muy fácil", "Fácil", "Normal", "Difícil", "Muy difícil"]
        self.scrollable_checkbox_frame_3 = ScrollBar_3(ventana_del_primer_boton, title="Nivel de Dificultad", values=values_3)
        self.scrollable_checkbox_frame_3.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')


       
      
       #  BOTON PARA ENVIAR COMPLETO EL FORMULARIO  
        self.button = ctk.CTkButton(ventana_del_primer_boton, text="my button", command=self.boton_enviar_registro)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)


    def boton_enviar_registro(self):
        pass
  
    def registrar_entrenamiento_futuro(self, event=None):
             
        # Creamos ventana para el primer botón
        ventana_del_primer_boton = ctk.CTkToplevel(self)
        ventana_del_primer_boton.title('Registrar entrenamiento futuro')
        
        # Ajustamos el tamaño de la ventana para que sea más compacto
        ventana_del_primer_boton.geometry('300x500')  

        # Hacemos que las columnas y filas se ajusten para que ocupen todo el espacio disponible
        ventana_del_primer_boton.columnconfigure(0, weight=1)
        ventana_del_primer_boton.rowconfigure([0, 1, 2], weight=1)

        # Agregar ScrollBar dentro de la ventana del primer botón
        values_1 = ["Cardio", "Fuerza", "Flexibilidad"]
        self.scrollable_checkbox_frame = ScrollBar_1(ventana_del_primer_boton, title="Tipo de Ejercicio", values=values_1)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=3, pady=5, sticky="nsew")

        values_2 = ['25m', '30m', '40m', '45m', '1h', '2h']
        self.scrollable_checkbox_frame_2 = ScrollBar_2(ventana_del_primer_boton, title='Duración estimada del entrenamiento', values=values_2)
        self.scrollable_checkbox_frame_2.grid(row=1, column=0, padx=3, pady=5, sticky="nsew")

        values_3 = ['Perder Peso', 'Mejorar Resistencia', 'Ganar masa muscular']
        self.scrollable_checkbox_frame_3 = ScrollBar_3(ventana_del_primer_boton, title='Objetivo del entrenamiento', values=values_3)
        self.scrollable_checkbox_frame_3.grid(row=2, column=0, padx=3, pady=5, sticky="nsew")
       
      
       #  BOTON PARA ENVIAR COMPLETO EL FORMULARIO  
        self.button = ctk.CTkButton(ventana_del_primer_boton, text="my button", command=self.boton_enviar_registro)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

    def seguimiento_registrado_anteriormente(self, event=None):
        # Crear ventana para mostrar entrenamientos
        ventana_seguimiento = ctk.CTkToplevel(self)
        ventana_seguimiento.title('Entrenamientos Registrados')
        ventana_seguimiento.geometry('300x500')

        # Hacer que las columnas y filas se ajusten
        ventana_seguimiento.columnconfigure(0, weight=1)
        ventana_seguimiento.rowconfigure([0, 1], weight=1)

        # Crear un marco para mostrar los entrenamientos
        frame_lista = ctk.CTkFrame(ventana_seguimiento)
        frame_lista.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Crear un Listbox para mostrar los entrenamientos
        self.lista_entrenamientos = tk.Listbox(frame_lista)
        self.lista_entrenamientos.pack(fill=tk.BOTH, expand=True)

        # Agregar algunos entrenamientos de ejemplo a la lista
        self.entrenamientos = [
            {"tipo": "Cardio", "duracion": "30m", "grupo": "Pecho"},
            {"tipo": "Fuerza", "duracion": "1h", "grupo": "Piernas"},
            {"tipo": "Flexibilidad", "duracion": "45m", "grupo": "Espalda"}
        ]
        for entrenamiento in self.entrenamientos:
            self.lista_entrenamientos.insert(tk.END, f"{entrenamiento['tipo']} - {entrenamiento['duracion']} - {entrenamiento['grupo']}")

        # Botón para editar entrenamiento
        self.btn_editar = ctk.CTkButton(ventana_seguimiento, text="Editar", command=self.editar_entrenamiento)
        self.btn_editar.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        # Botón para eliminar entrenamiento
        self.btn_eliminar = ctk.CTkButton(ventana_seguimiento, text="Eliminar", command=self.eliminar_entrenamiento)
        self.btn_eliminar.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

    def editar_entrenamiento(self):
        # Obtener el índice del entrenamiento seleccionado
        seleccion = self.lista_entrenamientos.curselection()
        if seleccion:
            index = seleccion[0]
            entrenamiento = self.entrenamientos[index]

            # Crear ventana para editar el entrenamiento
            ventana_editar = ctk.CTkToplevel(self)
            ventana_editar.title('Editar Entrenamiento')
            ventana_editar.geometry('300x500')

            # Campos para editar
            tipo_var = tk.StringVar(value=entrenamiento['tipo'])
            duracion_var = tk.StringVar(value=entrenamiento['Duracion'])
            grupo_var = tk.StringVar(value=entrenamiento['grupo'])

            ctk.CTkLabel(ventana_editar, text="Tipo de Ejercicio").pack()
            tipo_entry = ctk.CTkEntry(ventana_editar, textvariable=tipo_var)
            tipo_entry.pack()

            ctk.CTkLabel(ventana_editar, text="Duración").pack()
            duracion_entry = ctk.CTkEntry(ventana_editar, textvariable=duracion_var)
            duracion_entry.pack()

            ctk.CTkLabel(ventana_editar, text="Grupo Muscular").pack()
            grupo_entry = ctk.CTkEntry(ventana_editar, textvariable=grupo_var)
            grupo_entry.pack()

            # Botón para guardar cambios
            btn_guardar = ctk.CTkButton(ventana_editar, text="Guardar", command=lambda: self.guardar_cambios(index, tipo_var.get(), duracion_var.get(), grupo_var.get(), ventana_editar))
            btn_guardar.pack(pady=10)

    def guardar_cambios(self, index, tipo, duracion, grupo, ventana):
        # Actualizar el entrenamiento en la lista
        self.entrenamientos[index] = {"tipo": tipo, "duracion": duracion, "grupo": grupo}
        self.lista_entrenamientos.delete(index)
        self.lista_entrenamientos.insert(index, f"{tipo} - {duracion} - {grupo}")
        ventana.destroy()  # Cerrar ventana de edición

    def eliminar_entrenamiento(self):
        # Obtener el índice del entrenamiento seleccionado
        seleccion = self.lista_entrenamientos.curselection()
        if seleccion:
            index = seleccion[0]
            self.entrenamientos.pop(index)  # Eliminar de la lista
            self.lista_entrenamientos.delete(index)  # Eliminar de la lista visual

    
        
    def mostrar_link_registro(self):
        # Crear un link de texto para registrarse
        registro_link = ctk.CTkLabel(self, text="Si no tienes cuenta, regístrate", text_color="blue", cursor="hand2")
        registro_link.grid(row=3, column=0, padx=20, pady=5)  # Debajo del botón de Iniciar Sesión
        
        # Asociar la función que abre la ventana de registro
        registro_link.bind("<Button-1>", self.abrir_ventana_registro)
    
    def abrir_ventana_registro(self, event=None):
        # Crear una nueva ventana para el registro
        ventana_registro = ctk.CTkToplevel(self)
        ventana_registro.title("Registro")
        ventana_registro.geometry('300x500')
        
        # Usar grid para organizar los widgets
        ventana_registro.columnconfigure(0, weight=1)

        # Título de la ventana de registro
        registro_titulo = ctk.CTkLabel(ventana_registro, text="Crear Cuenta", font=('Arial', 20), text_color='blue')
        registro_titulo.grid(row=0, column=0, padx=10, pady=20)

        # Campos del formulario
        nombre_label = ctk.CTkLabel(ventana_registro, text="Nombre")
        nombre_label.grid(row=1, column=0, padx=10, pady=10)

        nombre_entry = ctk.CTkEntry(ventana_registro)
        nombre_entry.grid(row=2, column=0, padx=10, pady=10)

        usuario_label = ctk.CTkLabel(ventana_registro, text="Usuario")
        usuario_label.grid(row=3, column=0, padx=10, pady=10)

        usuario_entry = ctk.CTkEntry(ventana_registro) 
        usuario_entry.grid(row=4, column=0, padx=10, pady=10)

        contraseña_label = ctk.CTkLabel(ventana_registro, text="Contraseña")
        contraseña_label.grid(row=5, column=0, padx=10, pady=10)

        contraseña_entry = ctk.CTkEntry(ventana_registro)
        contraseña_entry.grid(row=6, column=0, padx=10, pady=10)

        # Botón Registrar
        registrar_boton = ctk.CTkButton(ventana_registro, text="Registrar", command=lambda: self.registrar_nuevo_usuario(nombre_entry, usuario_entry, contraseña_entry))
        registrar_boton.grid(row=7, column=0, padx=10, pady=20, sticky="s")

    def registrar_nuevo_usuario(self):
        # Ejemplo de implementación de este método
        usuario = self.usuario_caja_de_texto.get()
        contraseña = self.contraseña_caja_de_texto.get()

        if usuario and contraseña:
            # Aquí puedes añadir lógica para registrar al nuevo usuario en la base de datos.
            messagebox.showinfo("Registro", "Usuario registrado con éxito.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

if __name__ == "__main__":
    app = TrainSmart()
    app.mainloop()
