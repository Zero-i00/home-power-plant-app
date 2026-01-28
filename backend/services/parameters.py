from sqlalchemy.ext.asyncio import AsyncSession
from schemas.city import CityParameterSchema
from models.city import CityParameterModel
from sqlalchemy import select

class CityParametersService:

    @staticmethod
    async def list_all(session: AsyncSession) -> list[CityParameterSchema]:
        query = select(CityParameterModel)
        data = await session.execute(query)
        
        parameters = data.scalars().all()

        return [
            CityParameterSchema.model_validate(param) 
            for param in parameters
        ]
    
    @staticmethod
    async def list_by_city_id(session: AsyncSession, city_id: int) -> list[CityParameterSchema]:
        query = select(CityParameterModel).where(CityParameterModel.city_id == city_id)
        data = await session.execute(query)
        
        parameters = data.scalars().all()

        return [
            CityParameterSchema.model_validate(param) 
            for param in parameters
        ]
    

city_parameters_service = CityParametersService()
