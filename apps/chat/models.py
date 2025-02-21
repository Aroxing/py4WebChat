from .common import db, Field, auth
import datetime

# Define your database tables
db.define_table('chat_messages',
    Field('user_email'),
    Field('message', 'text'),
    Field('created_on', 'datetime', default=datetime.datetime.utcnow),
)

def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None 