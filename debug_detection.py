#!/usr/bin/env python3
"""
Debug script to test language detection and see what FastText returns
"""

import fasttext
import os

# Path to your model
MODEL_PATH = r"C:\Users\Yashu\Desktop\Project_new\lid.176.bin"

# Mapping ISO codes to Indian language names
lang_map = {
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
    "sd": "Sindhi"
}

def debug_detection():
    print("🔍 Debugging Language Detection")
    print("=" * 50)
    
    # Check if model exists
    if not os.path.exists(MODEL_PATH):
        print(f"❌ Model file not found: {MODEL_PATH}")
        return
    
    # Load model
    try:
        print("Loading model...")
        model = fasttext.load_model(MODEL_PATH)
        print("✅ Model loaded successfully")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return
    
    # Test texts with expected languages
    test_cases = [
        ("ನಮಸ್ಕಾರ", "Kannada"),
        ("నిఘంటుశోధన", "Telugu"),
        ("hello", "English"),
        ("घर", "Hindi"),
        ("வணக்கம்", "Tamil"),
        ("നമസ്കാരം", "Malayalam"),
        ("नमस्कार", "Marathi"),
        ("নমস্কার", "Bengali"),
        ("નમસ્તે", "Gujarati"),
        ("ਸਤ ਸ੍ਰੀ ਅਕਾਲ", "Punjabi")
    ]
    
    print("\n🧪 Testing Language Detection:")
    print("-" * 50)
    
    for text, expected_lang in test_cases:
        try:
            # Get raw prediction
            lang, prob = model.predict(text)
            
            # Debug: Print raw output
            print(f"\n📝 Text: '{text}' (Expected: {expected_lang})")
            print(f"🔍 Raw lang output: {lang}")
            print(f"🔍 Raw prob output: {prob}")
            
            # Try different label removal patterns
            raw_label = lang[0]
            print(f"🔍 Raw label: '{raw_label}'")
            
            # Try different replacement patterns
            patterns = [
                ("__label__", ""),
                ("_label_", ""),
                ("label_", ""),
                ("__label", ""),
                ("label", "")
            ]
            
            for pattern, replacement in patterns:
                code = raw_label.replace(pattern, replacement)
                name = lang_map.get(code, f"Unknown ({code})")
                print(f"   Pattern '{pattern}' → '{replacement}': {code} → {name}")
            
            # Use the correct pattern (double underscores)
            code = raw_label.replace("__label__", "")
            name = lang_map.get(code, f"Unknown ({code})")
            confidence = prob[0]
            
            print(f"✅ Final result: {name} (confidence: {confidence:.3f})")
            
            if name == expected_lang:
                print("🎯 CORRECT!")
            else:
                print(f"❌ WRONG! Expected: {expected_lang}")
                
        except Exception as e:
            print(f"❌ Error processing '{text}': {e}")
    
    print("\n" + "=" * 50)
    print("🔍 Debug complete!")

if __name__ == "__main__":
    debug_detection()
