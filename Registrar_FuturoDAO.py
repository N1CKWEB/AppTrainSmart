from Conexion import Conexion_1
from Cursor_del_pool import CursorDelPool_1
from Registrar_Entrenamiento_Futuro import Registrar_Entrenamiento_Futuro
from Logger_base import log


class Registrar_FuturoDAO:
    _SELECCIONAR = "SELECT * FROM Registrar_Entrenamiento_Futuro ORDER BY id_registrar_entrenamiento_futuro"
    _INSERTAR = "INSERT INTO Registrar_Entrenamiento_Futuro (tipo_de_ejercicio, duracion_estimada_del_entrenamiento, objetivo_del_entrenamiento) VALUES (%s, %s, %s)"
    _UPDATE = "UPDATE Registrar_Entrenamiento_Futuro SET tipo_de_ejercicio=%s, duracion_estimada_del_entrenamiento=%s, objetivo_del_entrenamiento=%s WHERE id_registrar_entrenamiento_futuro=%s"
    _ELIMINAR = "DELETE FROM Registrar_Entrenamiento_Futuro WHERE id_registrar_entrenamiento_futuro=%s"

    @classmethod
    def seleccionar_bd(cls):
        with CursorDelPool_1() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            entrenamientos_futuros = []
            for registro in registros:
                entrenamiento_futuro = Registrar_Entrenamiento_Futuro(
                    id_registrar_entrenamiento_futuro=registro[0],
                    tipo_de_ejercicio=registro[1],
                    duracion_estimada_del_entrenamiento=registro[2],
                    objetivo_del_entrenamiento=registro[3]
                )
                entrenamientos_futuros.append(entrenamiento_futuro)
            return entrenamientos_futuros

    @classmethod
    def insertar_bd(cls, entrenamiento_futuro):
        with CursorDelPool_1() as cursor:
            valores = (
                entrenamiento_futuro.tipo_de_ejercicio,
                entrenamiento_futuro.duracion_estimada_del_entrenamiento,
                entrenamiento_futuro.objetivo_del_entrenamiento
            )
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Entrenamiento futuro registrado: {entrenamiento_futuro}")
            return cursor.rowcount
    
    @classmethod
    def insertar_bd(cls,entrenamiento_Futuro):
      try:
        with CursorDelPool_1() as cursor:
            valores=(
                entrenamiento_Futuro['tipo_de_ejercicio'],
                entrenamiento_Futuro['duracion_estimada_del_entrenamiento'],
                entrenamiento_Futuro['objetivo_del_entrenamiento']
            )
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f"Entrenamiento futuro registrado: {entrenamiento_Futuro}")
            return cursor.rowcount
      except Exception as e:
          log.error(f'Error al insertar entrenamiento futuro')  
         
    @classmethod
    def actualizar_bd(cls, entrenamiento_futuro):
        with CursorDelPool_1() as cursor:
            valores = (
                entrenamiento_futuro.tipo_de_ejercicio,
                entrenamiento_futuro.duracion_estimada_del_entrenamiento,
                entrenamiento_futuro.objetivo_del_entrenamiento,
                entrenamiento_futuro.id_registrar_entrenamiento_futuro
            )
            cursor.execute(cls._UPDATE, valores)
            log.debug(f"Entrenamiento futuro actualizado: {entrenamiento_futuro}")
            return cursor.rowcount

    @classmethod
    def eliminar_bd(cls, entrenamiento_futuro):
        with CursorDelPool_1() as cursor:
            cursor.execute(cls._ELIMINAR, (entrenamiento_futuro.id_registrar_entrenamiento_futuro,))
            log.debug(f"Entrenamiento futuro eliminado con id: {entrenamiento_futuro.id_registrar_entrenamiento_futuro}")
            return cursor.rowcount


if __name__ == "__main__":
    # Ejemplo de inserción de entrenamiento futuro
    nuevo_entrenamiento_futuro = Registrar_Entrenamiento_Futuro(
        tipo_de_ejercicio="Pesas",
        duracion_estimada_del_entrenamiento="45",
        objetivo_del_entrenamiento="Aumento de masa muscular"
    )
    
    usuario_insertado = Registrar_FuturoDAO.insertar_bd(nuevo_entrenamiento_futuro) 
    log.info(f"Entrenamiento futuro insertado: {usuario_insertado}")
