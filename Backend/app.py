# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

chat_rooms = {}

@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200

@app.route('/api/messages/<roomId>', methods=['GET', 'POST'])
def handle_messages(roomId):
    if request.method == 'GET':
        messages = chat_rooms.get(roomId, [])
        return jsonify(messages)

    if request.method == 'POST':
        data = request.get_json()
        # --- CHANGE HERE: We now require a 'text' and a 'sender' ---
        if not data or 'text' not in data or 'sender' not in data:
            return jsonify({"error": "Message text and sender are required"}), 400

        new_message = {
            'sender': data['sender'], # Store the sender's ID
            'text': data['text'],
            'timestamp': datetime.datetime.utcnow().isoformat() + 'Z'
        }

        if roomId not in chat_rooms:
            chat_rooms[roomId] = []
        
        chat_rooms[roomId].append(new_message)
        
        return jsonify(new_message), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)