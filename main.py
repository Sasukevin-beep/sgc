from flask import Flask
from vistas.vista_api import api_bp

app = Flask(__name__)
app.register_blueprint(api_bp)


@app.route("/")
def inicio():
    return {"mensaje": "API SGC - Sistema de Gestión Comercial"}


if __name__ == "__main__":
    app.run(debug=True, port=5000)