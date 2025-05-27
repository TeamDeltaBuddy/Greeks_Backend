from fastapi import FastAPI
from dhan_api import get_option_chain

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Deltabuddy backend running"}

@app.get("/option-chain/{symbol}")
def option_chain(symbol: str):
    return get_option_chain(symbol)
