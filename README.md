# 🌊 River Flood Prediction System

A complete flood prediction system with both backend API and frontend web interface. The system uses machine learning models to predict river flood occurrences based on environmental and geographical factors.

## 🎯 System Components

- **🔧 Backend API**: FastAPI-based service with machine learning models
- **🎨 Frontend Web Interface**: Modern, responsive web application
- **📊 Prediction Engine**: Neural Network and Random Forest classifiers
- **📱 Mobile Responsive**: Works on desktop, tablet, and mobile devices

## 🌊 Features

### Backend API
- **Single Prediction**: Predict flood occurrence for individual locations
- **Batch Prediction**: Process multiple predictions in a single request
- **Multiple Models**: Support for Neural Network and Random Forest classifiers
- **Data Validation**: Comprehensive input validation using Pydantic
- **Health Monitoring**: Health check endpoints for service monitoring
- **Auto Documentation**: Interactive API documentation with Swagger UI
- **Error Handling**: Robust error handling and logging

### Frontend Web Interface
- **Modern UI**: Clean, responsive design with gradient backgrounds
- **Comprehensive Form**: All 13 required parameters with validation
- **Real-time Status**: Live API connection status
- **Visual Results**: Color-coded flood risk indicators
- **Sample Data**: One-click sample data filling
- **Mobile Responsive**: Works on all device sizes

## 🚀 Quick Start

### Option 1: Complete System (Recommended)
```bash
# Windows
run_system.bat

# Linux/Mac
chmod +x run_system.sh
./run_system.sh

# All Platforms
python start_full_system.py
```

### Option 2: Manual Setup
1. **Install dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   cd ..
   ```

2. **Start Backend API**
   ```bash
   python start_backend.py
   ```

3. **Start Frontend** (in another terminal)
   ```bash
   python start_frontend.py
   ```

4. **Access the System**
   - **Frontend**: http://localhost:8080
   - **Backend API**: http://localhost:8001
   - **API Documentation**: http://localhost:8001/docs

## 📊 API Endpoints

### Health & Status
- `GET /health` - Basic health check
- `GET /health/detailed` - Detailed system status
- `GET /health/models` - Model information
- `POST /health/models/reload` - Reload models (admin)

### Predictions
- `POST /predictions/predict` - Single flood prediction
- `POST /predictions/predict/batch` - Batch flood predictions
- `GET /predictions/models/available` - Available models info

### Information
- `GET /` - Root endpoint with API info
- `GET /info` - Detailed API information

## 🔧 Configuration

The API can be configured using environment variables or a `.env` file:

```env
# API Configuration
APP_NAME="River Flood Prediction API"
APP_VERSION="1.0.0"
DEBUG=false

# Server Configuration
HOST=0.0.0.0
PORT=8000

# Model Configuration
MODEL_PATH=models
NEURAL_NETWORK_MODEL=best_model.keras
NORMALIZATION_PARAMS=Normalized_param.json

# Security
SECRET_KEY=your-secret-key-change-in-production
```

## 📝 Usage Examples

### Single Prediction

```python
import requests

# Example prediction request
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

response = requests.post(
    "http://localhost:8000/predictions/predict",
    json=data
)

result = response.json()
print(f"Flood Prediction: {result['prediction']}")
print(f"Probability: {result['probability']:.2f}")
print(f"Confidence: {result['confidence']}")
```

### Batch Prediction

```python
import requests

# Example batch prediction request
data = {
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
        },
        # Add more predictions...
    ]
}

response = requests.post(
    "http://localhost:8000/predictions/predict/batch",
    json=data
)

results = response.json()
print(f"Processed {results['total_processed']} predictions")
```

### Using cURL

```bash
# Single prediction
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

# Health check
curl -X GET "http://localhost:8000/health"
```


## 📊 Input Data Schema

### Required Features

| Feature | Type | Range | Description |
|---------|------|-------|-------------|
| `latitude` | float | -90 to 90 | Latitude coordinate |
| `longitude` | float | -180 to 180 | Longitude coordinate |
| `elevation` | float | 0 to 10000 | Elevation in meters |
| `rainfall` | float | 0 to 1000 | Rainfall in mm |
| `temperature` | float | -50 to 60 | Temperature in Celsius |
| `humidity` | float | 0 to 100 | Humidity percentage |
| `river_discharge` | float | 0 to 10000 | River discharge in m³/s |
| `water_level` | float | 0 to 50 | Water level in meters |
| `land_cover` | enum | Water Body, Forest, Agricultural, Desert, Urban | Land cover type |
| `soil_type` | enum | Clay, Peat, Loam, Sandy, Silt | Soil type |
| `population_density` | float | 0 to 50000 | Population density |
| `infrastructure` | int | 0 or 1 | Infrastructure presence |
| `historical_floods` | int | 0 or 1 | Historical flood occurrence |

### Response Schema

```json
{
  "prediction": 1,
  "probability": 0.75,
  "confidence": "High",
  "model_used": "Neural Network Classifier v7",
  "processing_time": 0.045
}
```

## 🔍 Model Information

### Neural Network Classifier (v7)
- **Architecture**: 128 → 64 → 1 neurons
- **Activation**: ReLU (hidden), Sigmoid (output)
- **Regularization**: Dropout (0.4), L2 regularization
- **Optimizer**: Adam (lr=0.001)
- **Accuracy**: ~65%

### Random Forest Classifier
- **Type**: Ensemble method
- **Features**: All 13 input features
- **Accuracy**: ~60%

## 🛠️ Development

### Project Structure

```
backend/
├── app/
│   ├── api/                 # API endpoints
│   │   ├── health.py       # Health check endpoints
│   │   └── predictions.py  # Prediction endpoints
│   ├── models/             # Pydantic models
│   │   └── schemas.py      # Request/response schemas
│   ├── services/           # Business logic
│   │   └── model_service.py # Model loading and prediction
│   ├── middleware/         # Custom middleware
│   ├── utils/              # Utility functions
│   ├── config.py           # Configuration
│   └── main.py             # FastAPI application
├── tests/                  # Test files
├── requirements.txt        # Python dependencies
```

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-asyncio

# Run tests
pytest tests/
```

### Code Quality

```bash
# Format code
black backend/

# Lint code
flake8 backend/

# Type checking
mypy backend/
```

## 📈 Performance

- **Single Prediction**: ~50ms average response time
- **Batch Prediction**: ~10ms per prediction
- **Concurrent Requests**: Supports multiple simultaneous requests
- **Memory Usage**: ~500MB with models loaded

## 🔒 Security

- Input validation and sanitization
- CORS configuration
- Request logging and monitoring
- Error handling without information leakage

## 📚 API Documentation

The API provides comprehensive documentation through:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the repository
- Check the API documentation
- Review the health check endpoints

## 🔄 Version History

- **v1.0.0**: Initial release with Neural Network and Random Forest models
- Support for single and batch predictions
- Comprehensive API documentation
