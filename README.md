# Py4web Chat Application

A real-time chat application built with py4web and Socket.IO. Features user authentication, persistent message storage,
and real-time updates.

## Features

- Real-time chat using Socket.IO
- User authentication and registration
- Message persistence in SQLite database
- Clean and responsive UI using Bulma CSS
- Support for multiple simultaneous users

## Requirements

- Python 3.11
- py4web
- python-socketio
- eventlet
- python-dotenv

## Running the Application

1. Start the Socket.IO server:

```bash
python wsserver.py
```

2. In a new terminal, start py4web:

```bash
py4web run apps
```

3. Open your browser and navigate to `http://localhost:8000/chat`
4. Register a new user or login with an existing account