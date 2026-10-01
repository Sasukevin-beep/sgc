from dao.usuario_dao import UsuarioDAO
from modelos.usuario import Usuario
from utilidades.seguridad import hash_password, verificar_password


class ServicioSeguridad:
    """Reglas del negocio: aquí se decide si algo se permite o no."""

    def __init__(self):
        self.dao = UsuarioDAO()

    def _validar_clave(self, password):
        # Regla RN-02 del taller: mínimo 8 caracteres, una mayúscula y un número
        if len(password) < 8:
            return "La contraseña debe tener mínimo 8 caracteres"
        if not any(c.isupper() for c in password):
            return "La contraseña debe tener al menos una mayúscula"
        if not any(c.isdigit() for c in password):
            return "La contraseña debe tener al menos un número"
        return None

    def registrar(self, usuario, nombre_completo, correo, password, id_rol=2):
        error = self._validar_clave(password)
        if error:
            return False, error

        if self.dao.buscar_por_usuario(usuario):
            return False, "El usuario ya existe"

        if self.dao.buscar_por_correo(correo):
            return False, "El correo ya está registrado"

        nuevo = Usuario(
            usuario=usuario,
            nombre_completo=nombre_completo,
            correo=correo,
            clave_hash=hash_password(password),
            id_rol=id_rol,
        )
        self.dao.insertar(nuevo)
        return True, "Usuario registrado exitosamente"

    def login(self, usuario, password):
        datos = self.dao.buscar_por_usuario(usuario)

        if datos is None:
            return False, "Usuario o contraseña incorrectos", None

        if datos["estado"] != "ACTIVO":
            return False, "El usuario no está activo", None

        if not verificar_password(password, datos["clave_hash"]):
            return False, "Usuario o contraseña incorrectos", None

        # Se devuelven los datos SIN la contraseña
        datos.pop("clave_hash")
        return True, "Ingreso exitoso", datos