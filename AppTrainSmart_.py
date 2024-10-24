from ClienteDAO_GYM import ClienteDAO_GYM_1
from Cliente_GYM import Cliente_1
from Registrar_Entrenamiento_RealizadoDAO import Registrar_Entrenamiento_RealizadoDAO
from Registrar_FuturoDAO import Registrar_FuturoDAO
# from Registrar_FuturoDAO import Registrar_FuturoDAO
# from SeguimientoAnteriormenteDAO import SeguimientoAnteriormenteDAO
import customtkinter as ctk
from customtkinter import CTkImage,CTkScrollableFrame
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage, Image
from PIL import Image, ImageTk
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

    # Agregamos el método get_selected_value
    def get_selected_value(self):
        return self.obtener()  # Utiliza el método existente para obtener los valores seleccionados

class ScrollBar_2(ctk.CTkScrollableFrame):
    def __init__(self,master,title,values):
        super().__init__(master,label_text=title)
        self.grid_columnconfigure(0,weight=1)
        self.values=values
        self.checkboxes=[]
        
        for i,value in enumerate(self.values):
            checkbox=ctk.CTkCheckBox(self,text=value)
            checkbox.grid(row=i,column=0,padx=5,pady=5,sticky='ew')
            self.checkboxes.append(checkbox)
            
    def obtener(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes        
     
      # Agregamos el método get_selected_value
    def get_selected_value(self):
        return self.obtener()  # Utiliza el método existente para obtener los valores seleccionados
    
class ScrollBar_3(ctk.CTkScrollableFrame):
    
    def __init__(self,master,title,values):
        super().__init__(master,label_text=title)
        self.grid_columnconfigure(0,weight=1)
        self.values=values
        self.checkboxes=[]
        
        for i,value in enumerate(self.values):
            checkbox=ctk.CTkCheckBox(self,text=value)
            checkbox.grid(row=i,column=0,padx=5,pady=5,sticky='ew')
            self.checkboxes.append(checkbox)
            
    def obtener(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes        
    
      # Agregamos el método get_selected_value
    def get_selected_value(self):
        return self.obtener()  # Utiliza el método existente para obtener los valores seleccionados 

        
class TrainSmart(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        self.id_registrar_entrenamiento_realizado=None
        self.id_registrar_entrenamiento_futuro=None
        self.id_seguimiento=None
        self.values_1=None
        self.values_2=None
        self.values_3=None
        self.id_cliente = None  # Inicializa el id_cliente como None
        self.usuario_caja_de_texto = ctk.CTkEntry(self)  # Campo de entrada para el usuario
        self.contraseña_caja_de_texto = ctk.CTkEntry(self, show='*')  # Campo de entrada para la contraseña
        
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_imagen()
        self.mostrar_formulario()
        self.mostrar_botones()
        self.mostrar_link_registro()
        # self.destroy()  # Cierra la ventana principal aquí
        
        
    def configurar_ventana(self):    
        self.geometry('300x500')
        self.resizable(0, 0)
        self.configure(bg='#0F1111')
        # self.destroy()
                 
    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
    
    def mostrar_imagen(self):
        # Verifica si el archivo existe
        ruta_imagen = 'C:/Users/LENOVO/OneDrive/Documentos/AppTrainSmart_GYM/Imagenes/Trainsmart.png'  # Cambia esto si necesitas una ruta absoluta
        if not os.path.isfile(ruta_imagen):
            messagebox.showerror("Error", f"No se encontró el archivo: {ruta_imagen}")
            return
        
        # Cargar la imagen desde el archivo subido
        imagen = tk.PhotoImage(file=ruta_imagen)
        
        # Redimensionar la imagen a un tamaño más pequeño
        imagen_redimensionada = imagen.subsample(3, 3)  # Ajustar la escala de la imagen
        
        # Crear un widget para mostrar la imagen redimensionada
        imagen_label = ctk.CTkLabel(self, image=imagen_redimensionada, text="")  # Dejar el texto vacío para solo mostrar la imagen
        imagen_label.image = imagen_redimensionada  # Evitar que la imagen sea recolectada por el Garbage Collector
        imagen_label.grid(row=0, column=0, padx=20, pady=(20, 10))  # Ajustar el padding superior
        
        
    
    def mostrar_formulario(self):    
        # Frame para el formulario
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.grid(row=1, column=0, padx=20, pady=(10, 10))

        # Usuario
        usuario_etiqueta = ctk.CTkLabel(self.frame_form, text='Usuario')
        usuario_etiqueta.grid(row=0, column=0, padx=10, pady=10)

        self.usuario_caja_de_texto = ctk.CTkEntry(self.frame_form)
        self.usuario_caja_de_texto.grid(row=0, column=1, padx=10, pady=10)
        
        # Contraseña
        contraseña_etiqueta = ctk.CTkLabel(self.frame_form, text='Contraseña')
        contraseña_etiqueta.grid(row=1, column=0, padx=20, pady=10)

        self.contraseña_caja_de_texto = ctk.CTkEntry(self.frame_form, show="*")  # Ocultar el texto de la contraseña
        self.contraseña_caja_de_texto.grid(row=1, column=1, padx=10, pady=10)
     
             
    def Segunda_Ventana(self, event=None):
        # Ventana para registrar el entrenamiento
        ventana_registro_de_entrenamiento = ctk.CTkToplevel(self)
        ventana_registro_de_entrenamiento.title('Registrar entrenamiento')
        ventana_registro_de_entrenamiento.geometry('300x500')  # Incrementa el tamaño de la ventana para ajustarse a las imágenes grandes.
        ventana_registro_de_entrenamiento.resizable(0, 0)
#       
        ventana_registro_de_entrenamiento.columnconfigure(0, weight=1)
        
        # BOTÓN/IMAGEN 1 - Inicia Segunda_Ventana
        # Cargar la imagen con PIL y luego convertirla a CTkImage
        imagen_original_1 = Image.open('C:/Users/LENOVO/OneDrive/Documentos/AppTrainSmart_GYM/Imagenes/1.png')
        imagen_redimensionada_1 = imagen_original_1.resize((410, 200))
        imagen_tk_1 = ImageTk.PhotoImage(imagen_redimensionada_1)
        boton_registrar_entrenamiento = ctk.CTkLabel(ventana_registro_de_entrenamiento, image=imagen_tk_1, fg_color="transparent", bg_color="transparent", text='')
        boton_registrar_entrenamiento.image = imagen_tk_1
        boton_registrar_entrenamiento.grid(row=0, column=0, padx=20, pady=(5, 10), sticky="n")  # Aumenta el espaciado y centra
        boton_registrar_entrenamiento.bind("<Button-1>", self.registrar_entrenamiento)

        # BOTÓN/IMAGEN 2 - Inicia Segunda_Ventana_2
        imagen_original_2 = Image.open('C:/Users/LENOVO/OneDrive/Documentos/AppTrainSmart_GYM/Imagenes/2.png')
        imagen_redimensionada_2 = imagen_original_2.resize((410, 200))  # Redimensionar a 300x200
        imagen_tk_2 = ImageTk.PhotoImage(imagen_redimensionada_2)
        boton_registrar_entrenamiento_futuro = ctk.CTkLabel(ventana_registro_de_entrenamiento, image=imagen_tk_2, fg_color="transparent", bg_color="transparent", text='')
        boton_registrar_entrenamiento_futuro.image = imagen_tk_2
        boton_registrar_entrenamiento_futuro.grid(row=1, column=0, padx=20, pady=(5, 10), sticky="n")  # Aumenta el espaciado
        boton_registrar_entrenamiento_futuro.bind("<Button-1>", self.registrar_entrenamiento_futuro)

        # BOTÓN/IMAGEN 3 - Inicia Segunda_Ventana_3
        imagen_original_3 = Image.open('C:/Users/LENOVO/OneDrive/Documentos/AppTrainSmart_GYM/Imagenes/3.png')
        imagen_redimensionada_3 = imagen_original_3.resize((410, 200))  # Redimensionar a 300x200
        imagen_tk_3 = ImageTk.PhotoImage(imagen_redimensionada_3)
        boton_seguimiento_registrado_anteriormente = ctk.CTkLabel(ventana_registro_de_entrenamiento, image=imagen_tk_3, fg_color='transparent', bg_color='transparent', text='')
        boton_seguimiento_registrado_anteriormente.image = imagen_tk_3
        boton_seguimiento_registrado_anteriormente.grid(row=2, column=0, padx=20, pady=(5, 10), sticky="n")  # Ajustar espaciado
        boton_seguimiento_registrado_anteriormente.bind("<Button-1>", self.seguimiento_registrado_anteriormente)
        
    def mostrar_botones(self):
        
        # Botón de "Iniciar Sesión"
        login_boton = ctk.CTkLabel(self, text='Iniciar sesión', text_color='blue', cursor='hand2', bg_color='black')
        login_boton.grid(row=2, column=0, padx=20, pady=(10, 5))

        # Vincular el clic del botón con la función loguarse_y_guardar_cliente_en_la_bd
        login_boton.bind('<Button-1>', lambda event: self.loguarse_y_guardar_cliente_en_la_bd())

    def loguarse_y_guardar_cliente_en_la_bd(self):
        
        usuario = self.usuario_caja_de_texto.get()
        contraseña = self.contraseña_caja_de_texto.get()

        if not usuario or not contraseña:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return

    # Aquí se verifica si el usuario ya está registrado
        if ClienteDAO_GYM_1.validar_usuario(usuario, contraseña):
            self.id_cliente = usuario  # Suponiendo que el usuario tiene un ID único
            messagebox.showinfo("Inicio de Sesión", f"Usuario {usuario} inició sesión exitosamente.")
            self.Segunda_Ventana()            
            self.withdraw()
            
        else:
            # Si las credenciales son incorrectas, verificamos si el usuario existe
            if ClienteDAO_GYM_1.usuario_existe(usuario):
                messagebox.showerror("Error", "Credenciales incorrectas. Por favor, intenta nuevamente.")
            else:
                messagebox.showinfo("Información", f"El usuario {usuario} no está registrado en la base de datos.")

    
    def registrar_entrenamiento(self, event=None):
        # Creamos ventana para el primer botón
        ventana_del_primer_boton = ctk.CTkToplevel(self)
        ventana_del_primer_boton.title('Registrar entrenamiento realizado')

        # Ajustamos el tamaño de la ventana para que sea más compacto
        ventana_del_primer_boton.geometry('300x500')  

        # Hacemos que las columnas y filas se ajusten para que ocupen todo el espacio disponible
        ventana_del_primer_boton.columnconfigure(0, weight=1)
        ventana_del_primer_boton.rowconfigure([0, 1, 2], weight=1)

        # Agregar ScrollBar dentro de la ventana del primer botón
        values_1 = ["Cardio", "Fuerza", "Flexibilidad"]
        self.scrollable_checkbox_frame = ScrollBar_1(ventana_del_primer_boton, title="Tipo de Ejercicio", values=values_1)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=3, pady=5, sticky="nsew")

        values_2 = ['Pecho', 'Espalda', 'Piernas', 'Hombros', 'Bíceps', 'Tríceps']
        self.scrollable_checkbox_frame_2 = ScrollBar_2(ventana_del_primer_boton, title='Grupo muscular trabajado', values=values_2)
        self.scrollable_checkbox_frame_2.grid(row=1, column=0, padx=3, pady=5, sticky="nsew")

        values_3 = ['25m', '30m', '40m', '45m', '1h', '2h']
        self.scrollable_checkbox_frame_3 = ScrollBar_3(ventana_del_primer_boton, title='Duración del entrenamiento', values=values_3)
        self.scrollable_checkbox_frame_3.grid(row=2, column=0, padx=3, pady=5, sticky="nsew")

        # BOTON PARA ENVIAR COMPLETO EL FORMULARIO  
        self.button = ctk.CTkButton(ventana_del_primer_boton, text="Enviar", command=self.enviar_registro_realizado)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
    
    def enviar_registro_realizado(self):
        # Obtiene los valores de cada scrollable checkbox
        valor_1 = self.scrollable_checkbox_frame.get_selected_value()  # Tipo de ejercicio
        valor_2 = self.scrollable_checkbox_frame_2.get_selected_value()  # Grupo muscular trabajado
        valor_3 = self.scrollable_checkbox_frame_3.get_selected_value()  # Duración del entrenamiento

        # Verifica si se han seleccionado todos los campos
        if not valor_1 or not valor_2 or not valor_3:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")
            return  

        # Crear un diccionario con los datos a guardar
        entrenamiento_realizado = {
            "tipo_de_ejercicio": valor_1,
            "grupo_muscular_trabajado": valor_2,
            "duracion_del_entrenamiento": valor_3
        }
        
        # Insertar en la base de datos
        resultado = Registrar_Entrenamiento_RealizadoDAO.insertar_bd(entrenamiento_realizado)
        
        if resultado:  # Verifica que la inserción fue exitosa
            messagebox.showinfo("Éxito", "Entrenamiento registrado correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo registrar el entrenamiento.")    
            
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
        self.button = ctk.CTkButton(ventana_del_primer_boton, text="my button", command=self.enviar_registro_futuro)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
       
       
    def enviar_registro_futuro(self):
        
        # Obtienes los valores de cada scrollable checkbox
        valor_1=self.scrollable_checkbox_frame.get_selected_value()
        valor_2=self.scrollable_checkbox_frame_2.get_selected_value()
        valor_3=self.scrollable_checkbox_frame_3.get_selected_value()
        
        
        # Verifica si se han seleccionado todos los campos
        if not valor_1 or not valor_2 or not valor_3:
            messagebox.showerror('Error','Por favor, completa todo los campos')
            return
        
        # Creamos un diccionario con los datos a guardar
        
        entrenamiento_futuro={
            'tipo_de_ejercicio':valor_1,
            'duracion_estimada_del_entrenamiento':valor_2,
            'objetivo_del_entrenamiento':valor_3
        }
        
        resultado=Registrar_FuturoDAO.insertar_bd(entrenamiento_futuro)
         
        if resultado:
            messagebox.showinfo('Exito','Entrenamiento futuro registrado correctamente')
        else:
            messagebox.showerror('Error','No se pudo registrar el entrenamiento futuro') 
        
       
           
    def seguimiento_registrado_anteriormente(self, event=None):
        
        
        # Crear ventana para mostrar entrenamientos
        ventana_seguimiento = ctk.CTkToplevel(self)
        ventana_seguimiento.title('Entrenamientos Registrados')
        ventana_seguimiento.geometry('300x500')

        # Hacer que las columnas y filas se ajusten
        ventana_seguimiento.columnconfigure(0, weight=1)
        ventana_seguimiento.rowconfigure([0, 1], weight=1)



    def editar_entrenamiento(self):
        pass

    def guardar_cambios(self, index, tipo, duracion, grupo, ventana):
        pass  

    def eliminar_entrenamiento(self):
        pass
              
    
        
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

    def registrar_nuevo_usuario(self, nombre_entry, usuario_entry, contraseña_entry):
        # Aquí iría la lógica de registrar al usuario
        nombre = nombre_entry.get()
        usuario = usuario_entry.get()
        contraseña = contraseña_entry.get()
        
        if not nombre or not usuario or not contraseña:
            messagebox.showerror("Error", "Por favor, completa todos los campos.")  
            return
        
        # Validamos el valor del self.id_cliente 
        if self.id_cliente is None:
            cliente=Cliente_1(nombre=nombre, usuario=usuario, contraseña=contraseña)
            ClienteDAO_GYM_1.insertar_bd(cliente)
            messagebox.showinfo("Registro", f"Usuario {usuario} registrado exitosamente")
        elif usuario == usuario:
            messagebox.showinfo("Registro", f"Usuario {usuario} ya registrado!!")
         
            
    
if __name__ == "__main__":
    
    app = TrainSmart()
    app.mainloop()
