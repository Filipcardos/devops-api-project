import os
from flask import Flask, jsonify

from db import get_db_connection


def create_app():
    app = Flask(__name__)

    @app.route("/", methods=["GET"])
    def home():
        return jsonify({"message": "API está funcionando 🚀"}), 200

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200

    @app.route("/db-status", methods=["GET"])
    def db_status():
        try:
            conn = get_db_connection()
            conn.close()
            return jsonify({"database": "connected"}), 200
        except Exception as error:
            return jsonify({"database": "unavailable", "error": str(error)}), 503

    @app.errorhandler(404)
    def not_found(_error):
        return jsonify({"error": "Rota não encontrada"}), 404

    @app.errorhandler(500)
    def internal_error(_error):
        return jsonify({"error": "Erro interno do servidor"}), 500

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=port, debug=debug)
