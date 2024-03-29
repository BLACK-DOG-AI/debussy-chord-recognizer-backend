from flask import Blueprint
from src.commands.pong  import  Pong

ping_blueprint  = Blueprint('ping', __name__)

@ping_blueprint.route('/offers/ping', methods  = ['GET'])
def ping():
    result = Pong().execute()
    return result, 200