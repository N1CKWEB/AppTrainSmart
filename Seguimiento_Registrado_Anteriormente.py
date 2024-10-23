from Registrar_Entrenamiento import Registrar_Entrenamiento
from Registrar_Entrenamiento_Futuro import Registrar_Entrenamiento_Futuro
from datetime import date

class Seguimiento_Registrado_Anteriormente(Registrar_Entrenamiento, Registrar_Entrenamiento_Futuro):
    
    def __init__(self, id_seguimiento=None, id_registrar_entrenamiento_realizado=None, tipo_de_ejercicio_realizado=None,
                 grupo_muscular_trabajado=None, duracion_del_entrenamiento=None, id_registrar_entrenamiento_futuro=None,
                 tipo_de_ejercicio_futuro=None, duracion_estimada_del_entrenamiento=None, objetivo_del_entrenamiento=None,
                 fecha_seguimiento=None, comentarios=None):
        
        # Inicializamos la clase base Registrar_Entrenamiento
        Registrar_Entrenamiento.__init__(self, id_registrar_entrenamiento_realizado, tipo_de_ejercicio_realizado, 
                                         grupo_muscular_trabajado, duracion_del_entrenamiento)
        
        # Inicializamos la clase base Registrar_Entrenamiento_Futuro
        Registrar_Entrenamiento_Futuro.__init__(self, id_registrar_entrenamiento_futuro, tipo_de_ejercicio_futuro, 
                                                duracion_estimada_del_entrenamiento, objetivo_del_entrenamiento)
        
        # Nuevos atributos para la clase Seguimiento
        self.id_seguimiento = id_seguimiento
        self.fecha_seguimiento = fecha_seguimiento if fecha_seguimiento else date.today()  # Por defecto, fecha actual
        self.comentarios = comentarios if comentarios else "Sin comentarios"
    
    def __str__(self):
        # Combina la información de las clases base con la nueva información
        return (f"ID Seguimiento: {self.id_seguimiento}\n"
                f"Entrenamiento Realizado -> {Registrar_Entrenamiento.__str__(self)}\n"
                f"Entrenamiento Futuro -> {Registrar_Entrenamiento_Futuro.__str__(self)}\n"
                f"Fecha de Seguimiento: {self.fecha_seguimiento}\n"
                f"Comentarios: {self.comentarios}")

if __name__ == "__main__":
    
    seguimiento = Seguimiento_Registrado_Anteriormente(
        id_seguimiento=1,
        id_registrar_entrenamiento_realizado=1, tipo_de_ejercicio_realizado='Cardio',
        grupo_muscular_trabajado='Pecho', duracion_del_entrenamiento=45,
        id_registrar_entrenamiento_futuro=2, tipo_de_ejercicio_futuro='Fuerza',
        duracion_estimada_del_entrenamiento=30, objetivo_del_entrenamiento='Mejorar resistencia',
        fecha_seguimiento=date(2024, 10, 23), comentarios="Buen progreso, mantener la intensidad"
    )
    
    print(seguimiento)
