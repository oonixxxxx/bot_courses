from aiohttp import ClientSession

class HTTPSClent:
    def __init__(self, base_url: str, api_keys: str):
        self._ssesion = ClientSession(
            base_url=base_url,
            headers={
                'X-CMC_PRO_API_KEY': api_keys,
            }
        )

#pro-api.coinmarketcap.com

class CMHTTPSClient:
    async def get_listings(self):
        async with self._ssesion.get('/v1/cryptocurrency/listings/latest') as resp:
            result = await resp.json()

            return result["data"]

    async def get_currency(self, currency_id: int):
        async with self._ssesion.get(
                '/v2/cryptocurrency/quotes/latest',
                params={'id': currency_id}
        ) as resp:
            result = await resp.json()

            return result["data"][str(currency_id)]