from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']
collection = db['actions']

@app.route('/')
def home():
    return render_template('site.html')

@app.route('/api/action', methods=['POST'])
def handle_action():
    data = request.json
    action = data.get('action')
    if action in ['add_to_cart', 'buy_now', 'checkout']:
        collection.insert_one({
            'action': action,
            'timestamp': datetime.now()
        })
        return jsonify({'message': f'{action} action recorded.'})
    return jsonify({'message': 'Invalid action.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
