import re
from flask import Flask,jsonify, request as req

app = Flask(__name__)

stores = [ 
    {
        'name':'my_store',
        'items': [
            {'name':'A','price': 15.99},
            {'name':'B','price':12.59}
        ]
    },
    {
        'name':'clod_store',
        'items': [
            {'name':'A','price': 150.99},
            {'name':'B','price':120.59}
        ]
    }

]


# POST /store data:{name:}
@app.route('/store', methods=['POST'])
def create_store():
    req_data = req.get_json()
    new_store = {
        'name': req_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/ <string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_a_store(name):
    for store in stores: 
        if name == store['name']:
            return jsonify(store)
    return "Not found"


# GET /store
@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_item(name):
    pass


app.run(port=5001)