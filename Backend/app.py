# Final Corrected app.py

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import datetime

# This configuration correctly serves files from the 'Frontend' subfolder
app = Flask(__name__, static_folder='Frontend')
CORS(app)

chat_rooms = {}

# Route to serve the main index.html page
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Route to serve any other file (like chat.html)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

# API endpoint for messages
@app.route('/api/messages/<roomId>', methods=['GET', 'POST'])
def handle_messages(roomId):
    if request.method == 'GET':
        return jsonify(chat_rooms.get(roomId, []))

    if request.method == 'POST':
        data = request.get_json()
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