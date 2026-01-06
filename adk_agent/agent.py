from google.adk.agents import Agent
from .model.litellm_model.model_config import litellm_model
import json
import yfinance as yf

def get_stock_price(stock_code: str) -> str:
    """
    透過 Yahoo Finance 取得台股即時股價
    """
    # 處理台股後綴，預設加上 .TW (上市)，若找不到可能需要嘗試 .TWO (上櫃)
    # 這裡為了範例簡化，我們先假設是上市股票
    ticker = f"{stock_code}.TW"
    
    try:
        stock = yf.Ticker(ticker)
        # 取得盤中即時資訊 (fast_info 通常比 info 更即時且讀取更快)
        price = stock.fast_info['last_price']
        
        # 為了美觀，將價格四雪五入到小數點後兩位
        formatted_price = f"{price:.2f}"
        
        return json.dumps({
            "stock_code": stock_code,
            "price": formatted_price,
            "currency": "TWD",
            "source": "Yahoo Finance"
        })
        
    except Exception as e:
        return json.dumps({"error": f"無法取得資料: {str(e)}"})

root_agent = Agent(
    name="stock_agent",
    model=litellm_model,
    description="Agent to answer questions about the stock price",
    instruction=(
        "You are a helpful assistant that can check stock prices. "
        "1. Identify the 4-digit stock code from the user input. "
        "2. Call the `get_stock_price` tool EXACTLY ONCE. "
        "3. Once you receive the return value (even if it is just a number), "
        "IMMEDIATELY generate the final answer 'The price is XXX'. "
        "DO NOT call the tool again if you already have a numeric result."
    ),
    tools=[get_stock_price],
)
