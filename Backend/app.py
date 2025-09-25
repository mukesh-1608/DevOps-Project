# backend/app.py

# --- NEW: Import 'send_from_directory' ---
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import datetime
import os

# --- NEW: Tell Flask where the static frontend files are ---
app = Flask(__name__, static_folder='static')
CORS(app)

chat_rooms = {}

# --- NEW: Route to serve the main index.html page ---
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# --- NEW: Route to serve the chat.html page ---
@app.route('/chat.html')
def serve_chat():
    return send_from_directory(app.static_folder, 'chat.html')

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
        if not data or 'text' not in data or 'sender' not in data:
            return jsonify({"error": "Message text and sender are required"}), 400

        new_message = {
            'sender': data['sender'],
            'text': data['text'],
            'timestamp': datetime.datetime.utcnow().isoformat() + 'Z'
        }

        if roomId not in chat_rooms:
            chat_rooms[roomId] = []
        
        chat_rooms[roomId].append(new_message)
        
        return jsonify(new_message), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)