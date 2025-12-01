#!/usr/bin/env python3
"""
Start the River Flood Prediction Backend API
"""
import subprocess
import sys
import os
from pathlib import Path

def main():
    """Start the backend API server"""
    
    print("🌊 River Flood Prediction Backend API")
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
        import tensorflow
        print("✓ Backend dependencies found")
    except ImportError as e:
        print(f"📦 Installing missing dependencies: {e}")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed")
    
    # Check if model files exist
    model_files = [
        "models/best_model.keras",
        "../Neural Network Classifier0/Neural Network Classifier_v7/best_model.keras",
        "../Neural Network Classifier/best_model.keras"
    ]
    
    model_found = False
    for model_path in model_files:
        if Path(model_path).exists():
            print(f"✓ Model found: {model_path}")
            model_found = True
            break
    
    if not model_found:
        print("⚠ Warning: No model files found. The API will run with limited functionality.")
        print("   Make sure model files are in the correct location.")
    
    # Check normalization parameters
    if Path("Normalized_param.json").exists():
        print("✓ Normalization parameters found")
    else:
        print("⚠ Warning: Normalized_param.json not found")
    
    print("\n🚀 Starting the backend API server...")
    print("   API Documentation: http://localhost:8001/docs")
    print("   Health Check: http://localhost:8001/health")
    print("   API Endpoint: http://localhost:8001/predict")
    print("   Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Start the server
    try:
        subprocess.run([
            sys.executable, "-m", "uvicorn", 
            "app:app", 
            "--host", "0.0.0.0", 
            "--port", "8001", 
            "--reload"
        ])
    except KeyboardInterrupt:
        print("\n👋 Backend server stopped. Goodbye!")

if __name__ == "__main__":
    main()
