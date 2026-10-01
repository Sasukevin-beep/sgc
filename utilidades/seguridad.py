import bcrypt


def hash_password(password):
    """Convierte la contraseña en un texto revuelto que no se puede leer."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verificar_password(password, clave_hash):
    """Dice si la contraseña escrita coincide con la revuelta guardada."""
    return bcrypt.checkpw(password.encode("utf-8"), clave_hash.encode("utf-8"))