import os
from py4web import action, request, abort, redirect, URL
from py4web.utils.factories import ActionFactory
from .common import db, session, T, cache, auth, logger

# Initialize database
db.commit()

# Import controllers (after db initialization)
from . import controllers 