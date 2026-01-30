from fastapi import status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from services import city_service, city_parameters_service
from models.city import MonthDaysEnum

class Calculation:

    @staticmethod
    async def solar_station(session: AsyncSession, city_id: int, panel_power: float, sist_kpd: float, price_energy_sun: float, price_sun: float ) -> float:
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
            total += param.insolation * panel_power  *  day_peer_month * sist_kpd

        result = total * price_energy_sun

        ears = 0
        while price_sun > result:
            result * 1.07

            ears += 1


        return ears


    
    @staticmethod
    async def wind_generator(session: AsyncSession, city_id: int, blade_length: float, price_energy_wind: float, price_wind: float) -> float:
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
        
        total1 = 0

        for param in parameters:
            day_peer_month = MonthDaysEnum[param.month.name]
            total1 += 0.5 * param.air_density * ((blade_length * blade_length) * 3.14)  * (param.wind_speed*param.wind_speed*param.wind_speed) * 0.35 * 24 * day_peer_month * 0.75 

        
        result1 = total1 * price_energy_wind
        ears1 = 0
        while price_wind > result1:
            result1 * 1.07

            ears1 += 1
        
        
        return ears1

    
calculation_service = Calculation()
