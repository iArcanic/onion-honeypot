import secrets


# Flask secret key for session encryption 
FLASK_SESSION_SECRET_KEY = secrets.token_urlsafe(32)

# Logstash endpoint details
LOGSTASH_HOST = 'logstash'
LOGSTASH_PORT = '5514'
