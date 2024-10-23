
from Conexion import Conexion_1
from Cursor_del_pool import CursorDelPool_1
from Cliente_GYM import Cliente_1
from Registrar_Entrenamiento import Registrar_Entrenamiento
from Logger_base import log  # Importación absoluta


class Registrar_Entrenamiento_RealizadoDAO:
    
    _SELECCIONAR="SELECT * FROM Registrar_Entrenamiento_Realizado WHERE id_registrar_entrenamiento_realizado=%s"
    _INSERTAR="INSERT INTO Registrar_Entrenamiento_Realizado (id_registrar_entrenamiento_realizado,tipo_de_ejercicio,grupo_muscular_trabajado,duracion_del_entrenamiento) VALUES (%s,%s,%s,%s)"
    _UPDATE="UPDATE Registrar_Entrenamiento_Realizado SET id_registrar_entrenamiento_realizado=%s,tipo_de_ejercicio=%s,grupo_muscular_trabajado=%s,duracion_del_entrenamiento=%s WHERE id_registrar_entrenamiento_realizado=%s"
    _DELETE="DELETE FROM Registrar_Entrenamiento_Realizado WHERE id_registrar_entrenamiento_realizado=%s"

    from Conexion import Conexion_1
from Cursor_del_pool import CursorDelPool_1
from Registrar_Entrenamiento import Registrar_Entrenamiento


class Registrar_Entrenamiento_RealizadoDAO:
    _SELECCIONAR = "SELECT * FROM Registrar_Entrenamiento_Realizado WHERE id_registrar_entrenamiento_realizado=%s"
    _INSERTAR = "INSERT INTO Registrar_Entrenamiento_Realizado (tipo_de_ejercicio, grupo_muscular_trabajado, duracion_del_entrenamiento) VALUES (%s, %s, %s)"
    _UPDATE = "UPDATE Registrar_Entrenamiento_Realizado SET tipo_de_ejercicio=%s, grupo_muscular_trabajado=%s, duracion_del_entrenamiento=%s WHERE id_registrar_entrenamiento_realizado=%s"
    _DELETE = "DELETE FROM Registrar_Entrenamiento_Realizado WHERE id_registrar_entrenamiento_realizado=%s"

    @classmethod
    def seleccionar_bd(cls, id_registrar_entrenamiento_realizado):
        with CursorDelPool_1() as cursor:
            cursor.execute(cls._SELECCIONAR, (id_registrar_entrenamiento_realizado,))
            registros = cursor.fetchall()
            entrenamientos = []
            for registro in registros:
                entrenamiento = Registrar_Entrenamiento(
                    id_registrar_entrenamiento_realizado=registro[0],
                    tipo_de_ejercicio=registro[1],
                    grupo_muscular_trabajado=registro[2],
                    duracion_del_entrenamiento=registro[3]
                )
                entrenamientos.append(entrenamiento)
            return entrenamientos

    @classmethod
    def insertar_bd(cls, entrenamiento):
        with CursorDelPool_1() as cursor:
            valores = (
                entrenamiento.tipo_de_ejercicio,
                entrenamiento.grupo_muscular_trabajado,
                entrenamiento.duracion_del_entrenamiento
            )
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Entrenamiento registrado: {entrenamiento}")
            return cursor.rowcount

    @classmethod
    def actualizar_bd(cls, entrenamiento):
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

    @classmethod
    def eliminar_bd(cls, entrenamiento):
        with CursorDelPool_1() as cursor:
            cursor.execute(cls._DELETE, (entrenamiento.id_registrar_entrenamiento_realizado,))
            log.debug(f"Entrenamiento eliminado con id: {entrenamiento.id_registrar_entrenamiento_realizado}")
            return cursor.rowcount


if __name__ == "__main__":
    # Ejemplo de inserción de entrenamiento
    nuevo_entrenamiento = Registrar_Entrenamiento(
        tipo_de_ejercicio="Cardio",
        grupo_muscular_trabajado="Pecho",
        duracion_del_entrenamiento="30"
    )
    
    usuario_insertado = Registrar_Entrenamiento_RealizadoDAO.insertar_bd(nuevo_entrenamiento) 
    log.info(f"Entrenamiento insertado: {usuario_insertado}")
 
