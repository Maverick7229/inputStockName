# tools/stock_tools.py
import yfinance as yf

def get_stock_info(ticker: str) -> str:

    if not ticker.endswith('.NS') and not ticker.endswith('.BO') and not '.' in ticker:
        ticker += '.NS'
    stock = yf.Ticker(ticker)
    info = stock.info
    return f"""
    Ticker: {ticker}
    Name: {info.get('longName', 'N/A')}
    Sector: {info.get('sector', 'N/A')}
    Market Cap: {info.get('marketCap', 'N/A')}
    52 Week High: {info.get('fiftyTwoWeekHigh', 'N/A')}
    52 Week Low: {info.get('fiftyTwoWeekLow', 'N/A')}
    PE Ratio: {info.get('trailingPE', 'N/A')}
    """

def get_recent_trends(ticker: str, days=int(5)) -> str:
    if not ticker.endswith('.NS') and not ticker.endswith('.BO') and not '.' in ticker:
        ticker += '.NS'

    stock = yf.Ticker(ticker)
    hist = stock.history(period="6mo")
    if hist.empty:
        return "No historical data available."
    recent_close = hist['Close'][-days:]
    trend = "upward" if recent_close[-1] > recent_close[0] else "downward"
    return f"The stock has shown a {trend} trend over the last {days} days:\n{recent_close.to_string()}"


