from flask import Blueprint, jsonify, request
pppProfile_bp = Blueprint('pppProfile', __name__)
@pppProfile_bp.route('/pppProfile', methods=['GET'])
def get_pppProfile():
    pppProfile = [
        {'id': 1, 'name': 'Item 1'},
        {'id': 100, 'name': 'Item 2'},
        {'id': 101, 'name': 'Item 2'},
        {'id': 102, 'name': 'Item 2'},
        {'id': 103, 'name': 'Item 2'},
        {'id': 104, 'name': 'Item 2'},
    ]
    return jsonify(pppProfile)
