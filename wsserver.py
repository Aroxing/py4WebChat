import socketio
import eventlet

# Create Socket.IO server
sio = socketio.Server(
    cors_allowed_origins='*',
    async_mode='eventlet'
)

# Create WSGI app
app = socketio.WSGIApp(sio)

@sio.on('connect')
def connect(sid, environ):
    print(f'Client connected: {sid}')

@sio.on('disconnect')
def disconnect(sid):
    print(f'Client disconnected: {sid}')

@sio.on('to_py4web')
def message(sid, data):
    print(f'Message from {sid}:', data)
    # Broadcast the message to all clients except sender
    sio.emit('py4web_echo', data, skip_sid=sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('localhost', 8001)), app) 