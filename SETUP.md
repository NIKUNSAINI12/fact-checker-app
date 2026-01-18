# Setup Instructions

## Get Your API Keys

### 1. OpenRouter API Key (Free)
1. Visit https://openrouter.ai/
2. Sign up for a free account
3. Go to "Keys" section
4. Create a new API key
5. Copy the key (starts with `sk-or-v1-...`)

### 2. Tavily API Key (Free)
1. Visit https://tavily.com/
2. Sign up for a free account
3. Go to your dashboard
4. Copy your API key (starts with `tvly-...`)

## Configure the Application

1. Open the `.env` file in the project root
2. Replace the placeholder values with your actual API keys:

```
OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here
TAVILY_API_KEY=tvly-your-actual-key-here
FLASK_SECRET_KEY=any-random-string-here
```

3. Save the file

## Install and Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

The app will be available at http://localhost:5000
