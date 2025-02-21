"""
This file defines cache, session, and translator T object for the app
These are fixtures that every app needs so probably you will not be editing this file
"""
import logging
import sys

from py4web import Session, Cache, Translator, DAL, URL
from py4web.utils.auth import Auth
from py4web.utils.factories import ActionFactory

from . import settings

# implement custom loggers form settings.LOGGERS
logger = logging.getLogger("py4web:" + settings.APP_NAME)
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)
for item in settings.LOGGERS:
    level, filename = item.split(":", 1)
    if filename in ("stdout", "stderr"):
        handler = logging.StreamHandler(getattr(sys, filename))
    else:
        handler = logging.FileHandler(filename)
    handler.setFormatter(formatter)
    logger.setLevel(getattr(logging, level.upper(), "DEBUG"))
    logger.addHandler(handler)

# connect to db
db = DAL(
    settings.DB_URI,
    folder=settings.DB_FOLDER,
    pool_size=settings.DB_POOL_SIZE,
    migrate=settings.DB_MIGRATE,
    fake_migrate=settings.DB_FAKE_MIGRATE,
)

# define global objects that may or may not be used by th actions
cache = Cache(size=1000)
T = Translator(settings.T_FOLDER)

# pick the session type that suits you best
session = Session(secret=settings.SESSION_SECRET_KEY)

# Configure Auth
auth = Auth(session, db, define_tables=True)
auth.use_username = True
auth.param.registration_requires_confirmation = False
auth.param.registration_requires_approval = False
auth.param.login_after_registration = True
auth.param.allowed_actions = settings.ALLOWED_ACTIONS
auth.param.login_expiration_time = 3600  # 1 hour

# Simplified password settings
auth.param.password_complexity = {}  # Remove complexity requirements
auth.param.block_previous_password_num = 3

# Set default redirection URLs
auth.next = URL('index')  # This will handle both login and logout redirects

auth.enable()

# define convenience action that handles auth
action = ActionFactory(db, session, auth, T)
