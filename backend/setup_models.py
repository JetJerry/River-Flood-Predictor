#!/usr/bin/env python3
"""
Simple script to copy model files
"""
import shutil
from pathlib import Path

def setup_models():
    """Copy model files to the backend directory"""
    print("Setting up model files...")
    
    # Define paths
    project_root = Path("..")
    backend_dir = Path(".")
    
    # Model file paths
    model_sources = [
        project_root / "Neural Network Classifier0" / "Neural Network Classifier_v7" / "best_model.keras",
        project_root / "Neural Network Classifier" / "best_model.keras",
    ]
    
    # Create models directory
    models_dir = backend_dir / "models"
    models_dir.mkdir(exist_ok=True)
    
    # Copy neural network model
    model_copied = False
    for source in model_sources:
        if source.exists():
            dest = models_dir / "best_model.keras"
            shutil.copy2(source, dest)
            print(f"Copied model: {source} -> {dest}")
            model_copied = True
            break
    
    if not model_copied:
        print("Warning: Neural network model not found")
    
    # Copy normalization parameters
    norm_params_source = project_root / "Normalized_param.json"
    if norm_params_source.exists():
        dest = backend_dir / "Normalized_param.json"
        shutil.copy2(norm_params_source, dest)
        print(f"Copied normalization parameters: {norm_params_source} -> {dest}")
    else:
        print("Warning: Normalization parameters not found")
    
    print("\nModel setup completed!")
    print(f"Models directory: {models_dir}")

if __name__ == "__main__":
    setup_models()
