# Fact Checker - AI-Powered Document Verification

A web application that automatically verifies factual claims in PDF documents by cross-referencing them with current web data.

## About This Project

This application was built to solve a common problem: verifying the accuracy of information in documents. It takes a PDF file, extracts factual claims using AI, searches the web for current information, and categorizes each claim as verified, inaccurate, or false.

The motivation came from seeing how easily misinformation spreads. This tool helps quickly identify outdated statistics, false claims, and verify facts against current sources.

## How It Works

1. **Upload a PDF** - Drag and drop any PDF document
2. **Automatic Extraction** - The system identifies specific claims like statistics, dates, and financial figures
3. **Web Verification** - Each claim is checked against current web sources
4. **Clear Results** - Claims are categorized with evidence and source citations

## Tech Stack

**Backend:**
- Flask for the web framework
- OpenRouter API for AI-powered claim extraction
- Tavily Search API for real-time web verification
- pdfplumber for PDF text extraction

**Frontend:**
- Vanilla JavaScript for interactivity
- Modern CSS with responsive design
- Drag-and-drop file upload

## Getting Started

### Prerequisites

- Python 3.8 or higher
- API keys from OpenRouter and Tavily (both offer free tiers)

### Installation

1. Clone this repository
```bash
git clone https://github.com/NIKUNSAINI12/fact-checker-app.git
cd fact-checker-app
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up environment variables

Create a `.env` file in the project root:
```
OPENROUTER_API_KEY=your_openrouter_key
TAVILY_API_KEY=your_tavily_key
FLASK_SECRET_KEY=your_secret_key
```

Get your API keys:
- OpenRouter: https://openrouter.ai/
- Tavily: https://tavily.com/

4. Run the application
```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## Project Structure

```
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── pdf_processor.py      # PDF text extraction
├── claim_extractor.py    # AI claim identification
├── fact_verifier.py      # Web search and verification
├── templates/            # HTML templates
├── static/              # CSS and JavaScript
└── requirements.txt     # Python dependencies
```

## Features

- **Smart Claim Detection**: Automatically identifies verifiable facts in documents
- **Real-Time Verification**: Searches current web sources for accurate information
- **Source Citations**: Provides links to sources for each verification
- **User-Friendly Interface**: Clean, modern design with drag-and-drop upload
- **Detailed Results**: Shows why each claim was categorized as verified, inaccurate, or false

## Deployment

The app can be deployed to various platforms:

**Railway** (Recommended):
1. Connect your GitHub repository
2. Add environment variables in the dashboard
3. Deploy automatically

**Render**:
1. Create a new Web Service
2. Connect your repository
3. Add environment variables
4. Deploy

Note: Free tier deployments may have memory limitations for processing large PDFs.

## Development Notes

This project uses:
- OpenRouter's free models for cost-effective AI processing
- Tavily's search API for reliable web verification
- Gunicorn for production deployment
- Environment-based configuration for security

## License

MIT License - feel free to use this project for your own purposes.

## Acknowledgments

Built as a demonstration of combining AI capabilities with web search to create practical verification tools.
