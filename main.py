"""
Alpha Matrix Pro - API with 24/7 Bot Integration
FastAPI endpoints with background bot execution
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import MetaTrader5 as mt5
from typing import Optional
import asyncio
from bot import TradingBot, BotConfig
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Alpha Matrix Pro Connection Engine")

# Global bot instance
trading_bot: Optional[TradingBot] = None
bot_task: Optional[asyncio.Task] = None


# Data Models
class ConnectRequest(BaseModel):
    server: str
    login: int
    password: str


class TradeRequest(BaseModel):
    symbol: str
    action: str  # "BUY" or "SELL"
    volume: float
    sl: Optional[float] = 0.0
    tp: Optional[float] = 0.0


class BotStartRequest(BaseModel):
    server: str
    login: int
    password: str


class BotStatusResponse(BaseModel):
    status: str
    is_running: bool
    active_trades: int
    daily_trades: int
    last_updated: str


@app.get("/")
def root():
    return {"status": "active", "system": "Alpha Matrix Pro API with 24/7 Bot"}


# BROKER AUTHENTICATION ENDPOINT
@app.post("/connect")
def connect_account(data: ConnectRequest):
    if not mt5.initialize():
        raise HTTPException(status_code=500, detail="Failed to initialize MT5 engine")

    authorized = mt5.login(login=data.login, password=data.password, server=data.server)

    if authorized:
        acc_info = mt5.account_info()
        return {
            "status": "connected",
            "server": data.server,
            "account": data.login,
            "balance": acc_info.balance,
            "equity": acc_info.equity,
            "currency": acc_info.currency
        }
    else:
        error_code = mt5.last_error()
        raise HTTPException(
            status_code=400, 
            detail=f"Login failed on {data.server}. Check credentials. MT5 Error: {error_code}"
        )


# AUTOMATED TRADE EXECUTION ENDPOINT
@app.post("/trade")
def place_trade(data: TradeRequest):
    if not mt5.terminal_info():
        raise HTTPException(status_code=400, detail="MT5 terminal is not connected")

    symbol_info = mt5.symbol_info(data.symbol)
    if symbol_info is None:
        raise HTTPException(status_code=400, detail=f"Symbol {data.symbol} not found")

    if not symbol_info.visible:
        if not mt5.symbol_select(data.symbol, True):
            raise HTTPException(status_code=400, detail=f"Failed to select symbol {data.symbol}")

    order_type = mt5.ORDER_TYPE_BUY if data.action.upper() == "BUY" else mt5.ORDER_TYPE_SELL
    price = symbol_info.ask if data.action.upper() == "BUY" else symbol_info.bid

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": data.symbol,
        "volume": float(data.volume),
        "type": order_type,
        "price": price,
        "sl": float(data.sl),
        "tp": float(data.tp),
        "deviation": 20,
        "magic": 888111,
        "comment": "Alpha Matrix Pro Exec",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)

    if result.retcode != mt5.TRADE_RETCODE_DONE:
        raise HTTPException(
            status_code=400, 
            detail=f"Trade execution failed. Retcode: {result.retcode}"
        )

    return {
        "status": "success",
        "ticket": result.order,
        "symbol": data.symbol,
        "volume": result.volume,
        "price": result.price
    }


# 24/7 BOT ENDPOINTS

@app.post("/bot/start")
async def start_bot(data: BotStartRequest, background_tasks: BackgroundTasks):
    """Start 24/7 automated trading bot"""
    global trading_bot
    
    try:
        if trading_bot and trading_bot.is_running:
            raise HTTPException(status_code=400, detail="Bot is already running")
        
        # Create bot configuration
        config = BotConfig()
        config.MT5_SERVER = data.server
        config.MT5_LOGIN = data.login
        config.MT5_PASSWORD = data.password
        
        # Create bot instance
        trading_bot = TradingBot(config)
        
        # Start bot in background
        background_tasks.add_task(trading_bot.run)
        
        logger.info(f"Bot started for account {data.login}")
        
        return {
            "status": "started",
            "message": "24/7 trading bot is now running",
            "account": data.login
        }
        
    except Exception as e:
        logger.error(f"Bot start error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to start bot: {str(e)}")


@app.post("/bot/stop")
def stop_bot():
    """Stop the trading bot"""
    global trading_bot
    
    try:
        if not trading_bot or not trading_bot.is_running:
            raise HTTPException(status_code=400, detail="Bot is not running")
        
        trading_bot.shutdown()
        logger.info("Bot stopped")
        
        return {
            "status": "stopped",
            "message": "Trading bot has been stopped"
        }
        
    except Exception as e:
        logger.error(f"Bot stop error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to stop bot: {str(e)}")


@app.get("/bot/status")
def get_bot_status():
    """Get current bot status"""
    global trading_bot
    
    if not trading_bot:
        return {
            "status": "inactive",
            "is_running": False,
            "active_trades": 0,
            "daily_trades": 0,
            "message": "No bot instance"
        }
    
    active_trades_count = sum(len(trades) for trades in trading_bot.active_trades.values())
    
    return {
        "status": "active" if trading_bot.is_running else "inactive",
        "is_running": trading_bot.is_running,
        "active_trades": active_trades_count,
        "daily_trades": trading_bot.daily_trades_count,
        "daily_loss": trading_bot.daily_loss,
        "last_updated": trading_bot.last_account_update.isoformat()
    }


@app.get("/bot/trades")
def get_active_trades():
    """Get list of active trades"""
    global trading_bot
    
    if not trading_bot:
        raise HTTPException(status_code=400, detail="No bot instance")
    
    return {
        "active_trades": trading_bot.active_trades,
        "total_count": sum(len(trades) for trades in trading_bot.active_trades.values())
    }


@app.post("/bot/pause")
def pause_bot():
    """Pause bot trading (still connected)"""
    global trading_bot
    
    if not trading_bot:
        raise HTTPException(status_code=400, detail="No bot instance")
    
    trading_bot.config.TRADING_ENABLED = False
    
    return {
        "status": "paused",
        "message": "Bot trading has been paused"
    }


@app.post("/bot/resume")
def resume_bot():
    """Resume bot trading"""
    global trading_bot
    
    if not trading_bot:
        raise HTTPException(status_code=400, detail="No bot instance")
    
    trading_bot.config.TRADING_ENABLED = True
    
    return {
        "status": "resumed",
        "message": "Bot trading has been resumed"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
