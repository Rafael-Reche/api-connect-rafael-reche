from flask import Blueprint
from controllers.connect_controller import ConnectController

connect_bp = Blueprint('connect', __name__, url_prefix='/api')

connect_bp.route('/users', methods=['GET'])(ConnectController.get_users)
connect_bp.route('/users', methods=['POST'])(ConnectController.create_user)
connect_bp.route('/users/<string:user_id>', methods=['GET'])(ConnectController.get_user_by_id)
connect_bp.route('/users/<string:user_id>', methods=['PUT'])(ConnectController.update_user)
connect_bp.route('/users/<string:user_id>', methods=['DELETE'])(ConnectController.delete_user)
