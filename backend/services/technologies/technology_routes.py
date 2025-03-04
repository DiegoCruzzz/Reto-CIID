from flask import Blueprint, request, jsonify
from services.technologies.create import create_technology
from services.technologies.read import (get_all_technologies, get_technology_by_id)
from services.technologies.update import update_technology
from services.technologies.delete import delete_technology

technology_bp = Blueprint('technology_bp', __name__)

@technology_bp.route('/api/technologies/create', methods=['POST'])
def create_technology_route():
    data = request.json
    new_technology = create_technology(data)
    return jsonify(new_technology.serialize()), 201

@technology_bp.route('/api/technologies/read', methods=['GET'])
def get_technologies_route():
    technologies = get_all_technologies()
    return jsonify([tech.serialize() for tech in technologies]), 200

@technology_bp.route('/api/technologies/read/<int:id>', methods=['GET'])
def get_technology_route(id):
    technology = get_technology_by_id(id)
    return jsonify(technology.serialize()), 200

@technology_bp.route('/api/technologies/update/<int:id>', methods=['PUT'])
def update_technology_route(id):
    data = request.json
    updated_technology = update_technology(id, data)
    return jsonify(updated_technology.serialize()), 200

@technology_bp.route('/api/technologies/delete/<int:id>', methods=['DELETE'])
def delete_technology_route(id):
    delete_technology(id)
    return '', 204