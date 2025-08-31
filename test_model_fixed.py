#!/usr/bin/env python3
"""
Fixed test to see what FastText model returns - handles NumPy compatibility
"""

import fasttext
import numpy as np

# Load model
MODEL_PATH = r"C:\Users\Yashu\Desktop\Project_new\lid.176.bin"

print("Loading model...")
model = fasttext.load_model(MODEL_PATH)
print("Model loaded!")

# Test some texts
test_texts = [
    "hello",
    "ನಮಸ್ಕಾರ",  # Kannada
    "నిఘంటుశోధన",  # Telugu
    "வணக்கம்",  # Tamil
    "घर",  # Hindi
]

for text in test_texts:
    print(f"\nText: '{text}'")
    try:
        # Use k=1 to get only the top prediction
        lang, prob = model.predict(text, k=1)
        print(f"Raw lang: {lang}")
        print(f"Raw prob: {prob}")
        print(f"Lang[0]: '{lang[0]}'")
        print(f"Prob[0]: {prob[0]}")
        
        # Try to clean the label
        clean_label = lang[0].replace("__label__", "")
        print(f"Cleaned label: '{clean_label}'")
        
    except Exception as e:
        print(f"Error: {e}")
        # Try alternative approach
        try:
            result = model.predict(text, k=1)
            print(f"Alternative result: {result}")
        except Exception as e2:
            print(f"Alternative also failed: {e2}")
