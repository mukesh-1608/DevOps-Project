# Backend/app.py

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import datetime

# This tells Flask to serve files from the 'static' folder we created in the Dockerfile
app = Flask(__name__, static_folder='static')
CORS(app)

chat_rooms = {}

# This route serves the main index.html file
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# This route serves any other file (like chat.html)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# Health check endpoint for Kubernetes
@app.route('/health', methods=['GET'])
def health_check():
    return "OK", 200

# API endpoint for sending and receiving messages
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
    app.run(host='0.0.0.0', port=5000)