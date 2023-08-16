import httpx


async def get_exchange_rate(base_currency: str, target_currency: str) -> float:
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        return data["rates"].get(target_currency, 0.0)
