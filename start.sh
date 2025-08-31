#!/bin/bash

echo "🚀 Starting Language Detection Tool..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7+ first."
    exit 1
fi

# Check if the model file exists
MODEL_PATH = r"C:\Users\Yashu\Desktop\Project_new\lid.176.bin"
if [ ! -f "$MODEL_PATH" ]; then
    echo "❌ FastText model not found at $MODEL_PATH"
    echo "Please download the lid.176.bin file and place it in your Downloads folder."
    exit 1
fi

# Install dependencies if requirements.txt exists
if [ -f "requirements.txt" ]; then
    echo "📦 Installing Python dependencies..."
    pip3 install -r requirements.txt
fi

# Start the Flask backend
echo "🔧 Starting Flask backend server..."
python3 app.py &

# Wait a moment for the server to start
sleep 3

# Open the frontend in the default browser
echo "🌐 Opening frontend in browser..."
if command -v open &> /dev/null; then
    open index.html
elif command -v xdg-open &> /dev/null; then
    xdg-open index.html
else
    echo "📝 Please open index.html in your web browser manually"
fi

echo "✅ Language Detection Tool is ready!"
echo "Backend running on: http://localhost:5000"
echo "Frontend: index.html"
echo ""
echo "Press Ctrl+C to stop the server"
