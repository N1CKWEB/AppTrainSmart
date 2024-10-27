import customtkinter as ctk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from Registrar_Entrenamiento_RealizadoDAO import Registrar_Entrenamiento_RealizadoDAO

class TrainSmart(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TrainSmart")
        self.geometry('300x500')
        self.configure(fg_color='#0F1111')
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.mostrar_imagen()
        self.mostrar_formulario()
        self.mostrar_botones()
        self.mostrar_link_registro()

    def mostrar_imagen(self):
        ruta_imagen = 'C:/Users/LENOVO/OneDrive/Documentos/AppTrainSmart_GYM/Imagenes/Trainsmart.png'
        if not os.path.isfile(ruta_imagen):
            messagebox.showerror("Error", f"No se encontró el archivo: {ruta_imagen}")
            return
        
        imagen = Image.open(ruta_imagen)
        imagen_redimensionada = imagen.resize((100, 100))  # Ajusta el tamaño según necesites
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
        
        imagen_label = ctk.CTkLabel(self, image=imagen_tk, text="")
        imagen_label.image = imagen_tk
        imagen_label.grid(row=0, column=0, padx=20, pady=(20, 10))

    def mostrar_formulario(self):
        self.frame_form = ctk.CTkFrame(self)
        self.frame_form.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="nsew")

        ctk.CTkLabel(self.frame_form, text='Usuario').grid(row=0, column=0, padx=10, pady=10)
        self.usuario_entry = ctk.CTkEntry(self.frame_form)
        self.usuario_entry.grid(row=0, column=1, padx=10, pady=10)
        
        ctk.CTkLabel(self.frame_form, text='Contraseña').grid(row=1, column=0, padx=10, pady=10)
        self.contraseña_entry = ctk.CTkEntry(self.frame_form, show="*")
        self.contraseña_entry.grid(row=1, column=1, padx=10, pady=10)

    def mostrar_botones(self):
        login_boton = ctk.CTkButton(self, text='Iniciar sesión', command=self.loguarse_y_guardar_cliente_en_la_bd)
        login_boton.grid(row=2, column=0, padx=20, pady=(10, 5))

    def loguarse_y_guardar_cliente_en_la_bd(self):
        # Aquí iría la lógica de autenticación
        self.Segunda_Ventana()

    def Segunda_Ventana(self):
        ventana_registro_de_entrenamiento = ctk.CTkToplevel(self)
        ventana_registro_de_entrenamiento.title('Registrar entrenamiento')
        ventana_registro_de_entrenamiento.geometry('300x500')
        ventana_registro_de_entrenamiento.configure(fg_color='#0F1111')

        ctk.CTkButton(ventana_registro_de_entrenamiento, text="Ver Entrenamientos", command=self.mostrar_entrenamientos).pack(pady=20)

    def mostrar_entrenamientos(self):
        entrenamientos_window = ctk.CTkToplevel(self)
        entrenamientos_window.title("Entrenamientos Registrados")
        entrenamientos_window.geometry('600x400')
        entrenamientos_window.configure(fg_color='#0F1111')

        # Crear un frame para contener el Treeview y la scrollbar
        frame = ctk.CTkFrame(entrenamientos_window)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Crear un Treeview con estilo personalizado
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
                        background="#2a2d2e", 
                        foreground="white", 
                        rowheight=25, 
                        fieldbackground="#2a2d2e", 
                        bordercolor="#343638",
                        borderwidth=0)
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",
                        background="#565b5e", 
                        foreground="white", 
                        relief="flat")
        style.map("Treeview.Heading",
                  background=[('active', '#3484F0')])

        tree = ttk.Treeview(frame, columns=("ID", "Tipo", "Grupos Musculares", "Duración"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Tipo", text="Tipo de Ejercicio")
        tree.heading("Grupos Musculares", text="Grupos Musculares")
        tree.heading("Duración", text="Duración (min)")

        # Configurar las columnas para que se ajusten al contenido
        tree.column("ID", width=50)
        tree.column("Tipo", width=150)
        tree.column("Grupos Musculares", width=200)
        tree.column("Duración", width=100)

        # Agregar scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(fill="both", expand=True)

        # Insertar datos en el Treeview
        entrenamientos = Registrar_Entrenamiento_RealizadoDAO.seleccionar_bd(None)
        for entrenamiento in entrenamientos:
            tree.insert("", "end", values=(
                entrenamiento["id_registrar_entrenamiento_realizado"],
                entrenamiento["tipo_de_ejercicio"],
                entrenamiento["grupo_muscular_trabajado"],
                entrenamiento["duracion_del_entrenamiento"]
            ))

        # Frame para los botones
        button_frame = ctk.CTkFrame(entrenamientos_window)
        button_frame.pack(fill="x", padx=10, pady=10)

        # Botones de editar y eliminar
        ctk.CTkButton(button_frame, text="Editar", command=lambda: self.editar_entrenamiento(tree)).pack(side="left", padx=5)
        ctk.CTkButton(button_frame, text="Eliminar", command=lambda: self.eliminar_entrenamiento(tree)).pack(side="left", padx=5)

    def editar_entrenamiento(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un entrenamiento para editar.")
            return

        item = tree.item(selected_item)
        id_entrenamiento = item['values'][0]

        # Aquí creas una nueva ventana para editar el entrenamiento
        editar_window = ctk.CTkToplevel(self)
        editar_window.title("Editar Entrenamiento")
        editar_window.geometry('300x500')
        editar_window.configure(fg_color='#0F1111')

        ctk.CTkLabel(editar_window, text="Tipo de Ejercicio").pack(pady=5)
        tipo_entry = ctk.CTkEntry(editar_window)
        tipo_entry.pack(pady=5)
        tipo_entry.insert(0, item['values'][1])

        ctk.CTkLabel(editar_window, text="Grupos Musculares").pack(pady=5)
        grupos_entry = ctk.CTkEntry(editar_window)
        grupos_entry.pack(pady=5)
        grupos_entry.insert(0, item['values'][2])

        ctk.CTkLabel(editar_window, text="Duración").pack(pady=5)
        duracion_entry = ctk.CTkEntry(editar_window)
        duracion_entry.pack(pady=5)
        duracion_entry.insert(0, item['values'][3])

        ctk.CTkButton(editar_window, text="Guardar Cambios", command=lambda: self.guardar_cambios_entrenamiento(
            id_entrenamiento, 
            tipo_entry.get(), 
            grupos_entry.get(), 
            duracion_entry.get(), 
            editar_window, 
            tree
        )).pack(pady=20)

    def guardar_cambios_entrenamiento(self, id_entrenamiento, tipo, grupos, duracion, ventana, tree):
        # Aquí actualizarías la base de datos
        entrenamiento_actualizado = {
            "id_registrar_entrenamiento_realizado": id_entrenamiento,
            "tipo_de_ejercicio": tipo,
            "grupo_muscular_trabajado": grupos,
            "duracion_del_entrenamiento": duracion
        }
        resultado = Registrar_Entrenamiento_RealizadoDAO.actualizar_bd(entrenamiento_actualizado)
        if resultado:
            messagebox.showinfo("Éxito", "Entrenamiento actualizado correctamente")
            ventana.destroy()
            self.actualizar_treeview(tree)
        else:
            messagebox.showerror("Error", "No se pudo actualizar el entrenamiento")

    def eliminar_entrenamiento(self, tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un entrenamiento para eliminar.")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de que desea eliminar este entrenamiento?"):
            item = tree.item(selected_item)
            id_entrenamiento = item['values'][0]
            
            # Aquí eliminarías de la base de datos
            resultado = Registrar_Entrenamiento_RealizadoDAO.eliminar_bd({"id_registrar_entrenamiento_realizado": id_entrenamiento})
            if resultado:
                tree.delete(selected_item)
                messagebox.showinfo("Éxito", "Entrenamiento eliminado correctamente")
            else:
                messagebox.showerror("Error", "No se pudo eliminar el entrenamiento")

    def actualizar_treeview(self, tree):
        # Limpiar el Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Volver a cargar los datos
        entrenamientos = Registrar_Entrenamiento_RealizadoDAO.seleccionar_bd(None)
        for entrenamiento in entrenamientos:
            tree.insert("", "end", values=(
                entrenamiento["id_registrar_entrenamiento_realizado"],
                entrenamiento["tipo_de_ejercicio"],
                entrenamiento["grupo_muscular_trabajado"],
                entrenamiento["duracion_del_entrenamiento"]
            ))

    def mostrar_link_registro(self):
        registro_link = ctk.CTkLabel(self, text="Si no tienes cuenta, regístrate", text_color="blue", cursor="hand2")
        registro_link.grid(row=3, column=0, padx=20, pady=5)
        registro_link.bind("<Button-1>", self.abrir_ventana_registro)

    def abrir_ventana_registro(self, event=None):
        # Implementación de la ventana de registro (similar a tu código original)
        pass

if __name__ == "__main__":
    app = TrainSmart()
    app.mainloop()