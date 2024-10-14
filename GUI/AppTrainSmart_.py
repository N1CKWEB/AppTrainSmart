import customtkinter as ctk
from customtkinter import CTkImage
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage, Image
from PIL import Image, ImageTk
import os

class TrainSmart(ctk.CTk):
    
    def __init__(self):
        super().__init__()
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
        # Verifica si el archivo existe
        ruta_imagen = 'Trainsmart.png'  # Cambia esto si necesitas una ruta absoluta
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

        # Nombre
        usuario_etiqueta = ctk.CTkLabel(self.frame_form, text='Usuario')
        usuario_etiqueta.grid(row=0, column=0, padx=10, pady=10)

        self.usuario_caja_de_texto = ctk.CTkEntry(self.frame_form)
        self.usuario_caja_de_texto.grid(row=0, column=1, padx=10, pady=10)
        
        # Contraseña
        contraseña_etiqueta = ctk.CTkLabel(self.frame_form, text='Contraseña')
        contraseña_etiqueta.grid(row=1, column=0, padx=20, pady=10)

        self.contraseña_caja_de_texto = ctk.CTkEntry(self.frame_form, show="*")  # Ocultar el texto de la contraseña
        self.contraseña_caja_de_texto.grid(row=1, column=1, padx=10, pady=10)
        
    def mostrar_botones(self):
        # Botón de "Iniciar Sesión"
        login_boton = ctk.CTkLabel(self, text='Iniciar sesión', text_color='blue', cursor='hand2', bg_color='black')
        login_boton.grid(row=2, column=0, padx=20, pady=(10, 5))

        # Vincular el clic del botón con la función loguarse
        login_boton.bind('<Button-1>', self.loguarse)

    def loguarse(self, event=None):
        # Ventana para registrar el entrenamiento
        ventana_registro_de_entrenamiento = ctk.CTkToplevel(self)
        ventana_registro_de_entrenamiento.title('Registrar entrenamiento')
        ventana_registro_de_entrenamiento.geometry('300x500')  # Incrementa el tamaño de la ventana para ajustarse a las imágenes grandes.

        ventana_registro_de_entrenamiento.columnconfigure(0, weight=1)
        # BOTÓN/IMAGEN 1 - Inicia loguarse
        imagen_original_1 = Image.open('1.png')
        imagen_redimensionada_1 = imagen_original_1.resize((410, 200))  # Redimensionar a 300x200
        imagen_tk_1 = ImageTk.PhotoImage(imagen_redimensionada_1)
        boton_registrar_entrenamiento = ctk.CTkLabel(ventana_registro_de_entrenamiento, image=imagen_tk_1, fg_color="transparent", bg_color="transparent", text='')
        boton_registrar_entrenamiento.image = imagen_tk_1
        boton_registrar_entrenamiento.grid(row=0, column=0, padx=20, pady=(5, 10), sticky="n")  # Aumenta el espaciado y centra
        boton_registrar_entrenamiento.bind("<Button-1>", self.loguarse)

        # BOTÓN/IMAGEN 2 - Inicia loguarse_2
        imagen_original_2 = Image.open('2.png')
        imagen_redimensionada_2 = imagen_original_2.resize((410, 200))  # Redimensionar a 300x200
        imagen_tk_2 = ImageTk.PhotoImage(imagen_redimensionada_2)
        boton_registrar_entrenamiento_futuro = ctk.CTkLabel(ventana_registro_de_entrenamiento, image=imagen_tk_2, fg_color="transparent", bg_color="transparent", text='')
        boton_registrar_entrenamiento_futuro.image = imagen_tk_2
        boton_registrar_entrenamiento_futuro.grid(row=1, column=0, padx=20, pady=(5, 10), sticky="n")  # Aumenta el espaciado
        boton_registrar_entrenamiento_futuro.bind("<Button-1>", self.loguarse_2)

        # BOTÓN/IMAGEN 3 - Inicia loguarse_3
        imagen_original_3 = Image.open('3.png')
        imagen_redimensionada_3 = imagen_original_3.resize((410, 200))  # Redimensionar a 300x200
        imagen_tk_3 = ImageTk.PhotoImage(imagen_redimensionada_3)
        boton_seguimiento_registrado_anteriormente = ctk.CTkLabel(ventana_registro_de_entrenamiento, image=imagen_tk_3, fg_color='transparent', bg_color='transparent', text='')
        boton_seguimiento_registrado_anteriormente.image = imagen_tk_3
        boton_seguimiento_registrado_anteriormente.grid(row=2, column=0, padx=20, pady=(5, 10), sticky="n")  # Ajustar espaciado
        boton_seguimiento_registrado_anteriormente.bind("<Button-1>", self.mostrar_boton_seguimiento_registrado_anteriormente)

    def mostrar_boton_seguimiento_registrado_anteriormente(self, event=None):
        print('Funcion loguarse_3 ejecutada')

    def loguarse_2(self, event=None):
        # Código para manejar el evento del segundo botón
        print("Función loguarse_2 ejecutada")

            # Llamar a las funciones para mostrar los botones
        
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
        registrar_boton = ctk.CTkButton(ventana_registro, text="Registrar", command=lambda: self.registrar_usuario(nombre_entry, usuario_entry, contraseña_entry))
        registrar_boton.grid(row=7, column=0, padx=10, pady=20, sticky="s")

    def registrar_usuario(self, nombre_entry, usuario_entry, contraseña_entry):
        # Aquí iría la lógica de registrar al usuario
        nombre = nombre_entry.get()
        usuario = usuario_entry.get()
        contraseña = contraseña_entry.get()
        messagebox.showinfo("Registro", f"Usuario {usuario} registrado exitosamente")
    
    
    
if __name__ == "__main__":
    app = TrainSmart()
    app.mainloop()
