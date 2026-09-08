# Weather Dashboard

A comprehensive weather dashboard that fetches real-time data from the OpenWeatherMap API.

## ✨ Features

### 🔍 Search & Discovery
- **City Search** - Search for any city worldwide
- **Auto-complete Suggestions** - Get city suggestions as you type
- **Geolocation** - Click the location button to use your current position
- **Multi-language Support** - Works with any city name

### 🌡️ Current Weather Display
- **Large Temperature Display** - Easy-to-read temperature in Celsius
- **Weather Condition Icons** - Visual representation of weather
- **Feels-like Temperature** - Perceived temperature
- **Comprehensive Metrics**:
  - Humidity percentage
  - Atmospheric pressure
  - Wind speed and direction
  - Cloud coverage
  - Visibility distance

### 📅 Forecasts
- **5-Day Forecast** - Daily weather predictions
- **Hourly Forecast** - 24-hour breakdown with hourly updates
- **Interactive Cards** - Click for more details
- **Weather Icons** - Visual indicators for each time period

### 💨 Air Quality Information
- **AQI (Air Quality Index)** - Overall air quality (Good to Very Poor)
- **Pollutant Levels**:
  - PM2.5 (Fine particulate matter)
  - PM10 (Coarse particulate matter)
  - NO₂ (Nitrogen dioxide)
  - O₃ (Ozone)

### ☀️ UV Index
- **UV Radiation Level** - Real-time UV index
- **Risk Assessment** - Low, Moderate, High, Very High, or Extreme
- **Color-coded Display** - Visual risk indicator

## 🚀 Getting Started

### Step 1: Get Your API Key
1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Go to API Keys page and copy your key

### Step 2: Configure Your API Key
Open `weather/script.js` and replace:
```javascript
const API_KEY = 'YOUR_API_KEY_HERE';
```

With your actual API key:
```javascript
const API_KEY = 'abc123def456ghi789jkl012';
```

### Step 3: Open the Dashboard
Simply open `weather/index.html` in your web browser!

## 📊 API Endpoints Used

The dashboard makes API calls to:
1. **Geocoding API** - Convert city names to coordinates
2. **Current Weather API** - Real-time weather conditions
3. **Forecast API** - 5-day and hourly forecasts
4. **Air Pollution API** - Air quality data
5. **UV Index API** - Ultraviolet radiation levels

## 🎨 User Interface

### Desktop
- Full multi-column layout
- All information visible at once
- Large weather display
- Grid-based metrics

### Tablet
- Responsive grid that adapts to screen size
- Optimized spacing and font sizes
- Touch-friendly buttons

### Mobile
- Single-column layout
- Scrollable sections
- Full-width cards
- Large tap targets

## ⚙️ Technical Details

- **Framework**: Vanilla JavaScript (No dependencies)
- **API Service**: OpenWeatherMap
- **Architecture**: Event-driven
- **Data Format**: JSON
- **Updates**: Real-time
- **Caching**: Browser cache for static assets

## 🔒 Security Notes

- API key is only used on the client-side
- No server-side storage of sensitive data
- HTTPS recommended for production use
- Don't commit API keys to version control

## 🛠️ Customization

### Change Temperature Units
In `script.js`, replace all instances of `&units=metric` with `&units=imperial`

### Modify Color Scheme
Edit these colors in `styles.css`:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Change Default City
In `script.js`, modify the last line:
```javascript
fetchWeatherByCityName('Paris');
```

## 📱 Responsive Breakpoints

- **Desktop**: 1024px and above
- **Tablet**: 768px to 1023px
- **Mobile**: Below 768px

## 🔄 Data Update Frequency

- **Current Weather**: Updates every 10 minutes
- **Forecasts**: Updates every 3 hours
- **Air Quality**: Updates hourly
- **UV Index**: Updates periodically

## 🎯 Popular Cities to Try

- London, UK
- Tokyo, Japan
- New York, USA
- Sydney, Australia
- Dubai, UAE
- Paris, France
- Moscow, Russia
- Singapore
- Toronto, Canada
- Amsterdam, Netherlands

## 📚 Resources

- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [Weather Conditions Reference](https://openweathermap.org/weather-conditions)
- [API Keys Management](https://openweathermap.org/api/keys)

## 🐛 Troubleshooting

### "API key is invalid"
- Check your API key is correct
- Ensure no extra spaces
- Generate a new key if needed

### "City not found"
- Try alternative city names
- Use English city names
- Include country code (e.g., "London, UK")

### Geolocation not working
- Check browser permissions
- Allow location access when prompted
- Try a different browser

### No data displayed
- Check browser console for errors
- Verify API key is set
- Check internet connection

## 📄 License

MIT License - Free to use and modify

---

Enjoy using the Weather Dashboard! 🌍
