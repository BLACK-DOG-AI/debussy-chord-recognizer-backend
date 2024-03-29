from flask import jsonify, request, Blueprint
from src.commands.create_offer import CreateOffer
from src.commands.get_offer import GetOffer
from src.commands.get_list_offer import GetListOffer
from src.commands.delete_offer import DeleteOffer

offer_blueprint  = Blueprint('offer', __name__)

@offer_blueprint.route('/offers', methods  = ['POST'])
def create_offer():
    json = request.get_json()
    token = request.headers.get('Authorization', '').strip()
    result = CreateOffer(json, token).execute()
    return jsonify(result), 201

@offer_blueprint.route('/offers/<string:id>', methods  = ['GET'])
def get_offer(id):
    token = request.headers.get('Authorization', '').strip()
    result = GetOffer(id, token).execute()
    return jsonify(result), 200

@offer_blueprint.route('/offers', methods  = ['GET'])
def get_list_offer():
    owner = request.args.get('owner', '').strip()
    post_id = request.args.get('post', '').strip()
    token = request.headers.get('Authorization', '').strip()
    result = GetListOffer(token, owner, post_id).execute()
    return jsonify(result), 200

@offer_blueprint.route('/offers/<string:id>', methods  = ['DELETE'])
def delete_offer(id):
    token = request.headers.get('Authorization', '').strip()
    result = DeleteOffer(id, token).execute()
    return jsonify(result), 200