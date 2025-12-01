# 🌊 River Flood Prediction System - Complete Setup Guide

This guide will help you set up and run the complete River Flood Prediction System, including both the backend API and frontend web interface.

## 📋 Prerequisites

- **Python 3.8+** (Download from [python.org](https://python.org))
- **pip** (Python package manager)
- **Web Browser** (Chrome, Firefox, Safari, Edge)

## 🚀 Quick Start (Recommended)

### Windows Users
```bash
# Double-click or run in Command Prompt
run_system.bat
```

### Linux/Mac Users
```bash
# Make executable and run
chmod +x run_system.sh
./run_system.sh
```

### Manual Start (All Platforms)
```bash
# Start complete system
python start_full_system.py
```

## 🔧 Detailed Setup

### Step 1: Verify Project Structure
Make sure you have the following structure:
```
River-Flood-Prediction_001/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── models/
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── start_full_system.py
├── start_backend.py
├── start_frontend.py
└── run_system.bat (Windows)
```

### Step 2: Install Backend Dependencies
```bash
cd backend
pip install -r requirements.txt
cd ..
```

### Step 3: Verify Model Files
Check if model files exist in one of these locations:
- `backend/models/best_model.keras`
- `Neural Network Classifier0/Neural Network Classifier_v7/best_model.keras`
- `Neural Network Classifier/best_model.keras`

### Step 4: Start the System
```bash
python start_full_system.py
```

## 🌐 Access the Application

Once running, open your browser and navigate to:

- **🌐 Frontend**: http://localhost:8080
- **🔧 Backend API**: http://localhost:8001
- **📚 API Documentation**: http://localhost:8001/docs
- **❤️ Health Check**: http://localhost:8001/health

## 🎯 How to Use

1. **Open the Frontend**: Go to http://localhost:8080
2. **Fill the Form**: Enter environmental and geographical data
3. **Use Sample Data**: Click "Fill Sample Data" for testing
4. **Get Prediction**: Click "Predict Flood Risk"
5. **View Results**: See the flood risk assessment

## 📊 Input Parameters

The system requires 13 parameters:

### Location Data
- **Latitude**: -90 to 90
- **Longitude**: -180 to 180
- **Elevation**: 0 to 10,000 meters

### Weather Conditions
- **Rainfall**: 0 to 1,000 mm
- **Temperature**: -50 to 60°C
- **Humidity**: 0 to 100%

### Water Conditions
- **River Discharge**: 0 to 10,000 m³/s
- **Water Level**: 0 to 50 meters

### Environmental Factors
- **Land Cover**: Water Body, Forest, Agricultural, Desert, Urban
- **Soil Type**: Clay, Peat, Loam, Sandy, Silt

### Socio-economic Factors
- **Population Density**: 0 to 50,000
- **Infrastructure**: Present (1) or Absent (0)
- **Historical Floods**: Present (1) or Absent (0)

## 🛠️ Alternative Startup Methods

### Method 1: Separate Services
```bash
# Terminal 1: Start Backend
python start_backend.py

# Terminal 2: Start Frontend
python start_frontend.py
```

### Method 2: Manual Start
```bash
# Backend
cd backend
python -m uvicorn app:app --host 0.0.0.0 --port 8001 --reload

# Frontend (new terminal)
cd frontend
python -m http.server 8080
```

### Method 3: Direct API Testing
```bash
# Test API directly
curl -X POST "http://localhost:8001/predict" \
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

## 🔍 Troubleshooting

### Common Issues

#### 1. Python Not Found
```bash
# Windows: Add Python to PATH
# Linux/Mac: Install python3
sudo apt install python3 python3-pip  # Ubuntu/Debian
brew install python3                   # macOS
```

#### 2. Port Already in Use
```bash
# Find process using port
netstat -ano | findstr :8001  # Windows
lsof -i :8001                 # Linux/Mac

# Kill process
taskkill /PID <PID> /F         # Windows
kill -9 <PID>                  # Linux/Mac
```

#### 3. Model Files Not Found
- Check if model files exist in the correct locations
- The API will run with limited functionality if models are missing
- Copy model files to `backend/models/` directory

#### 4. CORS Errors
- Ensure backend is running on port 8001
- Check that CORS is enabled in the backend
- Verify API endpoint URL in frontend JavaScript

#### 5. Frontend Not Loading
- Check if frontend files exist in `frontend/` directory
- Ensure web server is running on port 8080
- Clear browser cache and reload

### Debug Mode

#### Backend Debug
```bash
# Check backend logs
cd backend
python -m uvicorn app:app --host 0.0.0.0 --port 8001 --reload --log-level debug
```

#### Frontend Debug
- Open browser developer tools (F12)
- Check Console tab for JavaScript errors
- Check Network tab for API requests
- Verify API responses

#### API Testing
```bash
# Health check
curl http://localhost:8001/health

# API info
curl http://localhost:8001/info

# Test prediction
curl -X POST "http://localhost:8001/predict" \
     -H "Content-Type: application/json" \
     -d '{"latitude": 28.6139, "longitude": 77.2090, "elevation": 216.0, "rainfall": 150.5, "temperature": 25.3, "humidity": 65.0, "river_discharge": 2500.0, "water_level": 5.2, "land_cover": "Urban", "soil_type": "Clay", "population_density": 5000.0, "infrastructure": 1, "historical_floods": 0}'
```

## 📈 Performance Tips

### Backend Optimization
- Use production WSGI server (gunicorn) for deployment
- Enable model caching
- Configure proper logging levels

### Frontend Optimization
- Enable browser caching
- Use CDN for static assets
- Optimize images and CSS

### System Requirements
- **RAM**: 2GB+ recommended
- **CPU**: 2+ cores recommended
- **Storage**: 1GB+ free space
- **Network**: Local network access

## 🔒 Security Considerations

### Development
- API runs on localhost only
- No authentication required
- CORS enabled for local development

### Production Deployment
- Enable HTTPS
- Add authentication
- Configure proper CORS origins
- Use environment variables for secrets
- Enable request logging

## 📚 Additional Resources

### Documentation
- **API Documentation**: http://localhost:8001/docs
- **Frontend Guide**: [README_FRONTEND.md](README_FRONTEND.md)
- **Backend Guide**: [README.md](README.md)

### Support
- Check browser console for errors
- Verify API connectivity
- Review system logs
- Create an issue in the repository

## 🎯 Next Steps

1. **Test the System**: Use sample data to verify functionality
2. **Customize**: Modify frontend styling or backend parameters
3. **Deploy**: Set up production deployment
4. **Extend**: Add new features or models
5. **Monitor**: Set up logging and monitoring

## 🆘 Getting Help

If you encounter issues:

1. **Check Prerequisites**: Ensure Python and dependencies are installed
2. **Verify Structure**: Confirm all files are in the correct locations
3. **Test Components**: Try starting backend and frontend separately
4. **Check Logs**: Review console output for error messages
5. **Create Issue**: Report problems with detailed error messages

---

**🌊 River Flood Prediction System - Built for Educational Purposes**
