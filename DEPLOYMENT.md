"""
Algo-Matrix- Deployment & Configuration Guide
Complete setup for production deployment
"""

# ==============================================================================
# DEPLOYMENT & CONFIGURATION GUIDE
# ==============================================================================

## SYSTEM REQUIREMENTS

### Minimum Requirements
- OS: Windows, macOS, or Linux
- Python: 3.8 or higher
- RAM: 2GB minimum (4GB recommended)
- Disk Space: 500MB minimum
- Internet: Stable connection required

### Recommended Setup
- OS: Linux (Ubuntu 20.04+)
- Python: 3.10 or higher
- RAM: 8GB or more
- Disk Space: 2GB
- Internet: 100Mbps+

---

## INSTALLATION STEPS

### 1. Prerequisites Installation

#### Windows
```batch
# Install Python from https://www.python.org/downloads/
# Install MetaTrader5 from https://www.metatrader5.com/download

# Verify installations
python --version
pip --version
```

#### macOS
```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python

# Verify
python3 --version
pip3 --version
```

#### Linux (Ubuntu/Debian)
```bash
# Update package manager
sudo apt update
sudo apt upgrade

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Verify
python3 --version
pip3 --version
```

### 2. Repository Setup

```bash
# Clone or navigate to repository
cd Algo-Matrix-

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

#### Bot Configuration
Edit `bot.py`:

```python
class BotConfig:
    # Broker credentials
    MT5_SERVER = "your_broker_server"
    MT5_LOGIN = your_login_number
    MT5_PASSWORD = "your_password"
    
    # Trading settings
    TRADING_ENABLED = True
    MARKET_OPEN = None  # None for 24/7
    MARKET_CLOSE = None
    
    # Risk limits
    MAX_DAILY_LOSS = 500
    MAX_TOTAL_TRADES_PER_DAY = 50
    MIN_PROFIT_TO_TRADE = -1000
```

#### Weather Configuration
Edit `weather/script.js`:

```javascript
const API_KEY = 'your_openweathermap_api_key';
```

#### Environment Variables (Optional but Recommended)

Create `.env` file:
```
MT5_SERVER=your_broker_server
MT5_LOGIN=12345
MT5_PASSWORD=your_password
API_KEY=your_openweathermap_key
```

Then in `bot.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()
MT5_SERVER = os.getenv('MT5_SERVER')
MT5_LOGIN = int(os.getenv('MT5_LOGIN'))
MT5_PASSWORD = os.getenv('MT5_PASSWORD')
```

---

## RUNNING THE APPLICATIONS

### Option 1: Standalone Bot
```bash
python bot.py
```

**Output:**
```
2026-09-08 18:10:45 - INFO - Initializing MT5 connection...
2026-09-08 18:10:50 - INFO - MT5 Connected - Account: 12345, Balance: 10000
2026-09-08 18:10:55 - INFO - Starting 24/7 trading loop...
2026-09-08 18:11:00 - INFO - Trade executed: BUY EURUSD - Ticket: 123456
```

### Option 2: API Server (Recommended)
```bash
python main.py
```

**Output:**
```
INFO:     Started server process [1234]
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

Access API:
- API Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/

### Web Applications
```bash
# Simply open in browser
# No server required - they run on frontend

# Clock
clock/index.html

# To-Do List
todo/index.html

# Weather (after API key setup)
weather/index.html
```

---

## PRODUCTION DEPLOYMENT

### Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]
```

Build and run:
```bash
# Build image
docker build -t algo-matrix .

# Run container
docker run -p 8000:8000 -e MT5_SERVER=your_server \
  -e MT5_LOGIN=12345 \
  -e MT5_PASSWORD=your_pass \
  algo-matrix
```

### Systemd Service (Linux)

Create `/etc/systemd/system/algo-matrix.service`:
```ini
[Unit]
Description=Algo Matrix Trading Bot
After=network.target

[Service]
Type=simple
User=trading
WorkingDirectory=/home/trading/Algo-Matrix-
ExecStart=/home/trading/Algo-Matrix-/venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable algo-matrix
sudo systemctl start algo-matrix
sudo systemctl status algo-matrix
```

### Cloud Deployment

#### Heroku
```bash
# Create Heroku app
heroku create algo-matrix

# Set environment variables
heroku config:set MT5_SERVER=your_server
heroku config:set MT5_LOGIN=12345
heroku config:set MT5_PASSWORD=your_pass

# Deploy
git push heroku main

# View logs
heroku logs --tail
```

#### AWS EC2
```bash
# Launch EC2 instance (Ubuntu 20.04)
# SSH into instance

# Install dependencies
sudo apt update
sudo apt install python3 python3-pip git

# Clone repository
git clone https://github.com/your-repo/Algo-Matrix-.git
cd Algo-Matrix-

# Setup
pip3 install -r requirements.txt

# Create systemd service (see above)

# Access via security group port 8000
```

#### DigitalOcean
```bash
# Create Droplet (Ubuntu 20.04)
# SSH into droplet

# Install dependencies
sudo apt update
sudo apt install python3 python3-pip git

# Clone and setup
git clone https://github.com/your-repo/Algo-Matrix-.git
cd Algo-Matrix-
pip3 install -r requirements.txt

# Run with nohup
nohup python3 main.py > bot.log 2>&1 &
```

---

## SECURITY CONFIGURATION

### Firewall Setup

#### Linux (ufw)
```bash
# Allow SSH
sudo ufw allow 22/tcp

# Allow API port
sudo ufw allow 8000/tcp

# Enable firewall
sudo ufw enable
```

#### Windows Firewall
```powershell
# Open PowerShell as Admin
New-NetFirewallRule -DisplayName "Algo-Matrix API" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 8000
```

### API Security

#### Add CORS Protection
Edit `main.py`:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### API Key Authentication
Add to `main.py`:
```python
from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

async def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != os.getenv("API_KEY"):
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key
```

### Credential Management

**NEVER:**
- ❌ Hardcode credentials in code
- ❌ Commit `.env` files to git
- ❌ Expose API keys in client code
- ❌ Share credentials via email/messages

**DO:**
- ✅ Use environment variables
- ✅ Add `.env` to `.gitignore`
- ✅ Use secure vaults (AWS Secrets Manager, HashiCorp Vault)
- ✅ Rotate credentials regularly
- ✅ Use restricted API keys

---

## MONITORING & LOGGING

### Log Configuration

Edit `bot.py` logging setup:
```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/trading_bot.log'),
        logging.RotatingFileHandler(
            'logs/trading_bot_rotation.log',
            maxBytes=10485760,  # 10MB
            backupCount=5
        ),
        logging.StreamHandler()
    ]
)
```

### Log Rotation

Create `logrotate` config for Linux:
```bash
# /etc/logrotate.d/algo-matrix
/home/trading/Algo-Matrix-/logs/*.log {
    daily
    rotate 14
    compress
    delaycompress
    notifempty
    create 0640 trading trading
    sharedscripts
    postrotate
        systemctl restart algo-matrix > /dev/null 2>&1 || true
    endscript
}
```

### Monitoring Tools

#### Basic Health Check
```bash
# Create health_check.py
import requests

response = requests.get('http://localhost:8000/bot/status')
if response.status_code == 200:
    print("✓ Bot is running")
else:
    print("✗ Bot is down")
```

#### Uptime Monitoring
```bash
# Use tools like:
# - Systemd (built-in monitoring)
# - Supervisor (process manager)
# - PM2 (Node.js alternative)
# - Monit (system monitoring)
```

---

## PERFORMANCE TUNING

### Memory Optimization
```python
# In bot.py
import psutil
import gc

# Monitor memory
def check_memory():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > 80:
        gc.collect()  # Force garbage collection
```

### Database Connection Pooling
For future database integration:
```python
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

engine = create_engine(
    'postgresql://user:pass@localhost/db',
    poolclass=NullPool,  # Disable pooling for 24/7 operation
    echo=False
)
```

### Concurrency Settings
```python
# In bot.py
PRICE_CHECK_INTERVAL = 5  # seconds
SIGNAL_CHECK_INTERVAL = 10  # seconds
ACCOUNT_UPDATE_INTERVAL = 30  # seconds

# Adjust based on system resources
# Lower = More frequent updates = More resources
```

---

## BACKUP & RECOVERY

### Database Backup (Future)
```bash
# Daily backup
0 2 * * * /home/trading/backup.sh

# backup.sh
#!/bin/bash
BACKUP_DIR="/backups/algo-matrix"
DATE=$(date +%Y%m%d_%H%M%S)

# Backup trade history
pg_dump algo_matrix > $BACKUP_DIR/db_$DATE.sql

# Backup logs
tar -czf $BACKUP_DIR/logs_$DATE.tar.gz /home/trading/Algo-Matrix-/logs/

# Keep only 30 days of backups
find $BACKUP_DIR -type f -mtime +30 -delete
```

### Configuration Backup
```bash
# Backup configurations
cp bot.py backups/bot_$(date +%Y%m%d).py
cp main.py backups/main_$(date +%Y%m%d).py
cp .env backups/.env_$(date +%Y%m%d).backup
```

---

## TROUBLESHOOTING

### Bot Won't Start
```bash
# 1. Check Python version
python --version  # Must be 3.8+

# 2. Check dependencies
pip list | grep -E "fastapi|metatrader5"

# 3. Verify credentials
# Check bot.py MT5_SERVER, LOGIN, PASSWORD

# 4. Check MT5 installation
# Verify MetaTrader5 is installed and running

# 5. Check logs
tail -f logs/trading_bot.log
```

### API Connection Issues
```bash
# Test connection
curl -v http://localhost:8000/

# Check firewall
sudo ufw status
netstat -an | grep 8000

# Check process
ps aux | grep main.py
```

### Memory Leak
```bash
# Monitor memory usage
watch -n 1 'ps aux | grep main.py | grep -v grep'

# Check for file handles
lsof -p $(pgrep -f main.py) | wc -l

# Restart if needed
sudo systemctl restart algo-matrix
```

---

## MAINTENANCE

### Regular Tasks

**Daily:**
- Check bot logs for errors
- Monitor account balance
- Verify active trades

**Weekly:**
- Backup configuration
- Review trading statistics
- Check system health

**Monthly:**
- Update dependencies: `pip install --upgrade -r requirements.txt`
- Review bot performance
- Analyze profit/loss
- Update documentation

**Quarterly:**
- Security audit
- Performance optimization
- Code review
- Backup rotation

### Dependency Updates
```bash
# Check for updates
pip list --outdated

# Update specific package
pip install --upgrade fastapi

# Update all
pip install --upgrade -r requirements.txt

# Test after updates
python main.py
```

---

## COMPLIANCE & RISK MANAGEMENT

### Trading Compliance
- 📝 Keep trading logs (required by regulations)
- 📊 Report P&L regularly
- 🔍 Monitor for unusual activity
- ⚠️ Set daily loss limits
- 💰 Maintain capital requirements

### System Reliability
- 🔄 Automated backups
- 📋 Monitoring alerts
- 🛡️ Firewall protection
- 🔐 Credential management
- 📊 Performance tracking

### Data Protection
- 🔒 Encrypt sensitive data
- 🚀 Regular backups
- 👤 Access controls
- 🛡️ Intrusion detection
- 📝 Audit logging

---

## SUPPORT & DOCUMENTATION

### Log Files
- `logs/trading_bot.log` - Main bot log
- `logs/trading_bot_rotation.log` - Rotated logs

### API Documentation
- Access at `http://localhost:8000/docs`
- Interactive Swagger UI
- Try endpoints directly

### Reference Guides
- [BOT_OPERATION.md](BOT_OPERATION.md) - Bot operations
- [README.md](README.md) - Main documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide

---

## EMERGENCY PROCEDURES

### Emergency Stop
```bash
# Stop bot immediately
sudo systemctl stop algo-matrix

# Or kill process
kill -9 $(pgrep -f main.py)

# Verify stopped
ps aux | grep main.py
```

### Account Recovery
```python
# Check account status
import MetaTrader5 as mt5
mt5.initialize()
print(mt5.account_info())

# Close all open positions
positions = mt5.positions_get()
for position in positions:
    # Close logic here
    pass
```

### Data Recovery
```bash
# Restore from backup
cp backups/bot_20260908.py bot.py
cp backups/.env_20260908.backup .env
```

---

## TESTING

### Unit Tests
```bash
# Create tests/test_bot.py
# Run tests
pytest tests/

# With coverage
pytest --cov=bot tests/
```

### Integration Tests
```bash
# Test API endpoints
# Test bot trading logic
# Test risk management
```

### Load Testing
```bash
# Test under high frequency trading
# Monitor resource usage
# Check for memory leaks
```

---

**Deployment Complete!** ✅

Your Algo-Matrix- system is ready for production operation.

---

*Deployment Guide - Last Updated: September 8, 2026*
