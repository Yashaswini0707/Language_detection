from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import fasttext
import os
import sys

app = Flask(__name__)
CORS(app)

# Path to your model
MODEL_PATH = r"C:\Users\Yashu\Desktop\Project_new\lid.176.bin"

# Global model variable
model = None

# Comprehensive language mapping
lang_map = {
    # Indian languages
    "en": "English",
    "kn": "Kannada",
    "te": "Telugu",
    "hi": "Hindi",
    "ta": "Tamil",
    "ml": "Malayalam",
    "mr": "Marathi",
    "bn": "Bengali",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "ur": "Urdu",
    "as": "Assamese",
    "or": "Odia",
    "sa": "Sanskrit",
    "ne": "Nepali",
    "bh": "Bihari",
    "mai": "Maithili",
    "gom": "Goan Konkani",
    "bpy": "Bishnupriya Manipuri",
    "sd": "Sindhi",
    
    # Common language codes that might be returned
    "eng": "English",
    "kan": "Kannada",
    "tel": "Telugu",
    "hin": "Hindi",
    "tam": "Tamil",
    "mal": "Malayalam",
    "mar": "Marathi",
    "ben": "Bengali",
    "guj": "Gujarati",
    "pan": "Punjabi",
    "urd": "Urdu",
    "asm": "Assamese",
    "ori": "Odia",
    "san": "Sanskrit",
    "nep": "Nepali",
}

def load_model():
    """Load the FastText model with error handling"""
    global model
    try:
        print("Loading FastText model...")
        if not os.path.exists(MODEL_PATH):
            print(f"❌ Model file not found: {MODEL_PATH}")
            return False
        model = fasttext.load_model(MODEL_PATH)
        print("✅ Model loaded successfully")
        return True
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return False

def detect_language(text):
    """Detect language with NumPy compatibility fix"""
    try:
        if model is None:
            return "Model not loaded", 0.0
        
        print(f"🔍 Detecting language for: '{text}'")
        
        # Use k=1 to avoid NumPy compatibility issues
        lang, prob = model.predict(text, k=1)
        print(f"🔍 Raw output - lang: {lang}, prob: {prob}")
        
        raw_label = lang[0]
        print(f"🔍 Raw label: '{raw_label}'")
        
        # Try different label cleaning patterns
        code = None
        patterns_to_try = [
            "__label__",
            "_label_", 
            "label_",
            "__label",
            "label"
        ]
        
        for pattern in patterns_to_try:
            if pattern in raw_label:
                code = raw_label.replace(pattern, "")
                print(f"🔍 Using pattern '{pattern}' → code: '{code}'")
                break
        
        # If no pattern matched, use the raw label
        if code is None:
            code = raw_label
            print(f"🔍 No pattern matched, using raw label: '{code}'")
        
        # Get language name
        name = lang_map.get(code, f"Unknown ({code})")
        confidence = prob[0]
        
        print(f"🔍 Final result: {name} (confidence: {confidence:.3f})")
        return name, confidence
        
    except Exception as e:
        print(f"❌ Error in detection: {e}")
        # Try alternative approach
        try:
            print("🔄 Trying alternative prediction method...")
            result = model.predict(text, k=1)
            print(f"🔄 Alternative result: {result}")
            
            # Extract from alternative result
            if isinstance(result, tuple) and len(result) == 2:
                alt_lang, alt_prob = result
                raw_label = alt_lang[0] if alt_lang else "unknown"
                confidence = alt_prob[0] if alt_prob else 0.0
                
                # Clean label
                code = raw_label.replace("__label__", "")
                name = lang_map.get(code, f"Unknown ({code})")
                
                print(f"🔄 Alternative final result: {name} (confidence: {confidence:.3f})")
                return name, confidence
            else:
                return f"Unknown (raw: {result})", 0.0
                
        except Exception as e2:
            print(f"❌ Alternative method also failed: {e2}")
            return "Error", 0.0

@app.route('/')
def index():
    """Serve the test page"""
    return send_file('simple_test.html')

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    try:
        model_status = model is not None
        return jsonify({
            'status': 'healthy',
            'model_loaded': model_status,
            'model_path': MODEL_PATH,
            'python_version': sys.version
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/samples', methods=['GET'])
def get_samples():
    """Get sample texts"""
    try:
        samples = [
            {"text": "hello", "language": "English", "description": "Greeting"},
            {"text": "ನಮಸ್ಕಾರ", "language": "Kannada", "description": "Hello"},
            {"text": "வணக்கம்", "language": "Tamil", "description": "Hello"},
            {"text": "घर", "language": "Hindi", "description": "Home"},
        ]
        return jsonify(samples)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/detect', methods=['POST'])
def detect():
    """Detect language endpoint"""
    try:
        print("📥 Received detection request")
        
        # Get request data
        data = request.get_json()
        if not data:
            print("❌ No JSON data received")
            return jsonify({'error': 'No JSON data received'}), 400
        
        text = data.get('text', '')
        if not text:
            print("❌ No text provided")
            return jsonify({'error': 'No text provided'}), 400
        
        print(f"📝 Processing text: '{text}'")
        
        # Detect language
        lang_name, confidence = detect_language(text)
        
        # Prepare response
        response_data = {
            'text': text,
            'language': lang_name,
            'confidence': round(confidence, 4),
            'confidence_percentage': round(confidence * 100, 2)
        }
        
        print(f"📤 Sending response: {response_data}")
        return jsonify(response_data)
        
    except Exception as e:
        print(f"❌ Error in detect endpoint: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🚀 Starting Fixed Language Detection API")
    print(f"📁 Model path: {MODEL_PATH}")
    
    # Load model
    if load_model():
        print("✅ Ready to serve requests")
    else:
        print("⚠️  Model failed to load, but API will still run")
    
    print("🌐 Access the test page at: http://localhost:5000")
    print("🔧 API endpoints:")
    print("   - GET  /api/health")
    print("   - GET  /api/samples")
    print("   - POST /api/detect")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
