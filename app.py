from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import uuid
from werkzeug.utils import secure_filename
from config import Config
from pdf_processor import PDFProcessor
from claim_extractor import ClaimExtractor
from fact_verifier import FactVerifier

app = Flask(__name__)
app.config.from_object(Config)
Config.init_app(app)

# Initialize processors
pdf_processor = PDFProcessor()
claim_extractor = ClaimExtractor()
fact_verifier = FactVerifier()

# Store results temporarily (in production, use Redis or database)
results_store = {}

@app.route('/')
def index():
    """Home page with upload interface"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle PDF upload and processing"""
    try:
        # Check if file is present
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        
        # Validate file
        pdf_processor.validate_pdf(file)
        
        # Save file
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)
        
        # Process PDF
        try:
            # Extract text
            text = pdf_processor.extract_text(filepath)
            
            # Extract claims
            claims = claim_extractor.extract_claims(text)
            
            if not claims:
                return jsonify({
                    'error': 'No verifiable claims found in the document'
                }), 400
            
            # Verify claims
            results = fact_verifier.verify_all_claims(claims)
            
            # Generate result ID
            result_id = str(uuid.uuid4())
            results_store[result_id] = {
                'filename': filename,
                'results': results,
                'total_claims': len(claims)
            }
            
            # Clean up uploaded file
            os.remove(filepath)
            
            return jsonify({
                'success': True,
                'result_id': result_id,
                'redirect': url_for('show_results', result_id=result_id)
            })
            
        except Exception as e:
            # Clean up file on error
            if os.path.exists(filepath):
                os.remove(filepath)
            raise e
            
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500

@app.route('/results/<result_id>')
def show_results(result_id):
    """Display verification results"""
    if result_id not in results_store:
        return redirect(url_for('index'))
    
    data = results_store[result_id]
    return render_template('results.html', 
                         filename=data['filename'],
                         results=data['results'],
                         total_claims=data['total_claims'])

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
