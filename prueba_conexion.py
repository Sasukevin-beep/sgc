from database.conexion import Conexion

with Conexion() as cn:
    cursor = cn.cursor()
    cursor.execute("SELECT nombre FROM rol")
    for fila in cursor.fetchall():
        print(fila[0])