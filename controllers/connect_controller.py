import re
from flask import request, jsonify
from data.mock_database import db

class ConnectController:
    
    @staticmethod
    def _is_valid_email(email: str) -> bool:
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))

    @staticmethod
    def get_users():
        users = db.get_all_users()
        return jsonify({
            "status": "success",
            "data": users,
            "count": len(users)
        }), 200

    @staticmethod
    def create_user():
        data = request.get_json(silent=True)
        if data is None:
            return jsonify({
                "status": "fail",
                "error": {
                    "code": "INVALID_JSON",
                    "message": "O corpo da requisição deve ser um JSON válido."
                }
            }), 400

        nome = data.get("nome")
        email = data.get("email")

        if not nome or not isinstance(nome, str) or not nome.strip():
            return jsonify({
                "status": "fail",
                "error": {
                    "code": "MISSING_PARAM",
                    "message": "O campo 'nome' é obrigatório e não pode ser vazio."
                }
            }), 400

        if not email or not isinstance(email, str) or not email.strip():
            return jsonify({
                "status": "fail",
                "error": {
                    "code": "MISSING_PARAM",
                    "message": "O campo 'email' é obrigatório e não pode ser vazio."
                }
            }), 400

        nome = nome.strip()
        email = email.strip().lower()

        if not ConnectController._is_valid_email(email):
            return jsonify({
                "status": "fail",
                "error": {
                    "code": "INVALID_FORMAT",
                    "message": "O campo 'email' fornecido possui um formato inválido."
                }
            }), 400

        existing_users = db.get_all_users()
        if any(user["email"] == email for user in existing_users):
            return jsonify({
                "status": "fail",
                "error": {
                    "code": "DUPLICATE_ENTRY",
                    "message": f"O e-mail '{email}' já está cadastrado no sistema."
                }
            }), 400

        new_user = db.create_user(nome=nome, email=email)

        return jsonify({
            "status": "success",
            "message": "Usuário cadastrado com sucesso.",
            "data": new_user
        }), 201

    @staticmethod
    def get_user_by_id(user_id: str):
        user = db.get_user_by_id(user_id)
        if not user:
            return jsonify({
                "status": "fail",
                "error": {
                    "code": "NOT_FOUND",
                    "message": f"Usuário com o ID '{user_id}' não foi encontrado."
                }
            }), 404

        return jsonify({
            "status": "success",
            "data": user
        }), 200

    @staticmethod
    def update_user(user_id: str):
        data = request.get_json(silent=True)
        if not data:
            return jsonify({
                "status": "fail",
                "error": {
                    "code": "INVALID_JSON",
                    "message": "Nenhum dado fornecido para atualização."
                }
            }), 400

        updated_user = db.update_user(
            user_id=user_id,
            nome=data.get("nome"),
            email=data.get("email")
        )

        if not updated_user:
            return jsonify({
                "status": "fail",
                "error": {
                    "code": "NOT_FOUND",
                    "message": f"Impossível atualizar. Usuário com ID '{user_id}' não foi encontrado."
                }
            }), 404

        return jsonify({
            "status": "success",
            "message": "Usuário atualizado com sucesso.",
            "data": updated_user
        }), 200

    @staticmethod
    def delete_user(user_id: str):
        is_deleted = db.delete_user(user_id)
        if not is_deleted:
            return jsonify({
                "status": "fail",
                "error": {
                    "code": "NOT_FOUND",
                    "message": f"Impossível excluir. Usuário com ID '{user_id}' não foi encontrado."
                }
            }), 404

        return jsonify({
            "status": "success",
            "message": f"Usuário com ID '{user_id}' foi removido com sucesso."
        }), 200
