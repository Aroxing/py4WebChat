#!/usr/bin/env python
from apps.chat.controllers import app  # Import the Socket.IO wrapped app

if __name__ == '__main__':
    import waitress
    waitress.serve(app, host='0.0.0.0', port=8000) 