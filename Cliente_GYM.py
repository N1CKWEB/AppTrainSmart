from Logger_base import log

class Cliente_1:

    def __init__(self, id_cliente=None, nombre=None, usuario=None, contraseña=None):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.usuario = usuario
        self.contraseña = contraseña

    def __str__(self):
        return (f'Id: {self.id_cliente}, Nombre: {self.nombre}, '
                f'usuario: {self.usuario}, contraseña: {self.contraseña}')


    @property
    def id_cliente(self):
        return self._id_cliente
    
    @id_cliente.setter
    def id_cliente(self, id_cliente):
        self._id_cliente = id_cliente

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def contraseña(self):
        return self._contraseña

    @contraseña.setter
    def contraseña(self, contraseña):
        self._contraseña = contraseña


if __name__ == "__main__":
    usuario02 = Cliente_1(1, "Nicolas", "Diaz", "2303")
    log.debug(usuario02)
