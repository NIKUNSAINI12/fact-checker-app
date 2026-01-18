import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration"""
    
    # Flask
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # OpenRouter API
    OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
    OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
    # Using OpenAI GPT-OSS-120B - free model on OpenRouter
    OPENROUTER_MODEL = "openai/gpt-oss-120b:free"
    
    # Tavily Search API
    TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
    
    # Upload settings
    UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
    MAX_FILE_SIZE_MB = int(os.getenv('MAX_FILE_SIZE_MB', 10))
    MAX_CONTENT_LENGTH = MAX_FILE_SIZE_MB * 1024 * 1024
    ALLOWED_EXTENSIONS = {'pdf'}
    
    @staticmethod
    def init_app(app):
        """Initialize application"""
        os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
