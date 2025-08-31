#!/usr/bin/env python3
"""
Simple test script to verify FastText installation and model loading
"""

import fasttext
import os

def test_fasttext():
    print("🧪 Testing FastText installation...")
    
    # Test 1: Import fasttext
    try:
        import fasttext
        print("✅ FastText imported successfully")
    except ImportError as e:
        print(f"❌ FastText import failed: {e}")
        return False
    
    # Test 2: Check model file
    model_path = r"C:\Users\Yashu\Desktop\Project_new\lid.176.bin"
    if os.path.exists(model_path):
        print(f"✅ Model file found: {model_path}")
    else:
        print(f"❌ Model file not found: {model_path}")
        return False
    
    # Test 3: Load model
    try:
        print("Loading model...")
        model = fasttext.load_model(model_path)
        print("✅ Model loaded successfully")
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False
    
    # Test 4: Test prediction
    try:
        test_text = "hello"
        lang, prob = model.predict(test_text)
        print(f"✅ Test prediction: '{test_text}' → {lang[0]} (confidence: {prob[0]:.2f})")
    except Exception as e:
        print(f"❌ Prediction failed: {e}")
        return False
    
    print("🎉 All tests passed!")
    return True

if __name__ == "__main__":
    test_fasttext()
