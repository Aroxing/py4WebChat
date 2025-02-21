import os

# Get the absolute path of the app directory
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Create required directories if they don't exist
DB_FOLDER = os.path.join(APP_DIR, "databases")
T_FOLDER = os.path.join(APP_DIR, "translations")

os.makedirs(DB_FOLDER, exist_ok=True)
os.makedirs(T_FOLDER, exist_ok=True)

# Define the applications folder
APP_NAME = "chat"
APP_AUTHOR = "Your Name"
APP_DESC = "Chat Application"
APP_KEYWORDS = "chat,websockets"

# Database settings
DB_URI = "sqlite://storage.db"
DB_POOL_SIZE = 1
DB_MIGRATE = True
DB_FAKE_MIGRATE = False

# Authentication settings
SESSION_SECRET_KEY = "ASDSDFASD%w#5235465__#1"  # Change this!
VERIFY_EMAIL = False
LOGIN_AFTER_REGISTRATION = True
ALLOWED_ACTIONS = ["all"]
DEFAULT_LOGIN_ENABLED = True

# Email settings (if needed)
SMTP_SSL = False
SMTP_SERVER = None
SMTP_SENDER = "you@example.com"
SMTP_LOGIN = None
SMTP_TLS = False

# Logging settings
LOGGERS = [
    "debug:stdout"
]  # format is level:filename

# OpenAI settings
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_MODEL = os.getenv('OPENAI_API_MODEL')

# Add these settings
AUTH_METHOD = "local" 