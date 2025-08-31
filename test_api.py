#!/usr/bin/env python3
"""
Test script for the Language Detection API
"""

import requests
import json
import time

def test_api():
    base_url = "http://localhost:5000/api"
    
    print("🧪 Testing Language Detection API...")
    
    # Test health endpoint
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
        else:
            print("❌ Health check failed")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure the Flask app is running.")
        return False
    
    # Test samples endpoint
    try:
        response = requests.get(f"{base_url}/samples")
        if response.status_code == 200:
            samples = response.json()
            print(f"✅ Samples endpoint working ({len(samples)} samples)")
        else:
            print("❌ Samples endpoint failed")
            return False
    except Exception as e:
        print(f"❌ Error testing samples: {e}")
        return False
    
    # Test detection endpoint
    test_texts = [
        "ನಮಸ್ಕಾರ",  # Kannada
        "hello",     # English
        "வணக்கம்",   # Tamil
    ]
    
    for text in test_texts:
        try:
            response = requests.post(
                f"{base_url}/detect",
                json={"text": text},
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ '{text}' → {result['language']} ({result['confidence_percentage']}%)")
            else:
                print(f"❌ Detection failed for '{text}': {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Error testing detection for '{text}': {e}")
            return False
    
    print("\n🎉 All tests passed! The API is working correctly.")
    return True

if __name__ == "__main__":
    test_api()
