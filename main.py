from fastapi import FastAPI
from currency_api.exchange_rate import get_exchange_rate
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Currency Exchange API"}

@app.get("/exchange_rate/")
async def get_currency_exchange_rate(base_currency: str, target_currency: str):
    exchange_rate = await get_exchange_rate(base_currency, target_currency)
    return {"base_currency": base_currency, "target_currency": target_currency, "exchange_rate": exchange_rate}


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)