# River Flood Prediction API - College Project

A simple FastAPI backend for predicting river flood occurrences using machine learning models.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### 2. Setup Model Files
```bash
python setup_models.py
```

### 3. Run the API
```bash
python run.py
```

### 4. Access the API
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 📁 Project Structure (Simplified)

```
backend/
├── app.py              # Main API application (everything in one file)
├── requirements.txt    # Python dependencies
├── run.py             # Simple run script
├── setup_models.py    # Model setup script
└── models/            # Model files (created by setup)
    └── best_model.keras
```

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root endpoint with API info |
| `/health` | GET | Health check |
| `/predict` | POST | Make flood prediction |
| `/info` | GET | API information |
| `/docs` | GET | Interactive documentation |

## 🧪 Example Usage

### Python Example
```python
import requests

# Make a prediction
data = {
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

response = requests.post("http://localhost:8000/predict", json=data)
result = response.json()
print(f"Flood Prediction: {result['prediction']}")
print(f"Probability: {result['probability']:.2f}")
print(f"Confidence: {result['confidence']}")
```

### cURL Example
```bash
curl -X POST "http://localhost:8000/predict" \
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

## 📝 Input Data Format

```json
{
  "latitude": 28.6139,           // -90 to 90
  "longitude": 77.2090,          // -180 to 180
  "elevation": 216.0,            // 0 to 10000 meters
  "rainfall": 150.5,             // 0 to 1000 mm
  "temperature": 25.3,           // -50 to 60 °C
  "humidity": 65.0,              // 0 to 100 %
  "river_discharge": 2500.0,     // 0 to 10000 m³/s
  "water_level": 5.2,            // 0 to 50 meters
  "land_cover": "Urban",         // Water Body, Forest, Agricultural, Desert, Urban
  "soil_type": "Clay",           // Clay, Peat, Loam, Sandy, Silt
  "population_density": 5000.0,  // 0 to 50000
  "infrastructure": 1,           // 0 or 1
  "historical_floods": 0         // 0 or 1
}
```

## 📈 Expected Response

```json
{
  "prediction": 1,               // 0: No flood, 1: Flood
  "probability": 0.75,           // 0 to 1
  "confidence": "High",          // Low, Medium, High
  "model_used": "Neural Network Classifier v7",
  "processing_time": 0.045       // seconds
}
```

## 🔧 Features

- **Single File Application**: Everything in `app.py` for simplicity
- **Automatic Model Loading**: Loads your trained neural network model
- **Data Validation**: Input validation using Pydantic
- **Interactive Documentation**: Swagger UI at `/docs`
- **Health Monitoring**: Health check endpoint
- **Error Handling**: Proper error responses

## 🚨 Troubleshooting

### Model Not Found
```bash
# Run the setup script
python setup_models.py
```

### Dependencies Missing
```bash
# Install requirements
pip install -r requirements.txt
```

### Port Already in Use
Change the port in `run.py` or kill the process using port 8000.

## 📚 What's Inside app.py

The `app.py` file contains:
1. **Data Models** - Pydantic schemas for validation
2. **Model Service** - Model loading and prediction logic
3. **FastAPI App** - API endpoints and configuration
4. **Error Handling** - Proper error responses

Everything is in one file for easy understanding and modification.

## 🎯 Perfect for College Projects

- ✅ **Simple Structure** - Easy to understand and modify
- ✅ **Single File** - Everything in one place
- ✅ **Well Documented** - Clear code with comments
- ✅ **Interactive Docs** - Automatic API documentation
- ✅ **Easy to Run** - Just 3 commands to get started
- ✅ **Professional** - Uses industry-standard FastAPI
