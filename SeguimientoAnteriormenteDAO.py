from Conexion import Conexion_1  # Importación absoluta
from Cursor_del_pool import CursorDelPool_1  # Importación absoluta
from Cliente_GYM import Cliente_1  # Importación absoluta
from Logger_base import log  # Importación absoluta
from Registrar_Entrenamiento import Registrar_Entrenamiento
from Registrar_Entrenamiento_Futuro import Registrar_Entrenamiento_Futuro   
from Seguimiento_Registrado_Anteriormente import Seguimiento_Registrado_Anteriormente

class SeguimientoAnteriormenteDAO_GYM_1:
    _SELECCIONAR = "SELECT * FROM Seguimiento_Registrado_Anteriormente WHERE id_seguimiento = %s"
    _INSERTAR = "INSERT INTO Seguimiento_Registrado_Anteriormente (id_registrar_entrenamiento_realizado, id_registrar_entrenamiento_futuro, fecha_seguimiento, comentarios) VALUES (%s, %s, %s, %s)"
    _UPDATE = "UPDATE Seguimiento_Registrado_Anteriormente SET id_registrar_entrenamiento_futuro = %s, fecha_seguimiento = %s, comentarios = %s WHERE id_seguimiento = %s"
    _DELETE = "DELETE FROM Seguimiento_Registrado_Anteriormente WHERE id_seguimiento = %s"

    @classmethod
    def seleccionar_bd(cls, id_seguimiento):
        with CursorDelPool_1() as cursor:
            cursor.execute(cls._SELECCIONAR, (id_seguimiento,))
            registros = cursor.fetchall()
            seguimientos = []
            for registro in registros:
                seguimiento = Seguimiento_Registrado_Anteriormente(
                    id_seguimiento=registro[0],
                    id_registrar_entrenamiento_realizado=registro[1],
                    id_registrar_entrenamiento_futuro=registro[2],
                    fecha_seguimiento=registro[3],
                    comentarios=registro[4]
                )
                seguimientos.append(seguimiento)
            return seguimientos

    @classmethod
    def insertar_bd(cls, seguimiento):
        with CursorDelPool_1() as cursor:
            valores = (
                seguimiento.id_registrar_entrenamiento_realizado, 
                seguimiento.id_registrar_entrenamiento_futuro, 
                seguimiento.fecha_seguimiento, 
                seguimiento.comentarios
            )
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Seguimiento insertado: {seguimiento}")
            return cursor.rowcount

    @classmethod
    def actualizar_bd(cls, seguimiento):
        with CursorDelPool_1() as cursor:
            valores = (
                seguimiento.id_registrar_entrenamiento_futuro, 
                seguimiento.fecha_seguimiento, 
                seguimiento.comentarios, 
                seguimiento.id_seguimiento
            )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f"Seguimiento actualizado: {seguimiento}")
            return cursor.rowcount

    @classmethod
    def eliminar_bd(cls, seguimiento):
        with CursorDelPool_1() as cursor:
            cursor.execute(cls._DELETE, (seguimiento.id_seguimiento,))
            log.debug(f"Seguimiento eliminado con id: {seguimiento.id_seguimiento}")
            return cursor.rowcount


if __name__ == "__main__":
    # Ejemplo de inserción de seguimiento
    seguimiento_nuevo = Seguimiento_Registrado_Anteriormente(
        id_registrar_entrenamiento_realizado=1,
        id_registrar_entrenamiento_futuro=2,
        fecha_seguimiento="2024-10-23",
        comentarios="Seguimiento de progreso"
    )
    
    usuario_insertado = SeguimientoAnteriormenteDAO_GYM_1.insertar_bd(seguimiento_nuevo) 
    log.info(f"Seguimiento insertado: {usuario_insertado}")
