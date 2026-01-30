import aiohttp


class APIClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self._session: aiohttp.ClientSession | None = None

    async def _get_session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(self.base_url)
        return self._session

    async def close(self):
        if self._session and not self._session.closed:
            await self._session.close()

    async def get(self, path: str) -> dict:
        session = await self._get_session()
        async with session.get(path) as resp:
            resp.raise_for_status()
            return await resp.json()

    async def post(self, path: str, payload: dict) -> dict:
        session = await self._get_session()
        async with session.post(path, json=payload) as resp:
            resp.raise_for_status()
            return await resp.json()
