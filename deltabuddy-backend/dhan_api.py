import os
import requests
from dotenv import load_dotenv

load_dotenv()

DHAN_BASE_URL = os.getenv("DHAN_BASE_URL")
CLIENT_ID = os.getenv("DHAN_CLIENT_ID")
ACCESS_TOKEN = os.getenv("DHAN_ACCESS_TOKEN")

HEADERS = {
    "access-token": ACCESS_TOKEN,
    "client-id": CLIENT_ID
}

def get_option_chain(symbol: str):
    url = f"{DHAN_BASE_URL}/options/option-chain"
    params = {"symbol": symbol}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()
