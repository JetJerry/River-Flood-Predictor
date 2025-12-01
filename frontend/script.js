// River Flood Prediction Frontend JavaScript
class FloodPredictionApp {
    constructor() {
        this.apiBaseUrl = 'http://localhost:8001'; // Backend API URL
        this.isLoading = false;
        this.init();
    }

    init() {
        this.bindEvents();
        this.checkApiStatus();
        this.loadApiInfo();
        this.loadModelInfo();
    }

    bindEvents() {
        // Form submission
        document.getElementById('predictionForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.handlePrediction();
        });

        // Sample data button
        document.getElementById('fillSampleData').addEventListener('click', () => {
            this.fillSampleData();
        });

        // Clear form button
        document.getElementById('clearForm').addEventListener('click', () => {
            this.clearForm();
        });
    }

    async checkApiStatus() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/health`);
            const data = await response.json();
            
            const statusIndicator = document.getElementById('statusIndicator');
            const statusText = document.getElementById('statusText');
            
            if (response.ok && data.status === 'healthy') {
                statusIndicator.className = 'status-indicator connected';
                statusText.textContent = 'API Connected';
            } else {
                statusIndicator.className = 'status-indicator error';
                statusText.textContent = 'API Error';
            }
        } catch (error) {
            const statusIndicator = document.getElementById('statusIndicator');
            const statusText = document.getElementById('statusText');
            statusIndicator.className = 'status-indicator error';
            statusText.textContent = 'API Offline';
            console.error('API check failed:', error);
        }
    }

    async loadApiInfo() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/info`);
            const data = await response.json();
            
            const apiInfoDiv = document.getElementById('apiInfo');
            apiInfoDiv.innerHTML = `
                <div class="info-item">
                    <span class="info-label">API Name:</span>
                    <span class="info-value">${data.api_name || 'River Flood Prediction API'}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Version:</span>
                    <span class="info-value">${data.version || '1.0.0'}</span>
                </div>
                <div class="info-item">
                    <span class="info-label">Model Status:</span>
                    <span class="info-value ${data.model_loaded ? 'text-success' : 'text-danger'}">
                        ${data.model_loaded ? 'Loaded' : 'Not Loaded'}
                    </span>
                </div>
                <div class="info-item">
                    <span class="info-label">Features:</span>
                    <span class="info-value">${data.features ? data.features.length : 13} parameters</span>
                </div>
            `;
        } catch (error) {
            document.getElementById('apiInfo').innerHTML = '<p class="text-danger">Failed to load API information</p>';
            console.error('Failed to load API info:', error);
        }
    }

    async loadModelInfo() {
        try {
            // Try to get model information from the API
            const response = await fetch(`${this.apiBaseUrl}/predictions/models/available`);
            if (response.ok) {
                const data = await response.json();
                const modelInfoDiv = document.getElementById('modelInfo');
                modelInfoDiv.innerHTML = `
                    <div class="info-item">
                        <span class="info-label">Model Type:</span>
                        <span class="info-value">${data.available_models[0]?.name || 'Neural Network'}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Version:</span>
                        <span class="info-value">${data.available_models[0]?.version || 'v7'}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Type:</span>
                        <span class="info-value">${data.available_models[0]?.type || 'Binary Classification'}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Features:</span>
                        <span class="info-value">${data.features_used ? data.features_used.length : 13} parameters</span>
                    </div>
                `;
            } else {
                // Fallback model info
                document.getElementById('modelInfo').innerHTML = `
                    <div class="info-item">
                        <span class="info-label">Model Type:</span>
                        <span class="info-value">Neural Network Classifier</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Version:</span>
                        <span class="info-value">v7</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Type:</span>
                        <span class="info-value">Binary Classification</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Features:</span>
                        <span class="info-value">13 parameters</span>
                    </div>
                `;
            }
        } catch (error) {
            document.getElementById('modelInfo').innerHTML = '<p class="text-danger">Failed to load model information</p>';
            console.error('Failed to load model info:', error);
        }
    }

    async handlePrediction() {
        if (this.isLoading) return;

        const formData = this.getFormData();
        if (!this.validateFormData(formData)) {
            return;
        }

        this.showLoading(true);
        
        try {
            const response = await fetch(`${this.apiBaseUrl}/predict`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            this.displayResults(result);
            
        } catch (error) {
            console.error('Prediction failed:', error);
            this.showError('Failed to get prediction. Please check if the API is running.');
        } finally {
            this.showLoading(false);
        }
    }

    getFormData() {
        const form = document.getElementById('predictionForm');
        const formData = new FormData(form);
        
        return {
            latitude: parseFloat(formData.get('latitude')),
            longitude: parseFloat(formData.get('longitude')),
            elevation: parseFloat(formData.get('elevation')),
            rainfall: parseFloat(formData.get('rainfall')),
            temperature: parseFloat(formData.get('temperature')),
            humidity: parseFloat(formData.get('humidity')),
            river_discharge: parseFloat(formData.get('river_discharge')),
            water_level: parseFloat(formData.get('water_level')),
            land_cover: formData.get('land_cover'),
            soil_type: formData.get('soil_type'),
            population_density: parseFloat(formData.get('population_density')),
            infrastructure: parseInt(formData.get('infrastructure')),
            historical_floods: parseInt(formData.get('historical_floods'))
        };
    }

    validateFormData(data) {
        const requiredFields = [
            'latitude', 'longitude', 'elevation', 'rainfall', 'temperature',
            'humidity', 'river_discharge', 'water_level', 'land_cover',
            'soil_type', 'population_density', 'infrastructure', 'historical_floods'
        ];

        for (const field of requiredFields) {
            if (data[field] === '' || data[field] === null || data[field] === undefined) {
                this.showError(`Please fill in all required fields. Missing: ${field}`);
                return false;
            }
        }

        // Validate ranges
        if (data.latitude < -90 || data.latitude > 90) {
            this.showError('Latitude must be between -90 and 90');
            return false;
        }
        if (data.longitude < -180 || data.longitude > 180) {
            this.showError('Longitude must be between -180 and 180');
            return false;
        }
        if (data.elevation < 0 || data.elevation > 10000) {
            this.showError('Elevation must be between 0 and 10,000 meters');
            return false;
        }
        if (data.rainfall < 0 || data.rainfall > 1000) {
            this.showError('Rainfall must be between 0 and 1,000 mm');
            return false;
        }
        if (data.temperature < -50 || data.temperature > 60) {
            this.showError('Temperature must be between -50 and 60°C');
            return false;
        }
        if (data.humidity < 0 || data.humidity > 100) {
            this.showError('Humidity must be between 0 and 100%');
            return false;
        }
        if (data.river_discharge < 0 || data.river_discharge > 10000) {
            this.showError('River discharge must be between 0 and 10,000 m³/s');
            return false;
        }
        if (data.water_level < 0 || data.water_level > 50) {
            this.showError('Water level must be between 0 and 50 meters');
            return false;
        }
        if (data.population_density < 0 || data.population_density > 50000) {
            this.showError('Population density must be between 0 and 50,000');
            return false;
        }

        return true;
    }

    displayResults(result) {
        const resultsSection = document.getElementById('resultsSection');
        const predictionCard = document.getElementById('predictionCard');
        
        const isFlood = result.prediction === 1;
        const probability = result.probability;
        const confidence = result.confidence;
        
        // Calculate probability percentage and color
        const probabilityPercent = Math.round(probability * 100);
        const probabilityColor = probability > 0.7 ? '#e74c3c' : probability > 0.4 ? '#f39c12' : '#27ae60';
        
        predictionCard.innerHTML = `
            <div class="prediction-result ${isFlood ? 'flood' : 'no-flood'}">
                <i class="fas ${isFlood ? 'fa-exclamation-triangle' : 'fa-check-circle'}"></i>
                ${isFlood ? 'FLOOD RISK DETECTED' : 'NO FLOOD RISK'}
            </div>
            
            <div class="probability-section">
                <h3>Risk Probability: ${probabilityPercent}%</h3>
                <div class="probability-bar">
                    <div class="probability-fill" style="width: ${probabilityPercent}%; background: ${probabilityColor};"></div>
                </div>
            </div>
            
            <div class="confidence-section">
                <span class="confidence-badge ${confidence.toLowerCase()}">
                    ${confidence} Confidence
                </span>
            </div>
            
            <div class="prediction-details">
                <p><strong>Model Used:</strong> ${result.model_used || 'Neural Network Classifier v7'}</p>
                <p><strong>Processing Time:</strong> ${result.processing_time ? result.processing_time.toFixed(3) : 'N/A'} seconds</p>
                <p><strong>Timestamp:</strong> ${new Date().toLocaleString()}</p>
            </div>
        `;
        
        resultsSection.style.display = 'block';
        resultsSection.classList.add('fade-in');
        
        // Scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    fillSampleData() {
        const sampleData = {
            latitude: 28.6139,
            longitude: 77.2090,
            elevation: 216.0,
            rainfall: 150.5,
            temperature: 25.3,
            humidity: 65.0,
            river_discharge: 2500.0,
            water_level: 5.2,
            land_cover: 'Urban',
            soil_type: 'Clay',
            population_density: 5000.0,
            infrastructure: '1',
            historical_floods: '0'
        };

        Object.keys(sampleData).forEach(key => {
            const element = document.getElementById(key);
            if (element) {
                element.value = sampleData[key];
            }
        });
    }

    clearForm() {
        document.getElementById('predictionForm').reset();
        document.getElementById('resultsSection').style.display = 'none';
    }

    showLoading(show) {
        this.isLoading = show;
        const overlay = document.getElementById('loadingOverlay');
        const predictBtn = document.getElementById('predictBtn');
        
        if (show) {
            overlay.style.display = 'flex';
            predictBtn.disabled = true;
            predictBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
        } else {
            overlay.style.display = 'none';
            predictBtn.disabled = false;
            predictBtn.innerHTML = '<i class="fas fa-search"></i> Predict Flood Risk';
        }
    }

    showError(message) {
        // Create a simple error notification
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-notification';
        errorDiv.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #e74c3c;
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            z-index: 1001;
            max-width: 400px;
            animation: slideIn 0.3s ease-out;
        `;
        errorDiv.innerHTML = `
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <i class="fas fa-exclamation-circle"></i>
                <span>${message}</span>
                <button onclick="this.parentElement.parentElement.remove()" style="background: none; border: none; color: white; cursor: pointer; margin-left: auto;">
                    <i class="fas fa-times"></i>
                </button>
            </div>
        `;
        
        document.body.appendChild(errorDiv);
        
        // Auto remove after 5 seconds
        setTimeout(() => {
            if (errorDiv.parentElement) {
                errorDiv.remove();
            }
        }, 5000);
    }
}

// Add CSS for error notification animation
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
`;
document.head.appendChild(style);

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new FloodPredictionApp();
});
