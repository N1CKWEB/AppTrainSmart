

class Registrar_Entrenamiento:
    
    def __init__(self,id_registrar_entrenamiento_realizado=None,tipo_de_ejercicio=None,grupo_muscular_trabajado=None,duracion_del_entrenamiento=None):
        
        self.id_registrar_entrenamiento_realizado=id_registrar_entrenamiento_realizado
        self.tipo_de_ejercicio=tipo_de_ejercicio
        self.grupo_muscular_trabajado=grupo_muscular_trabajado
        self.duracion_del_entrenamiento=duracion_del_entrenamiento

    
    @property
    def id_registrar_entrenamiento_realizado(self):
        return self._id_registrar_entrenamiento_realizado
    
    @id_registrar_entrenamiento_realizado.setter
    def id_registrar_entrenamiento_realizado(self, id_registrar_entrenamiento_realizado):
        self._id_registrar_entrenamiento_realizado = id_registrar_entrenamiento_realizado

    @property
    def tipo_de_ejercicio(self):
        return self._tipo_de_ejercicio

    @tipo_de_ejercicio.setter
    def tipo_de_ejercicio(self, tipo_de_ejercicio):
        self._tipo_de_ejercicio = tipo_de_ejercicio

    @property
    def grupo_muscular_trabajado(self):
        return self._grupo_muscular_trabajado

    @grupo_muscular_trabajado.setter
    def grupo_muscular_trabajado(self, grupo_muscular_trabajado):
        self._grupo_muscular_trabajado = grupo_muscular_trabajado

    @property
    def duracion_del_entrenamiento(self):
        return self._duracion_del_entrenamiento

    @duracion_del_entrenamiento.setter
    def duracion_del_entrenamiento(self, duracion_del_entrenamiento):
        self._duracion_del_entrenamiento = duracion_del_entrenamiento
    
    def __str__(self):
        return (f'Id: {self.id_registrar_entrenamiento_realizado}, Tipo de Ejercicio: {self.tipo_de_ejercicio}, Grupo Muscular Trabajado: {self.grupo_muscular_trabajado}, Duración del Entrenamiento: {self.duracion_del_entrenamiento}')
    
    
    
if __name__ == "__main__":
    cliente=Registrar_Entrenamiento(id_registrar_entrenamiento_realizado=1,tipo_de_ejercicio='Cardio',grupo_muscular_trabajado='Pecho',duracion_del_entrenamiento=30)
    print(cliente)