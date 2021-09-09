import flask
from flask import request, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd
app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)



@app.route('/', methods=['GET'])
def read_list():
    return pd.read_csv('./book.csv').to_json(orient = 'records')
@app.route('/add', methods=['POST'])
def add_item_to_list():
    req_data = request.get_json()
    print(req_data)
    item = req_data['item']
    books = pd.read_csv('./book.csv')
    books.loc[len(books.index)] = [item] 
    books.to_csv('./book.csv')
    return "Add item success"

@app.route('/delete', methods=['DELETE'])
def delete_item():
    # Get item from the POST body
    req_data = request.get_json()
    item = req_data['item']
    books = pd.read_csv('./book.csv')
    length1 = len(books.index)
    index_names = books[books['name'] == item ].index
    books.drop(index_names, inplace = True)
    print(index_names)
    length2 = len(books.index)
    if length1 - length2 > 0:
        books.to_csv('./book.csv')
        return 'Delete item success'
    return 'Delete item fail'

app.run()
