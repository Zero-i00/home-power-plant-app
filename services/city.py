from schemas.city import CityBaseSchema
from sqlalchemy.ext.asyncio import AsyncSession
from models.city import CityModel
from sqlalchemy import select

class CityService:

    @staticmethod
    async def retrieve(session: AsyncSession, id: int) -> CityBaseSchema | None:
        query = select(CityModel).where(CityModel.id == id)

        result = await session.execute(query)
        city = result.scalar_one_or_none()

        if city is None:
            return None

        return CityBaseSchema.model_validate(city)


city_service = CityService()
