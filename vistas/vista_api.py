from flask import Blueprint, request, jsonify
from servicios.servicio_seguridad import ServicioSeguridad

api_bp = Blueprint("api", __name__, url_prefix="/api")
servicio = ServicioSeguridad()


@api_bp.route("/usuarios", methods=["POST"])
def registrar_usuario():
    datos = request.get_json(silent=True)
    campos = ("usuario", "nombre_completo", "correo", "password")

    if not datos or not all(c in datos for c in campos):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # El rol siempre es VENDEDOR (2) al registrarse por esta puerta
    ok, mensaje = servicio.registrar(
        datos["usuario"], datos["nombre_completo"],
        datos["correo"], datos["password"]
    )

    if ok:
        return jsonify({"mensaje": mensaje}), 201
    return jsonify({"error": mensaje}), 400


@api_bp.route("/login", methods=["POST"])
def login():
    datos = request.get_json(silent=True)

    if not datos or not all(c in datos for c in ("usuario", "password")):
        return jsonify({"error": "Faltan datos requeridos"}), 400

    ok, mensaje, usuario = servicio.login(datos["usuario"], datos["password"])

    if ok:
        return jsonify({"mensaje": mensaje, "usuario": usuario}), 200
    return jsonify({"error": mensaje}), 401