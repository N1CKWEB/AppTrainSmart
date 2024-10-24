from Conexion import Conexion_1  # Importación absoluta
from Cursor_del_pool import CursorDelPool_1  # Importación absoluta
from Cliente_GYM import Cliente_1  # Importación absoluta
from Logger_base import log  # Importación absoluta
from Registrar_Entrenamiento import Registrar_Entrenamiento
from Registrar_Entrenamiento_Futuro import Registrar_Entrenamiento_Futuro
from Seguimiento_Registrado_Anteriormente import Seguimiento_Registrado_Anteriormente
class ClienteDAO_GYM_1:
    
    _SELECCIONAR = "SELECT * FROM clientes ORDER BY id_cliente"
    _INSERTAR = "INSERT INTO clientes (nombre, usuario, contraseña) VALUES (%s, %s, %s)"
    _UPDATE = "UPDATE clientes SET nombre=%s, usuario=%s, contraseña=%s WHERE id_cliente=%s"
    _DELETE = "DELETE FROM clientes WHERE id_cliente=%s"
    _VALIDAR_USUARIO = "SELECT * FROM clientes WHERE usuario = %s AND contraseña = %s"
    _USUARIO_EXISTE = "SELECT * FROM clientes WHERE usuario = %s"
    # # Consultas para obtener entrenamientos
    # _OBTENER_ENTRENAMIENTOS = """
    #     SELECT sr.fecha_seguimiento, er.tipo_de_ejercicio, er.duracion_del_entrenamiento, sr.comentarios
    #     FROM Seguimiento_Registrado_Anteriormente sr
    #     JOIN Registrar_Entrenamiento_Realizado er ON sr.id_registrar_entrenamiento_realizado = er.id_registrar_entrenamiento_realizado
    #     ORDER BY sr.fecha_seguimiento;
    # """
    # # Método para insertar entrenamientos
    # _INSERTAR_ENTRENAMIENTO = "INSERT INTO Registrar_Entrenamiento_Realizado (tipo_de_ejercicio, grupo_muscular_trabajado, duracion_de_entrenamiento) VALUES (%s, %s, %s)"

    @classmethod
    def insertar_entrenamiento(cls, entrenamiento):
        with CursorDelPool_1() as cursor:
            valores = (entrenamiento.tipo_ejercicio, entrenamiento.grupo_muscular, entrenamiento.duracion)
            cursor.execute(cls._INSERTAR_ENTRENAMIENTO, valores)
            log.debug(f"Entrenamiento insertado: {entrenamiento}")
            return cursor.rowcount

    @classmethod
    def seleccionar_bd(cls):
        with CursorDelPool_1() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente_1(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes

    @classmethod
    def insertar_bd(cls, cliente):
        with CursorDelPool_1() as cursor:
            valores = (cliente.nombre, cliente.usuario, cliente.contraseña)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Cliente insertado: {cliente}")
            return cursor.rowcount
    @classmethod
    def actualizar_bd(cls, cliente):
        with CursorDelPool_1() as cursor:
            valores = (cliente.nombre, cliente.usuario, cliente.contraseña, cliente.id_cliente)
            cursor.execute(cls._UPDATE, valores)
            log.debug(f"Cliente actualizado: {cliente}")
            return cursor.rowcount

    @classmethod
    def eliminar_bd(cls, cliente):
        with CursorDelPool_1() as cursor:
            cursor.execute(cls._DELETE, (cliente.id_cliente,))
            log.debug(f"Cliente eliminado con id: {cliente.id_cliente}")
            return cursor.rowcount

    @classmethod
    def validar_usuario(cls, usuario, contraseña):
        with CursorDelPool_1() as cursor:
            cursor.execute(cls._VALIDAR_USUARIO, (usuario, contraseña))
            resultado = cursor.fetchone()  # Obtener el primer resultado de la consulta
            if resultado:
                # Si se encuentra un usuario, devuelve un objeto Cliente_1
                return Cliente_1(resultado[0], resultado[1], resultado[2], resultado[3])  # Ajusta los índices según tu tabla
            return None  # Si no se encuentra, retorna None
    
    @classmethod
    def usuario_existe(cls, usuario):
        with CursorDelPool_1() as cursor:
            cursor.execute(cls._USUARIO_EXISTE, (usuario,))
            resultado = cursor.fetchone()  # Obtener el primer resultado de la consulta
            return resultado is not None  # Retorna True si el usuario existe, de lo contrario False

    
    # Método para obtener los entrenamientos registrados
    @classmethod
    def obtener_entrenamientos(cls):
        with CursorDelPool_1() as cursor:
            cursor.execute(cls._OBTENER_ENTRENAMIENTOS)
            registros = cursor.fetchall()  # Obtener todos los resultados
            
            entrenamientos = []
            for registro in registros:
                entrenamiento = {
                    "fecha": registro[0],
                    "tipo_ejercicio": registro[1],
                    "duracion": registro[2],
                    "comentarios": registro[3]
                }
                entrenamientos.append(entrenamiento)
            return entrenamientos  # Retorna una lista de entrenamientos 

   
if __name__ == "__main__":
    
    # # Insertar cliente
    # usuario02 =Registrar_Entrenamiento(1,"Cardio","Pecho","30")
    # usuario_insertado = ClienteDAO_GYM_1.insertar_bd(usuario02) 
    # log.info(f"Usuario insertado: {usuario_insertado}")
     pass