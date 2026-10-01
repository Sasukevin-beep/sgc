from database.conexion import Conexion
from modelos.usuario import Usuario


class UsuarioDAO:

    def insertar(self, u: Usuario) -> int:
        sql = """INSERT INTO usuario
                 (usuario, nombre_completo, correo, clave_hash, id_rol)
                 VALUES (%s, %s, %s, %s, %s)"""
        datos = (u.usuario, u.nombre_completo, u.correo, u.clave_hash, u.id_rol)
        with Conexion() as cn:
            cursor = cn.cursor()
            cursor.execute(sql, datos)
            return cursor.lastrowid

    def buscar_por_usuario(self, nombre_usuario: str):
        sql = """SELECT id_usuario, usuario, nombre_completo, correo,
                        clave_hash, id_rol, intentos_fallidos, estado
                 FROM usuario WHERE usuario = %s"""
        with Conexion() as cn:
            cursor = cn.cursor(dictionary=True)
            cursor.execute(sql, (nombre_usuario,))
            return cursor.fetchone()

    def buscar_por_correo(self, correo: str):
        sql = "SELECT id_usuario FROM usuario WHERE correo = %s"
        with Conexion() as cn:
            cursor = cn.cursor(dictionary=True)
            cursor.execute(sql, (correo,))
            return cursor.fetchone()