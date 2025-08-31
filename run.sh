#!/bin/bash

echo "🚀 Starting Language Detection Tool..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies if needed
if ! python -c "import flask" 2>/dev/null; then
    echo "📦 Installing Flask dependencies..."
    pip install flask flask-cors
fi

# Start the server
echo "🌐 Starting server..."
echo "Backend will be available at: http://localhost:5000"
echo "Frontend will open automatically..."
echo ""
echo "Press Ctrl+C to stop the server"

# Start the simple app and open frontend
python app_simple.py &
sleep 2
open index.html

# Wait for the background process
wait
