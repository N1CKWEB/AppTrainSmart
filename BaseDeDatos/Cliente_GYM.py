from Logger_base import log

class Cliente:
    
    def __init__(self,id_cliente=None,nombre=None,usuario=None,contraseña=None):
        self.id_cliente=id_cliente
        self.nombre=nombre
        self.usuario=usuario
        self.contraseña=contraseña
        
    def __str__(self):
        return f"Cliente(id_cliente={self.id_cliente}, nombre={self.nombre}, usuario={self.usuario}, contraseña={self.contraseña})"
    
    def __repr__(self):
        return f"Cliente(id_cliente={self.id_cliente}, nombre={self.nombre}, usuario={self.usuario}, contraseña={self.contraseña})"    
    
    
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
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def membresia(self):
        return self._membresia

    @membresia.setter
    def membresia(self, membresia):
        self._membresia = membresia


if __name__ == "__main__":
    usuario02 = Cliente(1,'Nicolas','nicodiaz23','nico2313')
    log.debug(usuario02)
        