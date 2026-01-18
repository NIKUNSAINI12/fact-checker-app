"""
Setup script to configure environment variables
Run this script to set up your API keys
"""

import os

def setup_env():
    print("🔧 Fact Checker - Environment Setup\n")
    print("=" * 50)
    
    # Get API keys
    print("\n📝 Please enter your API keys:")
    print("\nGet OpenRouter API key from: https://openrouter.ai/")
    openrouter_key = input("OpenRouter API Key: ").strip()
    
    print("\nGet Tavily API key from: https://tavily.com/")
    tavily_key = input("Tavily API Key: ").strip()
    
    # Generate secret key
    import secrets
    secret_key = secrets.token_hex(32)
    
    # Create .env file
    env_content = f"""# OpenRouter API Configuration
OPENROUTER_API_KEY={openrouter_key}

# Tavily Search API Configuration
TAVILY_API_KEY={tavily_key}

# Flask Configuration
FLASK_SECRET_KEY={secret_key}
FLASK_ENV=development

# Upload Configuration
MAX_FILE_SIZE_MB=10
UPLOAD_FOLDER=uploads
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("\n✅ Environment file created successfully!")
    print("📁 File: .env")
    print("\n🚀 You can now run: python app.py")

if __name__ == "__main__":
    setup_env()
