# 🔍 AI Fact Checker

An automated fact-checking web application that verifies claims in PDF documents against live web data using AI.

## 🌟 Features

- **PDF Upload**: Drag-and-drop interface for easy document upload
- **AI-Powered Extraction**: Automatically identifies verifiable claims using OpenRouter AI
- **Live Verification**: Cross-references claims against current web data via Tavily Search
- **Categorized Results**: Claims are classified as:
  - ✅ **Verified** - Matches current data
  - ⚠️ **Inaccurate** - Partially correct but outdated
  - ❌ **False** - Contradicts evidence or no evidence found
- **Source Citations**: Provides web sources for each verification

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenRouter API key (free tier available)
- Tavily API key (free tier available)

### Installation

1. **Clone or download this repository**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**

Create a `.env` file in the project root:
```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
FLASK_SECRET_KEY=your_random_secret_key_here
```

**Get your API keys:**
- **OpenRouter**: Visit [openrouter.ai](https://openrouter.ai/) and sign up for a free account
- **Tavily**: Visit [tavily.com](https://tavily.com/) and sign up for a free API key

4. **Run the application**
```bash
python app.py
```

5. **Open your browser**
Navigate to `http://localhost:5000`

## 📖 Usage

1. **Upload a PDF**: Drag and drop a PDF file or click to browse
2. **Wait for Processing**: The app will extract and verify claims (this may take 1-2 minutes)
3. **Review Results**: See verified, inaccurate, and false claims with evidence and sources
4. **Check Another Document**: Click "Check Another Document" to verify more files

## 🏗️ Project Structure

```
.
├── app.py                  # Main Flask application
├── config.py              # Configuration and API settings
├── pdf_processor.py       # PDF text extraction
├── claim_extractor.py     # AI-powered claim extraction
├── fact_verifier.py       # Web search and verification
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── templates/
│   ├── index.html        # Upload page
│   └── results.html      # Results display
└── static/
    ├── css/
    │   └── style.css     # Styling
    └── js/
        └── main.js       # Frontend logic
```

## 🔧 Configuration

Edit `config.py` to customize:
- **AI Model**: Change `OPENROUTER_MODEL` to use different free models
- **File Size Limit**: Adjust `MAX_FILE_SIZE_MB`
- **Upload Folder**: Change `UPLOAD_FOLDER` path

## 🌐 Deployment

### Deploy to Render

1. Create a `render.yaml`:
```yaml
services:
  - type: web
    name: fact-checker
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: OPENROUTER_API_KEY
        sync: false
      - key: TAVILY_API_KEY
        sync: false
      - key: FLASK_SECRET_KEY
        generateValue: true
```

2. Push to GitHub
3. Connect to Render and deploy

### Deploy to Railway

1. Push to GitHub
2. Connect to Railway
3. Add environment variables
4. Deploy automatically

## 🧪 Testing

Test with the provided `Assessment_Intern - Founder's Office AI (1).pdf` which contains intentional false claims about:
- Bitcoin prices
- AI model releases
- SpaceX missions
- Economic indicators

The app should correctly flag these as false or inaccurate.

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **PDF Processing**: pdfplumber
- **AI**: OpenRouter API (free models)
- **Search**: Tavily API
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Modern glassmorphism design

## 📝 License

MIT License - feel free to use for your projects!

## 🤝 Contributing

Contributions welcome! Please open an issue or submit a pull request.

## 📧 Support

For issues or questions, please open a GitHub issue.

---

**Built with ❤️ using OpenRouter AI & Tavily Search**
