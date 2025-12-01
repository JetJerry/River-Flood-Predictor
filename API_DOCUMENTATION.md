# River Flood Prediction API Documentation

## Overview

The River Flood Prediction API is a FastAPI-based service that provides machine learning-powered flood prediction capabilities. The API accepts environmental and geographical data and returns flood occurrence predictions with confidence levels.

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, the API does not require authentication. In production, consider implementing API keys or JWT tokens.

## Content Type

All requests and responses use `application/json`.

## Error Handling

The API uses standard HTTP status codes and returns error details in the following format:

```json
{
  "error": "ErrorType",
  "message": "Human-readable error message",
  "details": {
    "field": "Additional error details"
  }
}
```

## Endpoints

### 1. Health Check

#### GET /health

Check the basic health status of the API.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "version": "1.0.0",
  "models_loaded": true
}
```

#### GET /health/detailed

Get detailed health information including model status and system capabilities.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z",
  "version": "1.0.0",
  "service_info": {
    "name": "River Flood Prediction API",
    "description": "API for predicting river flood occurrences",
    "debug_mode": false
  },
  "models": {
    "neural_network": {
      "loaded": true,
      "status": "ready"
    },
    "random_forest": {
      "loaded": false,
      "status": "not_loaded"
    },
    "normalization": {
      "loaded": true,
      "status": "ready"
    }
  },
  "capabilities": {
    "single_prediction": true,
    "batch_prediction": true,
    "feature_preprocessing": true,
    "categorical_mapping": true
  }
}
```

### 2. Predictions

#### POST /predictions/predict

Make a single flood prediction.

**Parameters:**
- `model_type` (query, optional): Model to use (`neural_network` or `random_forest`). Default: `neural_network`

**Request Body:**
```json
{
  "latitude": 28.6139,
  "longitude": 77.2090,
  "elevation": 216.0,
  "rainfall": 150.5,
  "temperature": 25.3,
  "humidity": 65.0,
  "river_discharge": 2500.0,
  "water_level": 5.2,
  "land_cover": "Urban",
  "soil_type": "Clay",
  "population_density": 5000.0,
  "infrastructure": 1,
  "historical_floods": 0
}
```

**Response:**
```json
{
  "prediction": 1,
  "probability": 0.75,
  "confidence": "High",
  "model_used": "Neural Network Classifier v7",
  "processing_time": 0.045
}
```

#### POST /predictions/predict/batch

Make multiple flood predictions in a single request.

**Parameters:**
- `model_type` (query, optional): Model to use (`neural_network` or `random_forest`). Default: `neural_network`

**Request Body:**
```json
{
  "predictions": [
    {
      "latitude": 28.6139,
      "longitude": 77.2090,
      "elevation": 216.0,
      "rainfall": 150.5,
      "temperature": 25.3,
      "humidity": 65.0,
      "river_discharge": 2500.0,
      "water_level": 5.2,
      "land_cover": "Urban",
      "soil_type": "Clay",
      "population_density": 5000.0,
      "infrastructure": 1,
      "historical_floods": 0
    }
  ]
}
```

**Response:**
```json
{
  "predictions": [
    {
      "prediction": 1,
      "probability": 0.75,
      "confidence": "High",
      "model_used": "Neural Network Classifier v7",
      "processing_time": 0.045
    }
  ],
  "total_processed": 1,
  "processing_time": 0.045
}
```

#### GET /predictions/models/available

Get information about available prediction models.

**Response:**
```json
{
  "available_models": [
    {
      "name": "Neural Network Classifier",
      "version": "v7",
      "type": "Binary Classification",
      "description": "Deep learning model with 128-64-1 architecture",
      "features": {
        "input_shape": [null, 13],
        "output_shape": [null, 1],
        "total_params": 10241
      }
    }
  ],
  "total_models": 1,
  "normalization_available": true,
  "features_used": [
    "latitude", "longitude", "rainfall", "temperature",
    "humidity", "river_discharge", "water_level", "elevation",
    "land_cover", "soil_type", "population_density",
    "infrastructure", "historical_floods"
  ]
}
```

### 3. Information

#### GET /

Get basic API information.

**Response:**
```json
{
  "message": "Welcome to River Flood Prediction API",
  "version": "1.0.0",
  "description": "API for predicting river flood occurrences using machine learning models",
  "docs_url": "/docs",
  "health_check": "/health",
  "models_loaded": true
}
```

#### GET /info

Get detailed API information.

**Response:**
```json
{
  "api": {
    "name": "River Flood Prediction API",
    "version": "1.0.0",
    "description": "API for predicting river flood occurrences using machine learning models",
    "host": "0.0.0.0",
    "port": 8000,
    "debug": false
  },
  "models": {
    "neural_network_loaded": true,
    "random_forest_loaded": false,
    "normalization_loaded": true
  },
  "features": {
    "total_features": 13,
    "feature_list": [
      "latitude", "longitude", "rainfall", "temperature",
      "humidity", "river_discharge", "water_level", "elevation",
      "land_cover", "soil_type", "population_density",
      "infrastructure", "historical_floods"
    ]
  },
  "endpoints": {
    "health": "/health",
    "predictions": "/predictions",
    "docs": "/docs",
    "redoc": "/redoc"
  }
}
```

## Data Schema

### Input Features

| Field | Type | Range/Options | Description |
|-------|------|---------------|-------------|
| `latitude` | float | -90 to 90 | Latitude coordinate |
| `longitude` | float | -180 to 180 | Longitude coordinate |
| `elevation` | float | 0 to 10000 | Elevation in meters |
| `rainfall` | float | 0 to 1000 | Rainfall in mm |
| `temperature` | float | -50 to 60 | Temperature in Celsius |
| `humidity` | float | 0 to 100 | Humidity percentage |
| `river_discharge` | float | 0 to 10000 | River discharge in m³/s |
| `water_level` | float | 0 to 50 | Water level in meters |
| `land_cover` | string | Water Body, Forest, Agricultural, Desert, Urban | Land cover type |
| `soil_type` | string | Clay, Peat, Loam, Sandy, Silt | Soil type |
| `population_density` | float | 0 to 50000 | Population density |
| `infrastructure` | integer | 0 or 1 | Infrastructure presence |
| `historical_floods` | integer | 0 or 1 | Historical flood occurrence |

### Output Schema

| Field | Type | Description |
|-------|------|-------------|
| `prediction` | integer | Flood prediction (0: No flood, 1: Flood) |
| `probability` | float | Probability of flood occurrence (0 to 1) |
| `confidence` | string | Confidence level (Low, Medium, High) |
| `model_used` | string | Model used for prediction |
| `processing_time` | float | Processing time in seconds |

## Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request - Invalid input data |
| 422 | Validation Error - Request validation failed |
| 500 | Internal Server Error |
| 503 | Service Unavailable - Models not loaded |

## Rate Limiting

Currently, no rate limiting is implemented.

## Examples

### Python Example

```python
import requests
import json

# API base URL
base_url = "http://localhost:8000"

# Sample prediction data
prediction_data = {
    "latitude": 28.6139,
    "longitude": 77.2090,
    "elevation": 216.0,
    "rainfall": 150.5,
    "temperature": 25.3,
    "humidity": 65.0,
    "river_discharge": 2500.0,
    "water_level": 5.2,
    "land_cover": "Urban",
    "soil_type": "Clay",
    "population_density": 5000.0,
    "infrastructure": 1,
    "historical_floods": 0
}

# Make prediction
response = requests.post(
    f"{base_url}/predictions/predict",
    json=prediction_data
)

if response.status_code == 200:
    result = response.json()
    print(f"Flood Prediction: {'Flood' if result['prediction'] == 1 else 'No Flood'}")
    print(f"Probability: {result['probability']:.2f}")
    print(f"Confidence: {result['confidence']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

### JavaScript Example

```javascript
const baseUrl = 'http://localhost:8000';

const predictionData = {
    latitude: 28.6139,
    longitude: 77.2090,
    elevation: 216.0,
    rainfall: 150.5,
    temperature: 25.3,
    humidity: 65.0,
    river_discharge: 2500.0,
    water_level: 5.2,
    land_cover: "Urban",
    soil_type: "Clay",
    population_density: 5000.0,
    infrastructure: 1,
    historical_floods: 0
};

fetch(`${baseUrl}/predictions/predict`, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(predictionData)
})
.then(response => response.json())
.then(data => {
    console.log('Flood Prediction:', data.prediction === 1 ? 'Flood' : 'No Flood');
    console.log('Probability:', data.probability.toFixed(2));
    console.log('Confidence:', data.confidence);
})
.catch(error => {
    console.error('Error:', error);
});
```

### cURL Example

```bash
curl -X POST "http://localhost:8000/predictions/predict" \
     -H "Content-Type: application/json" \
     -d '{
       "latitude": 28.6139,
       "longitude": 77.2090,
       "elevation": 216.0,
       "rainfall": 150.5,
       "temperature": 25.3,
       "humidity": 65.0,
       "river_discharge": 2500.0,
       "water_level": 5.2,
       "land_cover": "Urban",
       "soil_type": "Clay",
       "population_density": 5000.0,
       "infrastructure": 1,
       "historical_floods": 0
     }'
```

## Interactive Documentation

The API provides interactive documentation through Swagger UI and ReDoc:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## Support

For support and questions:
- Check the health endpoints for service status
- Review the interactive documentation
- Create an issue in the repository

## Version History

- **v1.0.0**: Initial release with Neural Network and Random Forest models
- Support for single and batch predictions
- Comprehensive API documentation
