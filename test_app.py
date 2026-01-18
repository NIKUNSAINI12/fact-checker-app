"""
Simple test endpoint to verify environment variables are loaded
"""
from flask import Flask, jsonify
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/test-env')
def test_env():
    """Test if environment variables are loaded"""
    return jsonify({
        'OPENROUTER_API_KEY_SET': bool(os.getenv('OPENROUTER_API_KEY')),
        'OPENROUTER_API_KEY_LENGTH': len(os.getenv('OPENROUTER_API_KEY', '')),
        'TAVILY_API_KEY_SET': bool(os.getenv('TAVILY_API_KEY')),
        'TAVILY_API_KEY_LENGTH': len(os.getenv('TAVILY_API_KEY', '')),
        'FLASK_SECRET_KEY_SET': bool(os.getenv('FLASK_SECRET_KEY')),
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
