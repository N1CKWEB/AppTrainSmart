from AppTrainSmart_GYM.BaseDeDatos import Conexion 
from BaseDeDatos import Cursor_del_pool
from GUI import CLiente_GYM
from Logger_base import log

class ClienteDAO_NEW:
    _SELECCIONAR = "SELECT * FROM clientes ORDER BY id_cliente"
    _INSERTAR = "INSERT INTO clientes(nombre,usuario,contraseña ) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE clientes SET nombre=%s, usuario=%s, contraseña=%s WHERE id_cliente=%s"
    _ELIMINAR = "DELETE FROM clientes WHERE id_cliente=%s"

    @classmethod
    def seleccionar_bd(cls):
        with Cursor_del_pool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = CLiente_GYM(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes

    @classmethod
    def insertar_bd(cls, cliente):
        with Cursor_del_pool() as cursor:
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"Cliente insertado: {cliente}")
            return cursor.rowcount

    @classmethod
    def actualizar_bd(cls, cliente):
        with Cursor_del_pool() as cursor:
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id_cliente)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"Cliente actualizado: {cliente}")
            return cursor.rowcount

    @classmethod
    def eliminar_bd(cls, cliente):
        with Cursor_del_pool() as cursor:
            cursor.execute(cls._ELIMINAR, (cliente.id_cliente,))
            log.debug(f"Cliente eliminado con id: {cliente.id_cliente}")
            return cursor.rowcount

if __name__ == "__main__":

    # Insertar cliente
    usuario01 = CLiente_GYM(1,'Nicolas','nicodiaz23','nico2313')
    usuario_insertado = ClienteDAO_NEW.insertar_bd(usuario01)
    
    
    
    
    
    