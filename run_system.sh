#!/bin/bash

echo "🌊 River Flood Prediction System - Linux/Mac Launcher"
echo "=================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "   Please install Python 3.8+ from your package manager"
    exit 1
fi

echo "✓ Python found"

# Check if we're in the right directory
if [ ! -d "backend" ]; then
    echo "❌ Error: Backend directory not found"
    echo "   Please run this script from the project root directory"
    exit 1
fi

if [ ! -d "frontend" ]; then
    echo "❌ Error: Frontend directory not found"
    echo "   Please run this script from the project root directory"
    exit 1
fi

echo "✓ Project structure found"

# Make Python scripts executable
chmod +x start_full_system.py
chmod +x start_backend.py
chmod +x start_frontend.py

# Start the complete system
echo ""
echo "🚀 Starting the complete River Flood Prediction System..."
echo "   This will start both the backend API and frontend web interface"
echo ""
echo "   Backend API: http://localhost:8001"
echo "   Frontend: http://localhost:8080"
echo "   API Documentation: http://localhost:8001/docs"
echo ""
echo "   Press Ctrl+C to stop all services"
echo ""

python3 start_full_system.py

echo ""
echo "👋 System stopped. Goodbye!"
