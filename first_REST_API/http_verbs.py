from flask import (Flask,
                    jsonify, 
                    request as req,
                    render_template)
from flask.wrappers import Response

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

@app.route('/')
def home() -> str:
    return render_template('index.html')


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
def get_a_store(name: str) -> Response:
    for store in stores: 
        if name == store['name']:
            return jsonify(store)
    return jsonify({'message': 'Store not found'})


# GET /store
@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name: str) -> Response:
    req_data = req.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':req_data['name'],
                'price':req_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_items_in_stores(name:str) -> Response:
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message': 'Store not found'})


app.run(port=5001)