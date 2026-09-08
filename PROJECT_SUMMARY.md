# Project Summary - Algo-Matrix-

Complete overview of all applications and systems in this repository.

---

## 📋 Table of Contents

1. [Forex Trading Bot (24/7)](#forex-trading-bot-247)
2. [Weather Dashboard](#weather-dashboard)
3. [Digital Clock](#digital-clock)
4. [To-Do List Application](#to-do-list-application)

---

## 🤖 Forex Trading Bot (24/7)

### Purpose
Automated forex trading bot that executes trades 24/7 without manual intervention.

### Key Files
- **bot.py** - Core bot logic, trading strategies, and execution engine
- **main.py** - FastAPI server with bot control endpoints
- **BOT_OPERATION.md** - Comprehensive operation documentation
- **requirements.txt** - Python dependencies

### Features
✅ Continuous 24/7 trading operation
✅ Automatic trade execution based on signals
✅ Risk management with stop-loss and take-profit
✅ Multiple forex pair trading (EURUSD, GBPUSD, USDJPY)
✅ Daily loss and trade limit enforcement
✅ Real-time logging and monitoring
✅ REST API for bot control
��� Account statistics tracking

### How It Operates

**Initialization:**
- Connects to MetaTrader5 terminal
- Validates broker credentials
- Loads trading strategies
- Initializes risk management parameters

**Continuous Trading Loop:**
1. Check prices every 5 seconds
2. Generate trading signals every 10 seconds
3. Execute trades when signals appear
4. Monitor open positions
5. Update account stats every 30 seconds
6. Apply risk management rules
7. Close trades on TP/SL levels

**Risk Management:**
- Max daily loss: $500
- Max daily trades: 50
- Max concurrent trades per pair: 3
- Stop-loss: 20 pips per trade
- Take-profit: 40 pips per trade
- Risk per trade: 1% of account

### API Endpoints

```
POST /connect
- Login to broker account

POST /trade
- Execute manual trade

POST /bot/start
- Start 24/7 trading bot

POST /bot/stop
- Stop bot trading

GET /bot/status
- Get current bot status

GET /bot/trades
- Get active trades list

POST /bot/pause
- Pause trading (keep connection)

POST /bot/resume
- Resume trading
```

### Configuration
Edit `BotConfig` in bot.py:
- Trading symbols
- Timeframes
- Lot sizes
- Stop-loss/Take-profit levels
- Daily limits
- Update intervals

### Running the Bot

**Option 1: Standalone**
```bash
python bot.py
```

**Option 2: With API**
```bash
python main.py
```
Then access at http://localhost:8000

---

## 🌤️ Weather Dashboard

### Purpose
Real-time weather information with air quality and UV index tracking.

### Key Files
- **weather/index.html** - HTML template
- **weather/styles.css** - Styling and animations
- **weather/script.js** - API integration and functionality
- **weather/README.md** - Detailed documentation
- **weather/SETUP.md** - Setup guide

### Features
✨ Real-time weather data
🔍 City search with auto-complete
📍 Geolocation support
🌡️ Current weather display
📅 5-day forecast
⏰ 24-hour hourly forecast
💨 Air quality index (AQI)
☀️ UV radiation levels
📱 Fully responsive design
🎨 Beautiful gradient UI

### Weather Information Displayed

**Current Weather:**
- Temperature (Celsius)
- Weather condition
- Feels-like temperature
- Humidity
- Pressure
- Wind speed & direction
- Cloud coverage
- Visibility

**Forecasts:**
- 5-day daily forecast
- 24-hour hourly breakdown
- Weather icons for each period
- Temperature predictions

**Air Quality:**
- AQI (Good to Very Poor)
- PM2.5 levels
- PM10 levels
- NO₂ levels
- O₃ levels

**UV Index:**
- Current UV radiation
- Risk assessment
- Color-coded display

### Setup

1. Get free API key from https://openweathermap.org
2. Open weather/script.js
3. Replace `'YOUR_API_KEY_HERE'` with your key
4. Open weather/index.html in browser

### How to Use

1. Search for any city
2. Click geolocation button to use current location
3. View comprehensive weather information
4. Check forecasts and air quality
5. Monitor UV index

---

## 🕐 Digital Clock

### Purpose
Display current time across 8 different time zones globally.

### Key Files
- **clock/index.html** - HTML template with 8 time zones
- **clock/styles.css** - Styling with glowing effects
- **clock/script.js** - Real-time clock updates
- **clock/README.md** - Documentation

### Features
✨ Real-time updates every second
🌍 8 global time zones:
  - New York (EST/EDT)
  - London (GMT/BST)
  - Tokyo (JST)
  - Sydney (AEDT/AEST)
  - Dubai (GST)
  - São Paulo (BRT/BRST)
  - Moscow (MSK)
  - Singapore (SGT)
📱 Fully responsive design
🎨 Cyber theme with animations
⚡ No dependencies required
🔄 Auto-updates on tab visibility

### Time Zones Included

| City | Timezone | UTC Offset |
|------|----------|-----------|
| New York | EST/EDT | UTC-5/-4 |
| London | GMT/BST | UTC+0/+1 |
| Tokyo | JST | UTC+9 |
| Sydney | AEDT/AEST | UTC+10/+11 |
| Dubai | GST | UTC+4 |
| São Paulo | BRT/BRST | UTC-3/-2 |
| Moscow | MSK | UTC+3 |
| Singapore | SGT | UTC+8 |

### How to Use

1. Open clock/index.html in browser
2. Clocks start updating automatically
3. Times update every second
4. View local time at bottom
5. All times displayed in HH:MM:SS format

### Customization

Add new time zone:
1. Add to timeZones object in script.js
2. Add HTML clock-card in index.html
3. Update README with new timezone

---

## ✓ To-Do List Application

### Purpose
Task management with local storage persistence.

### Key Files
- **todo/index.html** - HTML template
- **todo/styles.css** - Styling and responsive layout
- **todo/script.js** - Task management and storage
- **todo/README.md** - Detailed documentation

### Features
✅ Add tasks instantly
✅ Mark tasks complete
✅ Delete individual tasks
✅ Filter by status (All/Active/Completed)
✅ Real-time statistics
✅ Clear all completed tasks
✅ Export tasks as JSON
✅ Local storage persistence
✅ Responsive design
✅ Auto-save functionality

### Statistics Dashboard
- **Total Tasks** - All tasks count
- **Completed** - Finished tasks count
- **Remaining** - Active tasks count

### How to Use

1. Open todo/index.html in browser
2. Type task in input field
3. Click "Add Task" or press Enter
4. Check checkbox to complete
5. Click "Delete" to remove
6. Use filter buttons to view tasks
7. Click "Clear Completed" to remove finished tasks
8. Click "Export" to download as JSON

### Local Storage Details

**Storage Key:** `todoList`

**Data Structure:**
```json
{
  "id": "_unique_id",
  "text": "Task description",
  "completed": false,
  "createdAt": "Date string"
}
```

**Capacity:** 5-10MB in most browsers (hundreds to thousands of tasks)

### Features

**Filtering:**
- All Tasks - Show everything
- Active - Show incomplete
- Completed - Show finished

**Timestamps:**
- Each task shows creation date/time
- Automatic capture
- Preserved in storage

**Export:**
- Download as JSON file
- Filename: todos_YYYY-MM-DD.json
- Import into other tools

**Data Persistence:**
- Automatic saving on every change
- Persists across sessions
- Browser-specific storage
- Cleared if browser data deleted

---

## 📊 Project Structure

```
Algo-Matrix-/
├── main.py                 # FastAPI server with bot endpoints
├── bot.py                  # 24/7 trading bot core logic
├── config.py               # Configuration management
├── requirements.txt        # Python dependencies
├── BOT_OPERATION.md        # Bot documentation
├── PROJECT_SUMMARY.md      # This file
│
├── weather/                # Weather Dashboard
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   ├── README.md
│   └── SETUP.md
│
├── clock/                  # Digital Clock
│   ├── index.html
│   ├── styles.css
│   ├── script.js
│   └── README.md
│
└── todo/                   # To-Do List
    ├── index.html
    ├── styles.css
    ├── script.js
    └── README.md
```

---

## 🚀 Quick Start Guide

### Forex Trading Bot
```bash
# Install dependencies
pip install -r requirements.txt

# Run bot standalone
python bot.py

# Or run with API
python main.py
# Visit: http://localhost:8000
```

### Weather Dashboard
1. Get API key from openweathermap.org
2. Update weather/script.js with API key
3. Open weather/index.html in browser

### Digital Clock
1. Open clock/index.html in browser
2. Clock starts automatically

### To-Do List
1. Open todo/index.html in browser
2. Start adding tasks

---

## 📱 Responsive Design

All applications are fully responsive:
- ✅ Desktop (1024px+)
- ✅ Tablet (768px - 1023px)
- ✅ Mobile (< 768px)

---

## 🔐 Security Notes

### Forex Bot
- Store credentials in environment variables
- Use demo account for testing
- Never hardcode passwords
- Validate all inputs

### Weather Dashboard
- API key visible in client code (acceptable for free tier)
- Use API key restrictions if available
- Monitor API usage

### To-Do List
- Data stored locally in browser
- No server transmission
- Private to each browser

---

## 🛠️ Technology Stack

### Backend
- Python 3.8+
- FastAPI
- MetaTrader5 API
- Asyncio

### Frontend
- HTML5
- CSS3
- Vanilla JavaScript
- No frameworks or dependencies

### APIs
- OpenWeatherMap (Weather)
- MetaTrader5 (Forex Trading)
- Browser Local Storage (To-Do)

---

## 📈 Features Summary

| Feature | Bot | Weather | Clock | Todo |
|---------|-----|---------|-------|------|
| 24/7 Operation | ✅ | ✅ | ✅ | ✅ |
| Real-time Updates | ✅ | ✅ | ✅ | ✅ |
| Local Storage | ❌ | ❌ | ❌ | ✅ |
| REST API | ✅ | ❌ | ❌ | ❌ |
| Responsive | ✅ | ✅ | ✅ | ✅ |
| Mobile Friendly | ✅ | ✅ | ✅ | ✅ |
| Logging | ✅ | ❌ | ❌ | ❌ |
| Export Data | ❌ | ❌ | ❌ | ✅ |

---

## 📝 Notes

- All applications use vanilla code (no heavy frameworks)
- Optimized for performance
- Full documentation included
- Easy to customize and extend
- Production-ready code

---

## 🎯 Next Steps

1. **Forex Bot**: Set up MetaTrader5 account, configure credentials
2. **Weather**: Get OpenWeatherMap API key, update configuration
3. **Clock**: Just open HTML file, no setup needed
4. **To-Do**: Open HTML file, start adding tasks

---

**Project Complete!** ✅

All applications are fully functional and ready to use.

---

*Last Updated: September 8, 2026*
