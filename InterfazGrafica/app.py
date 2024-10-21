import customtkinter as ctk

# Función para guardar el entrenamiento
def guardar_entrenamiento():
    fecha = entry_fecha.get()
    tipo = option_tipo.get()
    duracion = int(slider_duracion.get())
    
    print(f"Fecha: {fecha}, Tipo: {tipo}, Duración: {duracion} minutos")
    # Aquí iría la lógica para guardar en la base de datos o mostrar en pantalla

# Configuración básica de la ventana
ctk.set_appearance_mode("dark")  # Modo oscuro opcional
ctk.set_default_color_theme("blue")  # Tema de color opcional

root = ctk.CTk()  # Crear ventana principal
root.title("Formulario de Entrenamiento Futuro")
root.geometry("400x500")  # Ajustar el tamaño de la ventana

# Frame con scrollbar
scrollable_frame = ctk.CTkScrollableFrame(root, width=380, height=300)
scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Etiqueta de título
label = ctk.CTkLabel(scrollable_frame, text="Registrar Entrenamiento Futuro", font=("Arial", 16))
label.pack(pady=10)

# Campo para ingresar la fecha
label_fecha = ctk.CTkLabel(scrollable_frame, text="Fecha del Entrenamiento")
label_fecha.pack(pady=5)
entry_fecha = ctk.CTkEntry(scrollable_frame, placeholder_text="DD/MM/AAAA")
entry_fecha.pack(pady=5)

# Opción desplegable para seleccionar el tipo de ejercicio
label_tipo = ctk.CTkLabel(scrollable_frame, text="Tipo de Ejercicio")
label_tipo.pack(pady=5)
option_tipo = ctk.CTkOptionMenu(scrollable_frame, values=["Cardio", "Fuerza", "Flexibilidad", "Otro"])
option_tipo.pack(pady=5)

# Slider para seleccionar la duración del entrenamiento
label_duracion = ctk.CTkLabel(scrollable_frame, text="Duración (minutos)")
label_duracion.pack(pady=5)

slider_duracion = ctk.CTkSlider(scrollable_frame, from_=10, to=180, number_of_steps=17)
slider_duracion.set(30)  # Valor inicial en 30 minutos
slider_duracion.pack(pady=5)

# Botón para guardar el entrenamiento
boton_guardar = ctk.CTkButton(root, text="Guardar Entrenamiento", command=guardar_entrenamiento)
boton_guardar.pack(pady=20)

# Iniciar la aplicación
root.mainloop()


    #  # Tipo de ejercicio
    #  # # label_tipo_1 = ctk.CTkLabel(ventana_del_primer_boton, text="Tipo de Ejercicio")
    # # label_tipo_1.pack(pady=5)
    #  opciones_1 = ctk.CTkOptionMenu(ventana_del_primer_boton, values=["Cardio", "Fuerza", "Flexibilidad", "Otro"])
    #  opciones_1.pack(pady=5)
    
    #  # Musculo trabajado
    #   label_tipo_2=ctk.CTkLabel(ventana_del_primer_boton,text='Musculo Trabajado')
    #   label_tipo_2.pack(pady=5)
    #   opciones_2=ctk.CTkOptionMenu(ventana_del_primer_boton,values=['Pecho','Triceps','Biceps','Espalda','Piernas','Hombros','Brazos'])
                
      