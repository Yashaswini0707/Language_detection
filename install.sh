#!/bin/bash

echo "🔧 Installing Language Detection Tool dependencies..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7+ first."
    exit 1
fi

# Upgrade pip first
echo "📦 Upgrading pip..."
python3 -m pip install --upgrade pip

# Install basic dependencies first
echo "📦 Installing basic dependencies..."
python3 -m pip install flask==2.3.3 flask-cors==4.0.0 requests==2.31.0 gunicorn==21.2.0

# Try different fasttext installation methods
echo "📦 Installing fasttext..."

# Method 1: Try fasttext-wheel (pre-compiled)
echo "Trying fasttext-wheel..."
python3 -m pip install fasttext-wheel==0.9.2

if [ $? -eq 0 ]; then
    echo "✅ fasttext-wheel installed successfully!"
else
    echo "fasttext-wheel failed, trying alternative method..."
    
    # Method 2: Install pybind11 first, then fasttext
    echo "Installing pybind11..."
    python3 -m pip install pybind11==2.11.1
    
    echo "Trying fasttext with pybind11..."
    python3 -m pip install fasttext==0.9.2
    
    if [ $? -eq 0 ]; then
        echo "✅ fasttext installed successfully!"
    else
        echo "❌ fasttext installation failed. Trying conda method..."
        
        # Method 3: Try conda if available
        if command -v conda &> /dev/null; then
            echo "Using conda to install fasttext..."
            conda install -c conda-forge fasttext -y
        else
            echo "❌ All installation methods failed."
            echo "Please try one of these manual methods:"
            echo "1. Install via conda: conda install -c conda-forge fasttext"
            echo "2. Install via brew: brew install fasttext"
            echo "3. Download pre-compiled wheel from: https://pypi.org/project/fasttext-wheel/"
            exit 1
        fi
    fi
fi

echo "✅ All dependencies installed successfully!"
echo ""
echo "You can now run the application with:"
echo "python3 app.py"
