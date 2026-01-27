from fastapi import status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from services import city_service, city_parameters_service
from models.city import MonthDaysEnum

class Calculation:

    @staticmethod
    async def solar_station(session: AsyncSession, city_id: int, panel_power: float, panel_kpd: float) -> float:
        city = await city_service.retrieve(session, city_id)

        if city is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Не удалось найти такой город'
            )
    
        parameters = await city_parameters_service.list_by_city_id(session, city.id)

        if parameters is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Не удалось найти параметры для города {city.name}'
            )
        
        total = 0

        for param in parameters:
            day_peer_month = MonthDaysEnum[param.month.name]
            total += param.insolation * panel_power * panel_kpd * day_peer_month

        return total
    
    # TODO написать функцию вычислений для генератора ветра
    # session: AsyncSession, city_id: int нужно через , дополнить параметрами из CalculationWindGeneratorIn 
    @staticmethod
    async def wind_generator(session: AsyncSession, city_id: int) -> float:
        #  Копируешь всё из solar_station и меняешь только вычисления в for
        ...

    
calculation_service = Calculation()
