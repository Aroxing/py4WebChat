import os
from dotenv import load_dotenv

load_dotenv()

# Define the applications folder
APPS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Define the URL prefix for your application
APP_NAME = "chat"

# Database settings
DB_URI = "sqlite://storage.db"

# Other py4web settings
DASHBOARD_MODE = "full"
DEFAULT_LOGIN_ENABLED = True

# OPENAI
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_MODEL = os.getenv('OPENAI_API_MODEL')
