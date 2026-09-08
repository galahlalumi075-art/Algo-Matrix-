# Quick Start Guide - Algo-Matrix-

Get all applications running in minutes!

---

## 🤖 FOREX TRADING BOT (24/7)

### Prerequisites
- Python 3.8+
- MetaTrader5 installation
- Broker account (Demo or Live)

### Setup (2 minutes)

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Credentials**
   Edit `bot.py` - Update `BotConfig`:
   ```python
   MT5_SERVER = "your_broker_server"
   MT5_LOGIN = 12345
   MT5_PASSWORD = "your_password"
   ```

3. **Run Bot**
   ```bash
   python bot.py
   ```

### Via API (Recommended)
   ```bash
   python main.py
   ```
   Then access: http://localhost:8000

### API Quick Test
   ```bash
   # Start bot
   curl -X POST http://localhost:8000/bot/start \
     -H "Content-Type: application/json" \
     -d '{"server":"your_server","login":12345,"password":"pass"}'
   
   # Check status
   curl http://localhost:8000/bot/status
   
   # Stop bot
   curl -X POST http://localhost:8000/bot/stop
   ```

---

## 🌤️ WEATHER DASHBOARD (30 seconds)

### Setup

1. **Get API Key**
   - Visit: https://openweathermap.org/api
   - Sign up (free)
   - Copy your API key

2. **Add API Key**
   - Open: `weather/script.js`
   - Find: `const API_KEY = 'YOUR_API_KEY_HERE';`
   - Replace with your key

3. **Open in Browser**
   - Double-click: `weather/index.html`
   - Done! ✅

### Features to Try
- Search for cities
- Click location button (📍)
- Check 5-day forecast
- View air quality
- Monitor UV index

---

## 🕐 DIGITAL CLOCK (Instant)

### Setup
1. Double-click: `clock/index.html`
2. See 8 time zones updating in real-time
3. Done! ✅

### Time Zones
- New York
- London
- Tokyo
- Sydney
- Dubai
- São Paulo
- Moscow
- Singapore

---

## ✓ TO-DO LIST (Instant)

### Setup
1. Double-click: `todo/index.html`
2. Start adding tasks
3. Tasks auto-save to browser storage
4. Done! ✅

### Quick Features
- Add/delete tasks
- Mark complete
- Filter (All/Active/Completed)
- Export tasks as JSON
- Clear completed

---

## 📂 File Locations

```
Algo-Matrix-/
├── main.py              ← Start API server here
├── bot.py               ← Start bot here
├── requirements.txt     ← Install dependencies
├── BOT_OPERATION.md     ← Bot documentation
├── PROJECT_SUMMARY.md   ← Full project info
│
├── weather/index.html   ← Open in browser
├── clock/index.html     ← Open in browser
└── todo/index.html      ← Open in browser
```

---

## ⚡ Quick Commands

### Python Applications
```bash
# Install all dependencies
pip install -r requirements.txt

# Run trading bot (standalone)
python bot.py

# Run with API server
python main.py

# Run specific module
python -m bot
```

### Web Applications
```bash
# Use any of these:
# - Double-click the HTML file
# - Right-click → Open with → Browser
# - Drag and drop into browser window
# - Type file path in browser address bar
```

---

## 🐛 Troubleshooting

### Bot Won't Start
- Check Python version (3.8+)
- Install dependencies: `pip install -r requirements.txt`
- Verify MetaTrader5 is installed
- Check credentials in bot.py

### Weather Shows No Data
- Verify API key is correct
- Check internet connection
- Ensure API key has correct permissions
- Try searching for a different city

### Clock Not Updating
- Refresh browser (Ctrl+R)
- Check browser console (F12)
- Try a different browser

### To-Do Not Saving
- Check if local storage is enabled
- Try incognito/private mode
- Clear browser cache
- Check available storage space

---

## 📚 Documentation Files

- **BOT_OPERATION.md** - Complete bot operation guide
- **PROJECT_SUMMARY.md** - Full project overview
- **weather/README.md** - Weather app details
- **weather/SETUP.md** - Weather app setup guide
- **clock/README.md** - Clock app details
- **todo/README.md** - To-Do app details

---

## 🔗 Useful Links

- **OpenWeatherMap API**: https://openweathermap.org/api
- **MetaTrader5 Download**: https://www.metatrader5.com
- **FastAPI Docs**: http://localhost:8000/docs (when running)

---

## ✅ Verification Checklist

### Forex Bot
- [ ] Python installed
- [ ] Dependencies installed
- [ ] Credentials configured
- [ ] MetaTrader5 running
- [ ] Bot starts without errors

### Weather Dashboard
- [ ] API key obtained
- [ ] API key added to script.js
- [ ] Browser opens HTML file
- [ ] Search works for cities

### Digital Clock
- [ ] HTML file opens in browser
- [ ] Clock displays 8 time zones
- [ ] Time updates every second

### To-Do List
- [ ] HTML file opens in browser
- [ ] Can add tasks
- [ ] Tasks save (refresh page, they remain)

---

## 🎯 Next Steps

1. **Start with easiest**: Open clock/index.html (takes 5 seconds)
2. **Then try To-Do**: Open todo/index.html (takes 10 seconds)
3. **Add Weather**: Get API key and update weather/script.js (takes 2 minutes)
4. **Advanced Bot**: Set up MetaTrader5 and run trading bot (takes 10 minutes)

---

## 💡 Tips

- Keep API key secure (don't commit to public repos)
- Export to-do tasks regularly as backup
- Monitor bot logs for trading activity
- Use demo account for bot testing
- Check weather data accuracy by searching known cities

---

## 📞 Support

For each application, check the README.md in its folder:
- `weather/README.md`
- `clock/README.md`
- `todo/README.md`

For bot operation: See `BOT_OPERATION.md`

---

**You're all set! Enjoy using Algo-Matrix-** 🚀

---

*Quick Start Guide - Last Updated: September 8, 2026*
