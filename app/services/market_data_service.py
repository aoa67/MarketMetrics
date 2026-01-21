import os
import requests

ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

def get_top_movers_alpha_vantage():
    """
    Alpha Vantage has a TOP_GAINERS_LOSERS endpoint.
    Returns raw JSON.
    """
    if not ALPHA_VANTAGE_KEY:
        raise RuntimeError("Missing ALPHA_VANTAGE_API_KEY in environment variables")

    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TOP_GAINERS_LOSERS",
        "apikey": ALPHA_VANTAGE_KEY,
    }

    r = requests.get(url, params=params, timeout=20)
    r.raise_for_status()
    return r.json()
