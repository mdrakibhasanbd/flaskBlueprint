import json

from flask import Blueprint, jsonify, request
from ..dbconfig.db import get_mongo_db
from ..dbconfig.jsoni import JSONEncoder

mikrotik_bp = Blueprint('mikrotik', __name__)

db = get_mongo_db()
@mikrotik_bp.route('/items', methods=['GET'])
def get_items():
    # db.drop_collection('mikrotik')


    # db['mikrotik'].insert_many(items)
    mikrotikData = []
    findItems = db['mikrotik'].find()
    mikrotikData.extend(findItem for findItem in findItems)



    return json.dumps(mikrotikData, cls=JSONEncoder)


@mikrotik_bp.route('/addMikrotik', methods=['POST'])
def add_mikrotik():
    mikrotik = request.json
    print(mikrotik)
    return jsonify(mikrotik)
