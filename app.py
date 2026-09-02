import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from routes.connect_routes import connect_bp

load_dotenv()

app = Flask(__name__)

@app.before_request
def parse_json_middleware():
    if request.method in ['POST', 'PUT', 'PATCH'] and request.data:
        if not request.is_json:
            return jsonify({
                "status": "fail",
                "error": {
                    "code": "BAD_REQUEST",
                    "message": "O Content-Type deve ser application/json"
                }
            }), 400

app.register_blueprint(connect_bp)

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
