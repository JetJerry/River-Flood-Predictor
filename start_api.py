#!/usr/bin/env python3
"""
Quick start script for the River Flood Prediction API
"""
import subprocess
import sys
import os
from pathlib import Path

def main():
    """Start the API with proper setup"""
    
    print("🌊 River Flood Prediction API - Quick Start")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("backend").exists():
        print("❌ Error: Please run this script from the project root directory")
        print("   The 'backend' folder should be visible from here.")
        sys.exit(1)
    
    # Change to backend directory
    os.chdir("backend")
    
    # Check if requirements are installed
    try:
        import fastapi
        import uvicorn
        print("✓ FastAPI dependencies found")
    except ImportError:
        print("📦 Installing dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed")
    
    # Setup models
    print("🔧 Setting up model files...")
    try:
        subprocess.run([sys.executable, "scripts/setup_models.py"], check=True)
        print("✓ Model files set up")
    except subprocess.CalledProcessError:
        print("⚠ Warning: Could not set up model files automatically")
        print("   You may need to copy model files manually")
    
    print("\n🚀 Starting the API server...")
    print("   API Documentation: http://localhost:8000/docs")
    print("   Health Check: http://localhost:8000/health")
    print("   Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Start the server
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "app.main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000", 
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")

if __name__ == "__main__":
    main()
