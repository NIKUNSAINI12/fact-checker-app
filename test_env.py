"""Test if environment variables are loaded"""
import os
from dotenv import load_dotenv

load_dotenv()

print("Testing environment variables:")
print(f"OPENROUTER_API_KEY: {os.getenv('OPENROUTER_API_KEY')[:20] if os.getenv('OPENROUTER_API_KEY') else 'NOT SET'}...")
print(f"TAVILY_API_KEY: {os.getenv('TAVILY_API_KEY')[:20] if os.getenv('TAVILY_API_KEY') else 'NOT SET'}...")
print(f"FLASK_SECRET_KEY: {os.getenv('FLASK_SECRET_KEY')}")
