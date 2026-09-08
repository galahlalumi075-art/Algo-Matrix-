"""
Alpha Matrix Pro - Bot Operation Documentation
Complete guide on how the bot operates 24/7
"""

# ==============================================================================
# ALPHA MATRIX PRO - 24/7 AUTOMATED FOREX TRADING BOT
# ==============================================================================

## OVERVIEW
The bot is a fully automated trading system that:
- Runs continuously 24/7 without manual intervention
- Executes trades automatically based on predefined strategies
- Manages risk through stop-loss and take-profit levels
- Monitors multiple forex pairs simultaneously
- Logs all activities for analysis and compliance

---

## HOW THE BOT OPERATES

### 1. INITIALIZATION PHASE
When bot.py starts:
- Connects to MetaTrader5 terminal
- Validates login credentials with broker
- Loads trading strategies configuration
- Initializes logging system
- Sets risk management parameters

### 2. CONTINUOUS TRADING LOOP (24/7)
The bot enters an infinite loop that:

#### a) Price Monitoring (Every 5 seconds)
   - Checks current bid/ask prices
   - Retrieves historical candlestick data
   - Analyzes market conditions

#### b) Signal Generation (Every 10 seconds)
   - Applies trading strategy algorithm
   - Calculates moving averages
   - Identifies BUY/SELL signals
   - Compares technical indicators

#### c) Trade Execution
   - When signal is generated, bot automatically executes trade
   - Sets appropriate stop-loss and take-profit levels
   - Manages position size based on risk percentage
   - Records trade in active trades list
   - Increments daily trade counter

#### d) Position Management
   - Monitors open trades for profit/loss
   - Closes trades when TP/SL levels hit
   - Tracks cumulative daily loss
   - Updates account statistics

#### e) Account Updates (Every 30 seconds)
   - Fetches current balance
   - Calculates equity
   - Monitors daily loss
   - Checks risk limits

### 3. TRADING STRATEGIES (SIMULTANEOUS)
Bot trades 3 forex pairs at once:
- **EURUSD**: 5-minute timeframe, 0.1-1.0 lot size
- **GBPUSD**: 5-minute timeframe, 0.1-1.0 lot size
- **USDJPY**: 5-minute timeframe, 0.1-1.0 lot size

For each pair:
- Max 3 concurrent trades
- 20 pips stop-loss
- 40 pips take-profit
- 1% risk per trade

---

## AUTOMATIC TRADE EXECUTION FLOW

```
MARKET CONDITIONS
    ↓
FETCH PRICE DATA (5-second check)
    ↓
CALCULATE MOVING AVERAGES
    ↓
GENERATE SIGNAL (BUY/SELL/NONE)
    ↓
CHECK DAILY LIMITS
    ↓
IS SIGNAL VALID?
    ├─ NO → Wait 10 seconds → Loop
    └─ YES → Calculate Stop Loss & Take Profit
        ↓
        EXECUTE TRADE
        ↓
        LOG TRADE DETAILS
        ↓
        MONITOR POSITION
        ↓
        CLOSE ON TP/SL HIT
        ↓
        UPDATE STATISTICS
```

---

## RISK MANAGEMENT RULES

### Daily Limits
- **Max Daily Trades**: 50 trades per day
- **Max Daily Loss**: $500 USD
- **Min Equity**: Account must maintain minimum balance
- **Max Concurrent Trades**: 3 per symbol

### Position Management
- Every trade has automatic stop-loss
- Every trade has automatic take-profit
- Position size never exceeds max_volume
- Risk per trade: 1% of account

### Automatic Safeguards
- Bot stops trading if daily loss exceeded
- Bot stops trading if trade limit reached
- Bot stops trading if equity falls below minimum
- All trading halts at market close (if configured)

---

## HOW TO RUN THE BOT

### Option 1: Standalone Bot Execution
```bash
python bot.py
```

This runs the bot independently:
- Connects to MT5 broker
- Starts 24/7 trading loop
- Logs all activities to trading_bot.log
- Continues until interrupted (Ctrl+C)

### Option 2: API Integration (Recommended)
```bash
python main.py
```

Start FastAPI server with bot endpoints:
- Access API at http://localhost:8000
- Control bot via REST endpoints
- Monitor bot status in real-time
- Start/stop bot remotely

### API Endpoints for Bot Control:

#### Start Bot
```
POST /bot/start
{
  "server": "your_broker_server",
  "login": 12345,
  "password": "your_password"
}
```

#### Stop Bot
```
POST /bot/stop
```

#### Get Bot Status
```
GET /bot/status
```
Returns: is_running, active_trades, daily_trades, daily_loss

#### Get Active Trades
```
GET /bot/trades
```
Returns: List of all open positions

#### Pause Bot (Stop trading, keep connection)
```
POST /bot/pause
```

#### Resume Bot (Resume trading)
```
POST /bot/resume
```

---

## CONFIGURATION PARAMETERS

Located in `BotConfig` class in bot.py:

### MT5 Connection
- `MT5_SERVER`: Broker server address
- `MT5_LOGIN`: Account login number
- `MT5_PASSWORD`: Account password

### Trading Hours
- `TRADING_ENABLED`: True/False to enable/disable
- `MARKET_OPEN`: None for 24/7 trading
- `MARKET_CLOSE`: None for 24/7 trading

### Update Intervals (seconds)
- `PRICE_CHECK_INTERVAL`: 5 (check prices every 5 sec)
- `SIGNAL_CHECK_INTERVAL`: 10 (check signals every 10 sec)
- `ACCOUNT_UPDATE_INTERVAL`: 30 (update account every 30 sec)

### Risk Parameters
- `MAX_DAILY_LOSS`: $500 (stop trading if exceeded)
- `MAX_TOTAL_TRADES_PER_DAY`: 50 trades max
- `MIN_PROFIT_TO_TRADE`: Minimum equity threshold

### Per-Strategy Settings
Each trading strategy defines:
- `symbol`: Currency pair (EURUSD, GBPUSD, USDJPY)
- `timeframe`: Candle duration (5 minutes)
- `base_volume`: Starting lot size (0.1)
- `max_volume`: Maximum lot size (1.0)
- `stop_loss_pips`: SL distance (20 pips)
- `take_profit_pips`: TP distance (40 pips)
- `risk_percentage`: Risk per trade (1%)
- `max_concurrent_trades`: Max open positions (3)

---

## LOGGING AND MONITORING

### Log Files
- **trading_bot.log**: All bot activities
  - Trade executions
  - Signal generations
  - Error messages
  - Account updates

### Console Output
- Real-time status updates
- Trade confirmations
- Error alerts
- Account information

### Log Examples
```
2026-09-08 17:30:45 - INFO - Trade executed: BUY EURUSD - Ticket: 12345
2026-09-08 17:30:50 - INFO - Account - Balance: 10000, Equity: 10050, Profit: 50
2026-09-08 17:31:00 - INFO - Position closed: EURUSD - Profit: 40
2026-09-08 17:31:05 - WARNING - Daily trade limit reached: 50
```

---

## TROUBLESHOOTING

### Bot Won't Connect
- Check MT5 server address is correct
- Verify login credentials
- Ensure account is demo or live as configured
- Check internet connection

### No Trades Executing
- Verify trading symbols are available
- Check if TRADING_ENABLED is True
- Monitor signal generation logs
- Verify account has sufficient margin

### Trades Closing Immediately
- Check stop-loss and take-profit levels
- Verify broker's spread is not too wide
- Monitor market volatility
- Check if daily loss limit was reached

### Memory or Performance Issues
- Reduce PRICE_CHECK_INTERVAL value
- Reduce number of active trading symbols
- Monitor system resources
- Check log file size (rotate if needed)

---

## CUSTOMIZATION

### Add New Trading Pair
In `BotConfig.TRADING_STRATEGIES`, add:
```python
TradingStrategy(
    symbol="AUDUSD",
    timeframe=5,
    base_volume=0.1,
    max_volume=1.0,
    stop_loss_pips=20,
    take_profit_pips=40,
    risk_percentage=1.0,
    max_concurrent_trades=3
)
```

### Modify Trading Strategy
Edit `generate_trading_signal()` method to change:
- Moving average periods
- Signal generation logic
- Entry conditions
- Exit conditions

### Change Risk Parameters
Modify values in `BotConfig`:
```python
MAX_DAILY_LOSS = 1000  # Change daily loss limit
MAX_TOTAL_TRADES_PER_DAY = 100  # More trades allowed
```

---

## DEPLOYMENT FOR BASE64 ENCODING

To provide configuration as base64:

```python
import base64
import json

config_dict = {
    "server": "your_broker_server",
    "login": 12345,
    "password": "your_password",
    "trading_enabled": True
}

# Encode to base64
encoded = base64.b64encode(json.dumps(config_dict).encode()).decode()
print(encoded)

# Decode when needed
decoded = json.loads(base64.b64decode(encoded).decode())
```

---

## SAFETY FEATURES

✅ Automatic stop-loss on every trade
✅ Daily loss limit enforcement
✅ Daily trade count limit
✅ Minimum equity requirement
✅ Concurrent trade limits per symbol
✅ Comprehensive error handling
✅ Real-time logging
✅ Graceful shutdown capability
✅ Position monitoring
✅ Account statistics tracking

---

## PERFORMANCE METRICS

Expected Performance:
- Win Rate: 45-55% (depends on market conditions)
- Average Win: 40 pips
- Average Loss: 20 pips
- Profit Factor: 1.5+
- Max Daily Trades: 50
- Risk per Trade: 1%

---

## SUPPORT

For issues or questions about bot operation:
1. Check trading_bot.log for errors
2. Verify all configuration parameters
3. Test connectivity with `/connect` endpoint
4. Monitor bot status with `/bot/status`
5. Check broker account status

---

END OF DOCUMENTATION
