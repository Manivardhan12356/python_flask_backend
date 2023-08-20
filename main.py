# from flask import Flask, jsonify, request

# app = Flask(__name__)

# # Sample data
# data = []

# @app.route('/api/data', methods=['GET'])
# def get_data():
#     return jsonify(data)

# @app.route('/api/data', methods=['POST'])
# def create_data():
#     new_entry = request.get_json()
#     data.append(new_entry)
#     return jsonify(message='Data added successfully')

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, jsonify, request

app = Flask(__name__)

data = []

@app.route('/mani/<int:item_id>', methods=['GET'])
def mani(item_id):
    if item_id < len(data):
        return jsonify(data[item_id])
    else:
        return jsonify(message="Item not found")

@app.route('/mani', methods=['POST'])
def create_post():
    demo = request.get_json()
    data.append(demo)
    return jsonify(message='Success of post')

if __name__ == '__main__':
    app.run(debug=True)


