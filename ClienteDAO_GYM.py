from Conexion import Conexion_1  # Importación absoluta
from Cursor_del_pool import CursorDelPool_1  # Importación absoluta
from Cliente_GYM import Cliente_1  # Importación absoluta
from Logger_base import log  # Importación absoluta

class ClienteDAO_GYM_1:
    
    _SELECCIONAR = "SELECT * FROM clientes ORDER BY id_cliente"
    _INSERTAR = "INSERT INTO clientes (nombre, usuario, contraseña) VALUES (%s, %s, %s)"
    _UPDATE = "UPDATE clientes SET nombre=%s, usuario=%s, contraseña=%s WHERE id_cliente=%s"
    _DELETE = "DELETE FROM clientes WHERE id_cliente=%s"
    _VALIDAR_USUARIO = "SELECT * FROM clientes WHERE usuario = %s AND contraseña = %s"
    _USUARIO_EXISTE = "SELECT * FROM clientes WHERE usuario = %s"
    
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


if __name__ == "__main__":
    # Insertar cliente
    usuario02 = Cliente_1(3, 'Neymar', 'ney11', 'neeeyy')
    usuario_insertado = ClienteDAO_GYM_1.insertar_bd(usuario02)
