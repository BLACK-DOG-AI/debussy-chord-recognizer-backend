from flask import jsonify, Blueprint
from src.commands.reset import Reset

database_managment_blueprint  = Blueprint('database_managment', __name__)

@database_managment_blueprint.route('/offers/reset', methods  = ['POST'])
def reset_offer():
    result = Reset().execute()
    return jsonify(result), 200