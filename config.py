# Configuration settings for Python application

# Database configuration
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'username': 'admin',
    'password': 'password',
    'database': 'sample_db'
}

# API configuration
API_CONFIG = {
    'base_url': 'https://api.example.com',
    'api_key': 'your_api_key_here',
    'timeout': 30  # in seconds
}

# Logging configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'file': '/var/log/app.log',
    'max_size': 10 * 1024 * 1024,  # 10 MB
    'backup_count': 5
}
