

class Registrar_Entrenamiento_Futuro:
    
    def __init__(self, id_registrar_entrenamiento_futuro=None,
                 tipo_de_ejercicio=None, duracion_estimada_del_entrenamiento=None,
                 objetivo_del_entrenamiento=None):
        
        self._id_registrar_entrenamiento_futuro = id_registrar_entrenamiento_futuro
        self._tipo_de_ejercicio = tipo_de_ejercicio
        self._duracion_estimada_del_entrenamiento = duracion_estimada_del_entrenamiento
        self._objetivo_del_entrenamiento = objetivo_del_entrenamiento
      
    @property
    def id_registrar_entrenamiento_futuro(self):
        return self._id_registrar_entrenamiento_futuro
    
    @id_registrar_entrenamiento_futuro.setter
    def id_registrar_entrenamiento_futuro(self, id_registrar_entrenamiento_futuro):
        self._id_registrar_entrenamiento_futuro = id_registrar_entrenamiento_futuro
        
    @property
    def tipo_de_ejercicio(self):
        return self._tipo_de_ejercicio
    
    @tipo_de_ejercicio.setter
    def tipo_de_ejercicio(self, tipo_de_ejercicio):
        self._tipo_de_ejercicio = tipo_de_ejercicio
        
    @property
    def duracion_estimada_del_entrenamiento(self):
        return self._duracion_estimada_del_entrenamiento
    
    @duracion_estimada_del_entrenamiento.setter
    def duracion_estimada_del_entrenamiento(self, duracion_estimada_del_entrenamiento):
        self._duracion_estimada_del_entrenamiento = duracion_estimada_del_entrenamiento
        
    @property
    def objetivo_del_entrenamiento(self):
        return self._objetivo_del_entrenamiento
    
    @objetivo_del_entrenamiento.setter
    def objetivo_del_entrenamiento(self, objetivo_del_entrenamiento):
        self._objetivo_del_entrenamiento = objetivo_del_entrenamiento
    
    def __str__(self):  
        return f"Id: {self.id_registrar_entrenamiento_futuro}, Tipo de Ejercicio: {self.tipo_de_ejercicio}, Duración estimada del entrenamiento: {self.duracion_estimada_del_entrenamiento}, Objetivo del entrenamiento: {self.objetivo_del_entrenamiento}" 

if __name__ == "__main__":  
    cliente = Registrar_Entrenamiento_Futuro(id_registrar_entrenamiento_futuro=1, tipo_de_ejercicio='Cardio', duracion_estimada_del_entrenamiento=30, objetivo_del_entrenamiento='Mejorar resistencia')
    print(cliente)
