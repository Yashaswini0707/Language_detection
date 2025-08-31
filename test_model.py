#!/usr/bin/env python3
"""
Simple test to see what FastText model returns
"""

import fasttext

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
    lang, prob = model.predict(text)
    print(f"Raw lang: {lang}")
    print(f"Raw prob: {prob}")
    print(f"Lang[0]: '{lang[0]}'")
    print(f"Prob[0]: {prob[0]}")
    
    # Try to clean the label
    clean_label = lang[0].replace("__label__", "")
    print(f"Cleaned label: '{clean_label}'")
