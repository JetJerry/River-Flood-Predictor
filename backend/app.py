"""
Simple River Flood Prediction API for College Project
"""
import json
import time
import logging
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
import numpy as np
import pandas as pd
import tensorflow as tf
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =============================================================================
# DATA MODELS
# =============================================================================

class LandCoverType(str, Enum):
    WATER_BODY = "Water Body"
    FOREST = "Forest"
    AGRICULTURAL = "Agricultural"
    DESERT = "Desert"
    URBAN = "Urban"

class SoilType(str, Enum):
    CLAY = "Clay"
    PEAT = "Peat"
    LOAM = "Loam"
    SANDY = "Sandy"
    SILT = "Silt"

class FloodPredictionRequest(BaseModel):
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    elevation: float = Field(..., ge=0, le=10000)
    rainfall: float = Field(..., ge=0, le=1000)
    temperature: float = Field(..., ge=-50, le=60)
    humidity: float = Field(..., ge=0, le=100)
    river_discharge: float = Field(..., ge=0, le=10000)
    water_level: float = Field(..., ge=0, le=50)
    land_cover: LandCoverType
    soil_type: SoilType
    population_density: float = Field(..., ge=0, le=50000)
    infrastructure: int = Field(..., ge=0, le=1)
    historical_floods: int = Field(..., ge=0, le=1)

class FloodPredictionResponse(BaseModel):
    prediction: int = Field(..., description="0: No flood, 1: Flood")
    probability: float = Field(..., ge=0, le=1)
    confidence: str = Field(..., description="Low, Medium, High")
    model_used: str
    processing_time: float

# =============================================================================
# MODEL SERVICE
# =============================================================================

class ModelService:
    def __init__(self):
        self.model = None
        self.normalization_params = None
        self.model_loaded = False
        
        # Feature mappings
        self.land_cover_mapping = {
            LandCoverType.WATER_BODY: 1,
            LandCoverType.FOREST: 2,
            LandCoverType.AGRICULTURAL: 3,
            LandCoverType.DESERT: 4,
            LandCoverType.URBAN: 5
        }
        
        self.soil_type_mapping = {
            SoilType.CLAY: 1,
            SoilType.PEAT: 2,
            SoilType.LOAM: 3,
            SoilType.SANDY: 4,
            SoilType.SILT: 5
        }
        
        self.feature_order = [
            'latitude', 'longitude', 'rainfall', 'temperature', 'humidity',
            'river_discharge', 'water_level', 'elevation', 'land_cover',
            'soil_type', 'population_density', 'infrastructure', 'historical_floods'
        ]
    
    async def load_model(self) -> bool:
        """Load the trained model and normalization parameters"""
        try:
            # Load normalization parameters
            params_path = Path("Normalized_param.json")
            if params_path.exists():
                with open(params_path, 'r') as f:
                    self.normalization_params = json.load(f)
                logger.info("Normalization parameters loaded")
            
            # Load neural network model with custom objects
            model_paths = [
                Path("models/best_model.keras"),
                Path("../Neural Network Classifier0/Neural Network Classifier_v7/best_model.keras"),
                Path("../Neural Network Classifier/best_model.keras")
            ]
            
            for model_path in model_paths:
                if model_path.exists():
                    try:
                        # Try loading with custom objects to handle compatibility
                        self.model = tf.keras.models.load_model(
                            str(model_path), 
                            custom_objects=None,
                            compile=False
                        )
                        logger.info(f"Model loaded from: {model_path}")
                        self.model_loaded = True
                        return True
                    except Exception as model_error:
                        logger.warning(f"Failed to load model from {model_path}: {str(model_error)}")
                        continue
            
            logger.warning("Model not found or could not be loaded")
            return False
            
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            return False
    
    def _preprocess_data(self, request: FloodPredictionRequest) -> np.ndarray:
        """Preprocess input data for prediction"""
        # Convert to dictionary
        data_dict = request.dict()
        
        # Map categorical variables
        data_dict['land_cover'] = self.land_cover_mapping[data_dict['land_cover']]
        data_dict['soil_type'] = self.soil_type_mapping[data_dict['soil_type']]
        
        # Create feature array
        features = np.array([data_dict[feature] for feature in self.feature_order])
        
        # Normalize if parameters available
        if self.normalization_params:
            normalized_features = np.zeros_like(features)
            for i, feature in enumerate(self.feature_order):
                if feature in self.normalization_params:
                    min_val = self.normalization_params[feature]['min']
                    max_val = self.normalization_params[feature]['max']
                    if max_val - min_val != 0:
                        normalized_features[i] = (features[i] - min_val) / (max_val - min_val)
                    else:
                        normalized_features[i] = 0.0
                else:
                    normalized_features[i] = features[i]
            features = normalized_features
        
        return features.reshape(1, -1)
    
    async def predict(self, request: FloodPredictionRequest) -> Tuple[int, float, str]:
        """Make flood prediction"""
        if not self.model_loaded:
            raise RuntimeError("Model not loaded")
        
        try:
            # Preprocess data
            features = self._preprocess_data(request)
            
            # Make prediction
            prob = self.model.predict(features, verbose=0)[0][0]
            prediction = 1 if prob > 0.5 else 0
            probability = float(prob)
            
            # Determine confidence
            if probability > 0.8 or probability < 0.2:
                confidence = "High"
            elif probability > 0.6 or probability < 0.4:
                confidence = "Medium"
            else:
                confidence = "Low"
            
            return prediction, probability, confidence
            
        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            raise RuntimeError(f"Prediction failed: {str(e)}")

# =============================================================================
# FASTAPI APPLICATION
# =============================================================================

app = FastAPI(
    title="River Flood Prediction API",
    description="Simple API for predicting river flood occurrences",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize model service
model_service = ModelService()

@app.on_event("startup")
async def startup_event():
    """Load model on startup"""
    logger.info("Starting River Flood Prediction API...")
    success = await model_service.load_model()
    if success:
        logger.info("Model loaded successfully")
    else:
        logger.warning("Model loading failed - API will run with limited functionality")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "River Flood Prediction API",
        "version": "1.0.0",
        "status": "running",
        "model_loaded": model_service.model_loaded,
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy" if model_service.model_loaded else "degraded",
        "model_loaded": model_service.model_loaded,
        "timestamp": time.time()
    }

@app.post("/predict", response_model=FloodPredictionResponse)
async def predict_flood(request: FloodPredictionRequest):
    """Make flood prediction"""
    try:
        start_time = time.time()
        
        if not model_service.model_loaded:
            raise HTTPException(
                status_code=503,
                detail="Model not loaded. Please try again later."
            )
        
        prediction, probability, confidence = await model_service.predict(request)
        processing_time = time.time() - start_time
        
        return FloodPredictionResponse(
            prediction=prediction,
            probability=probability,
            confidence=confidence,
            model_used="Neural Network Classifier v7",
            processing_time=processing_time
        )
        
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/info")
async def api_info():
    """Get API information"""
    return {
        "api_name": "River Flood Prediction API",
        "version": "1.0.0",
        "model_loaded": model_service.model_loaded,
        "features": model_service.feature_order,
        "endpoints": {
            "predict": "/predict",
            "health": "/health",
            "docs": "/docs"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
