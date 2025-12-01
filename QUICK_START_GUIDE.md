# River Flood Prediction API - Quick Start Guide

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### 1. Install Dependencies

```bash
# Navigate to the backend directory
cd backend

# Install required packages
pip install -r requirements.txt
```

### 2. Setup Model Files

```bash
# Run the setup script to copy model files
python scripts/setup_models.py
```

### 3. Start the API Server

```bash
# Option 1: Using the run script
python run.py

# Option 2: Using uvicorn directly
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Option 3: From project root
python start_api.py
```

### 4. Access the API

Once the server is running, you can access:

- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health
- **API Info**: http://localhost:8000/info

## 🧪 Test the API

### Quick Test with cURL

```bash
# Health check
curl http://localhost:8000/health

# Make a prediction
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

### Test with Python

```python
import requests

# Test health endpoint
response = requests.get("http://localhost:8000/health")
print("Health Status:", response.json())

# Test prediction endpoint
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

response = requests.post("http://localhost:8000/predictions/predict", json=data)
result = response.json()
print("Prediction:", result)
```


## 📊 API Endpoints Summary

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint with API info |
| GET | `/health` | Basic health check |
| GET | `/health/detailed` | Detailed system status |
| GET | `/info` | API information |
| POST | `/predictions/predict` | Single flood prediction |
| POST | `/predictions/predict/batch` | Batch flood predictions |
| GET | `/predictions/models/available` | Available models info |

## 🔧 Configuration

Create a `.env` file in the backend directory:

```env
# API Configuration
APP_NAME=River Flood Prediction API
DEBUG=false
HOST=0.0.0.0
PORT=8000

# Model Configuration
MODEL_PATH=models
NEURAL_NETWORK_MODEL=best_model.keras
NORMALIZATION_PARAMS=Normalized_param.json
```

## 🧪 Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run tests
pytest tests/
```

## 📝 Input Data Format

The API expects the following data format for predictions:

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

## 🚨 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Install dependencies with `pip install -r requirements.txt`
2. **Model not found**: Run `python scripts/setup_models.py` to copy model files
3. **Port already in use**: Change the port in configuration or kill the process using port 8000
4. **Models not loaded**: Check that model files exist in the `models/` directory

### Check Model Files

```bash
# Check if model files exist
ls -la models/
ls -la Normalized_param.json
```

### View Logs

```bash
# Logs appear in the terminal when running the server
```

## 📚 Additional Resources

- **Full API Documentation**: [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
- **Project README**: [README.md](README.md)
- **Interactive Docs**: http://localhost:8000/docs (when server is running)

## 🆘 Support

If you encounter issues:

1. Check the health endpoint: `GET /health`
2. Review the logs for error messages
3. Ensure all dependencies are installed
4. Verify model files are in the correct location
5. Check the interactive documentation at `/docs`

## 🎯 Next Steps

1. **Test the API**: Use the interactive documentation at `/docs`
2. **Integrate**: Use the API in your applications
3. **Monitor**: Use health check endpoints for monitoring
4. **Scale**: Run multiple instances for production use
5. **Extend**: Add new features or models as needed
