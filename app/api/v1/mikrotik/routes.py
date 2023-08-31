from flask import Blueprint, jsonify, request
from ..dbconfig.db import get_mongo_db
from ..dbconfig.jsoni import JSONEncoder
from pymongo.errors import ServerSelectionTimeoutError
import json

mikrotik_bp = Blueprint('mikrotik', __name__)


# Remove the global db definition

@mikrotik_bp.route('/items', methods=['GET'])
def get_items():
    try:
        db = get_mongo_db()

        # Perform operations on the database
        mikrotikData = []
        findItems = db['mikrotik'].find()
        mikrotikData.extend(findItem for findItem in findItems)

        return json.dumps(mikrotikData, cls=JSONEncoder)
    except ServerSelectionTimeoutError:
        error_message = {
            "error": "connection_error",
            "message": "Unable to connect to the MongoDB server."
        }
        # HTTP status code 500 indicates Internal Server Error
        return jsonify(error_message), 500


@mikrotik_bp.route('/addMikrotik', methods=['POST'])
def add_mikrotik():
    mikrotik = request.json
    print(mikrotik)
    return jsonify(mikrotik)
