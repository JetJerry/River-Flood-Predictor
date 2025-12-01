#!/usr/bin/env python3
"""
Start the complete River Flood Prediction System (Backend + Frontend)
"""
import subprocess
import sys
import os
import threading
import time
import webbrowser
from pathlib import Path

def start_backend():
    """Start the backend API server"""
    print("🔧 Starting Backend API...")
    os.chdir("backend")
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "app:app", 
            "--host", "0.0.0.0", 
            "--port", "8001", 
            "--reload"
        ])
    except KeyboardInterrupt:
        print("Backend stopped")

def start_frontend():
    """Start the frontend web server"""
    print("🎨 Starting Frontend...")
    os.chdir("frontend")
    try:
        subprocess.run([
            sys.executable, "-m", "http.server", "8080"
        ])
    except KeyboardInterrupt:
        print("Frontend stopped")

def check_backend_health():
    """Check if backend is running"""
    import requests
    try:
        response = requests.get("http://localhost:8001/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def main():
    """Start the complete system"""
    
    print("🌊 River Flood Prediction System - Complete Setup")
    print("=" * 60)
    
    # Check if we're in the right directory
    if not Path("backend").exists() or not Path("frontend").exists():
        print("❌ Error: Please run this script from the project root directory")
        print("   Both 'backend' and 'frontend' folders should be visible from here.")
        sys.exit(1)
    
    # Check dependencies
    print("📦 Checking dependencies...")
    try:
        import fastapi
        import uvicorn
        import tensorflow
        print("✓ Backend dependencies found")
    except ImportError:
        print("📦 Installing backend dependencies...")
        os.chdir("backend")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        os.chdir("..")
        print("✓ Backend dependencies installed")
    
    # Check model files
    model_files = [
        "backend/models/best_model.keras",
        "Neural Network Classifier0/Neural Network Classifier_v7/best_model.keras",
        "Neural Network Classifier/best_model.keras"
    ]
    
    model_found = False
    for model_path in model_files:
        if Path(model_path).exists():
            print(f"✓ Model found: {model_path}")
            model_found = True
            break
    
    if not model_found:
        print("⚠ Warning: No model files found. The API will run with limited functionality.")
    
    print("\n🚀 Starting the complete system...")
    print("   Backend API: http://localhost:8001")
    print("   Frontend: http://localhost:8080")
    print("   API Documentation: http://localhost:8001/docs")
    print("   Press Ctrl+C to stop all services")
    print("-" * 60)
    
    # Start backend in a separate thread
    backend_thread = threading.Thread(target=start_backend, daemon=True)
    backend_thread.start()
    
    # Wait a bit for backend to start
    print("⏳ Waiting for backend to start...")
    time.sleep(3)
    
    # Check if backend is running
    if check_backend_health():
        print("✓ Backend API is running")
    else:
        print("⚠ Backend may not be fully ready yet")
    
    # Start frontend in a separate thread
    frontend_thread = threading.Thread(target=start_frontend, daemon=True)
    frontend_thread.start()
    
    # Wait a bit for frontend to start
    time.sleep(2)
    
    # Open browser
    print("🌐 Opening browser...")
    try:
        webbrowser.open("http://localhost:8080")
    except:
        print("   Please manually open: http://localhost:8080")
    
    print("\n✅ System is running!")
    print("   - Backend API: http://localhost:8001")
    print("   - Frontend: http://localhost:8080")
    print("   - API Docs: http://localhost:8001/docs")
    print("\n   Press Ctrl+C to stop all services")
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Shutting down all services...")
        print("   Goodbye!")

if __name__ == "__main__":
    main()
