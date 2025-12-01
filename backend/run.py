#!/usr/bin/env python3
"""
Simple run script for River Flood Prediction API
"""
import uvicorn
import sys
import os
from pathlib import Path

def main():
    print("🌊 River Flood Prediction API - College Project")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("app.py").exists():
        print("❌ Error: app.py not found. Please run from backend directory.")
        sys.exit(1)
    
    print("🚀 Starting the API server...")
    print("   API Documentation: http://localhost:8001/docs")
    print("   Health Check: http://localhost:8001/health")
    print("   Press Ctrl+C to stop the server")
    print("-" * 50)
    
    try:
        uvicorn.run(
            "app:app",
            host="0.0.0.0",
            port=8001,
            reload=True,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 Server stopped. Goodbye!")

if __name__ == "__main__":
    main()