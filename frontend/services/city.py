from api.client import APIClient
from schemas.city import (
    CitySchema,
)

class CityService:

    @staticmethod
    async def list(
        client: APIClient
    ) -> list[CitySchema]:
        result = await client.get('/city')
        return [
            CitySchema.model_validate(city)
            for city in result
        ]


city_service = CityService()
