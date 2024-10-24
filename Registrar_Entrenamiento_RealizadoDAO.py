from Conexion import Conexion_1
from Cursor_del_pool import CursorDelPool_1
from Cliente_GYM import Cliente_1
from Registrar_Entrenamiento import Registrar_Entrenamiento
from Logger_base import log  # Importación absoluta


class Registrar_Entrenamiento_RealizadoDAO:
    
    _SELECCIONAR = "SELECT * FROM Registrar_Entrenamiento_Realizado WHERE id_registrar_entrenamiento_realizado=%s"
    _INSERTAR = "INSERT INTO Registrar_Entrenamiento_Realizado (tipo_de_ejercicio, grupo_muscular_trabajado, duracion_del_entrenamiento) VALUES (%s, %s, %s)"
    _UPDATE = "UPDATE Registrar_Entrenamiento_Realizado SET tipo_de_ejercicio=%s, grupo_muscular_trabajado=%s, duracion_del_entrenamiento=%s WHERE id_registrar_entrenamiento_realizado=%s"
    _DELETE = "DELETE FROM Registrar_Entrenamiento_Realizado WHERE id_registrar_entrenamiento_realizado=%s"
    _VALIDAR_ENTRENAMIENTO = "SELECT * FROM Registrar_Entrenamiento_Realizado WHERE tipo_de_ejercicio=%s AND grupo_muscular_trabajado=%s AND duracion_del_entrenamiento=%s"

    @classmethod
    def seleccionar_bd(cls, id_registrar_entrenamiento_realizado):
        try:
            with CursorDelPool_1() as cursor:
                cursor.execute(cls._SELECCIONAR, (id_registrar_entrenamiento_realizado,))
                registros = cursor.fetchall()
                entrenamientos = []
                for registro in registros:
                    # Crear un diccionario similar a la estructura utilizada en el método insertar_bd
                    entrenamiento = {
                        "id_registrar_entrenamiento_realizado": registro[0],
                        "tipo_de_ejercicio": registro[1],
                        "grupo_muscular_trabajado": registro[2],
                        "duracion_del_entrenamiento": registro[3]
                    }
                    entrenamientos.append(entrenamiento)
                log.debug(f"Entrenamientos seleccionados: {entrenamientos}")
                return entrenamientos
        except Exception as e:
            log.error(f"Error al seleccionar entrenamiento: {e}")
            return None
    

    @classmethod
    def insertar_bd(cls, entrenamiento):
        try:
            with CursorDelPool_1() as cursor:
                valores = (
                    entrenamiento["tipo_de_ejercicio"],
                    entrenamiento["grupo_muscular_trabajado"],
                    entrenamiento["duracion_del_entrenamiento"]
                )
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f"Entrenamiento registrado: {entrenamiento}")
                return cursor.rowcount
        except Exception as e:
            log.error(f"Error al insertar entrenamiento: {e}")
            return 0
        
    @classmethod
    def actualizar_bd(cls, entrenamiento):
        try:
            with CursorDelPool_1() as cursor:
                valores = (
                    entrenamiento.tipo_de_ejercicio,
                    entrenamiento.grupo_muscular_trabajado,
                    entrenamiento.duracion_del_entrenamiento,
                    entrenamiento.id_registrar_entrenamiento_realizado
                )
                cursor.execute(cls._UPDATE, valores)
                log.debug(f"Entrenamiento actualizado: {entrenamiento}")
                return cursor.rowcount
        except Exception as e:
            log.error(f"Error al actualizar entrenamiento: {e}")
            return None

    @classmethod
    def eliminar_bd(cls, entrenamiento):
        try:
            with CursorDelPool_1() as cursor:
                cursor.execute(cls._DELETE, (entrenamiento.id_registrar_entrenamiento_realizado,))
                log.debug(f"Entrenamiento eliminado con id: {entrenamiento.id_registrar_entrenamiento_realizado}")
                return cursor.rowcount
        except Exception as e:
            log.error(f"Error al eliminar entrenamiento: {e}")
            return None
        
    @classmethod
    def validar_entrenamiento_realizado(cls, tipo_de_ejercicio, grupo_muscular_trabajado, duracion_del_entrenamiento):
        try:
            with CursorDelPool_1() as cursor:
                cursor.execute(cls._VALIDAR_ENTRENAMIENTO, (tipo_de_ejercicio, grupo_muscular_trabajado, duracion_del_entrenamiento))
                resultado = cursor.fetchone()
                if resultado:
                    return Registrar_Entrenamiento(
                        id_registrar_entrenamiento_realizado=resultado[0],
                        tipo_de_ejercicio=resultado[1],
                        grupo_muscular_trabajado=resultado[2],
                        duracion_del_entrenamiento=resultado[3]
                    )
                return None
        except Exception as e:
            log.error(f"Error al validar entrenamiento: {e}")
            return None


if __name__ == "__main__":
    # Ejemplo de inserción de entrenamiento
    nuevo_entrenamiento = Registrar_Entrenamiento(
        # tipo_de_ejercicio="Fuerza",
        grupo_muscular_trabajado="Espalda",
        duracion_del_entrenamiento="30"
    )
    nuevo_entrenamiento_2=Registrar_Entrenamiento()
    
    entrenamiento_insertado = Registrar_Entrenamiento_RealizadoDAO.seleccionar_bd(nuevo_entrenamiento) 
    log.info(f"Entrenamiento insertado: {entrenamiento_insertado}")

    entrenamiento_seleccionado=Registrar_Entrenamiento_RealizadoDAO.seleccionar_bd(nuevo_entrenamiento)
    log.info(f"Entrenamiento seleccionado: {entrenamiento_seleccionado}")