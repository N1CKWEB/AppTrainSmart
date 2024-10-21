from Conexion import Conexion_1  # Importación absoluta
from Cursor_del_pool import CursorDelPool_1  # Importación absoluta
from Cliente_GYM import Cliente_1  # Importación absoluta
from Logger_base import log  # Importación absoluta


class ClienteDAO_GYM:
    
    _SELECCIONAR = "SELECT * FROM clientes ORDER BY id_cliente"
    _INSERTAR = "INSERT INTO clientes (nombre, usuario, contraseña) VALUES (%s, %s, %s)"
    _UPDATE = "UPDATE clientes SET nombre=%s, usuario=%s, contraseña=%s WHERE id_cliente=%s"
    _DELETE = "DELETE FROM clientes WHERE id_cliente=%s"

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


if __name__ == "__main__":
    # Insertar cliente
    usuario02 = Cliente_1(1, 'Nicolas', 'nicodiaz23', 'nico2313')
    usuario_insertado = ClienteDAO_GYM.insertar_bd(usuario02)
