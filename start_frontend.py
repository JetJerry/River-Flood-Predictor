#!/usr/bin/env python3
"""
Start the River Flood Prediction Frontend
"""
import subprocess
import sys
import os
import webbrowser
from pathlib import Path
import time

def main():
    """Start the frontend web server"""
    
    print("🌊 River Flood Prediction Frontend")
    print("=" * 50)
    
    # Check if frontend directory exists
    if not Path("frontend").exists():
        print("❌ Error: Frontend directory not found")
        print("   Please make sure the 'frontend' folder exists.")
        sys.exit(1)
    
    # Check if frontend files exist
    required_files = ["index.html", "styles.css", "script.js"]
    missing_files = []
    
    for file in required_files:
        if not Path(f"frontend/{file}").exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Error: Missing frontend files: {', '.join(missing_files)}")
        sys.exit(1)
    
    print("✓ Frontend files found")
    
    # Change to frontend directory
    os.chdir("frontend")
    
    print("\n🚀 Starting the frontend web server...")
    print("   Frontend URL: http://localhost:8080")
    print("   Make sure the backend API is running on http://localhost:8001")
    print("   Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Start a simple HTTP server
    try:
        # Try Python 3 first
        subprocess.run([
            sys.executable, "-m", "http.server", "8080"
        ])
    except KeyboardInterrupt:
        print("\n👋 Frontend server stopped. Goodbye!")

if __name__ == "__main__":
    main()
