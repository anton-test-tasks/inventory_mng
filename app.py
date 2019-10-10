from flask import Flask, jsonify, request
from Inventory import Inventory


app = Flask(__name__)

inventory = Inventory()


@app.route('/items/', methods=['GET'])
def get_items():
    store_id = request.args.get('store_id', default='')
    item_name = request.args.get('item_name', default='')
    category_id = request.args.get('category_id', default='')
    result = []
    if store_id != '':
        result = inventory.get_categories_for_store(int(store_id))
    elif item_name != '':
        result = inventory.get_item_inventory(item_name)
    elif category_id != '':
        result = inventory.get_median_for_category(int(category_id))
    else:
        result = inventory.data

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
