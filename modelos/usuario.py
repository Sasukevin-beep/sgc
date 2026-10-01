class Usuario:
    def __init__(self, usuario, nombre_completo, correo, clave_hash, id_rol,
                 id_usuario=None, estado="ACTIVO", intentos_fallidos=0):
        self.id_usuario = id_usuario
        self.usuario = usuario
        self.nombre_completo = nombre_completo
        self.correo = correo
        self.clave_hash = clave_hash
        self.id_rol = id_rol
        self.estado = estado
        self.intentos_fallidos = intentos_fallidos