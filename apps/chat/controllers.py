"""
Chat application controllers
"""
from py4web import action, request, redirect, URL

from cls.chat_gpt_handler import ChatGPTHandler
from .common import db, auth, logger
from .models import get_user_email

# Initialize ChatGPT handler
chat_handler = ChatGPTHandler(logger)


# Default route - redirects to index
@action('/')
@action.uses(auth)
def default():
    redirect(URL('index'))


# Main chat interface
@action('index')
@action.uses('index.html', auth.user, db)
def index():
    return dict(
        user_email=get_user_email(),
        chat_url=URL('chat'),
        load_messages_url=URL('load_messages'),
        sio_url='http://localhost:8001'  # Socket.IO server URL
    )


@action('chat', method=['POST'])
@action.uses(db, auth.user)
def chat():
    message = request.json.get('message')
    user_email = get_user_email()
    if message:
        # Save message to database
        db.chat_messages.insert(
            user_email=user_email,
            message=message
        )
        return dict(status='success')
    return dict(status='error')


@action('load_messages')
@action.uses(db, auth.user)
def load_messages():
    messages = db(db.chat_messages).select(orderby=db.chat_messages.created_on)
    return dict(messages=[
        {'user': m.user_email, 'message': m.message, 'created_on': m.created_on}
        for m in messages
    ])
