from flask import Blueprint, request, jsonify
from services.startups.create import create_startup
from services.startups.read import (get_all_startups, get_startup_by_id)
from services.startups.update import update_startup
from services.startups.delete import delete_startup


startup_bp = Blueprint('startup_bp', __name__)

@startup_bp.route('/api/startups/create', methods=['POST'])
def create_startup_route():
    data = request.json
    new_startup = create_startup(data)
    return jsonify(new_startup.serialize()), 201

@startup_bp.route('/api/startups/read', methods=['GET'])
def get_startups_route():
    startups = get_all_startups()
    return jsonify([startup.serialize() for startup in startups]), 200

@startup_bp.route('/api/startups/read/<int:id>', methods=['GET'])
def get_startup_route(id):
    startup = get_startup_by_id(id)
    return jsonify(startup.serialize()), 200

@startup_bp.route('/api/startups/update/<int:id>', methods=['PUT'])
def update_startup_route(id):
    data = request.json
    updated_startup = update_startup(id, data)
    return jsonify(updated_startup.serialize()), 200

@startup_bp.route('/api/startups/delete/<int:id>', methods=['DELETE'])
def delete_startup_route(id):
    delete_startup(id)
    return '', 204
