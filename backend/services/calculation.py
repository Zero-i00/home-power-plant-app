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

        annual = total * price_energy_sun

        cumulative = 0
        ears = 0
        while price_sun > cumulative:
            year_income = annual * (1.07 ** ears)
            remaining = price_sun - cumulative
            if remaining <= year_income:
                ears += round(remaining / year_income, 2)
                break
            cumulative += year_income
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

        
        annual1 = total1 * price_energy_wind
        cumulative1 = 0
        ears1 = 0
        while price_wind > cumulative1:
            year_income = annual1 * (1.07 ** ears1)
            remaining = price_wind - cumulative1
            if remaining <= year_income:
                ears1 += round(remaining / year_income, 2)
                break
            cumulative1 += year_income
            ears1 += 1

        return ears1

    
    # @staticmethod
    # async def wind_generator(session: AsyncSession, city_id: int, blade_length: float, sist_kpd: float, panel_power: float, price_total: float, price_energy_total: float) -> float:
    #     city = await city_service.retrieve(session, city_id)

    #     if city is None:
    #         raise HTTPException(
    #             status_code=status.HTTP_404_NOT_FOUND,
    #             detail='Не удалось найти такой город'
    #         )
    
    #     parameters = await city_parameters_service.list_by_city_id(session, city.id)

    #     if parameters is None:
    #         raise HTTPException(
    #             status_code=status.HTTP_404_NOT_FOUND,
    #             detail=f'Не удалось найти параметры для города {city.name}'

    #         )
        

    #     total2 = 0

    #     for param in parameters:
    #         day_peer_month = MonthDaysEnum[param.month.name]
    #         total2 += (0.5 * param.air_density * ((blade_length * blade_length) * 3.14)  * (param.wind_speed*param.wind_speed*param.wind_speed) * 0.35 * 24 * day_peer_month * 0.75) + (param.insolation * panel_power  *  day_peer_month * sist_kpd)


    #     result2 = total2 * price_energy_total
    #     ears2 = 0
    #     while price_total > result2:
    #         result2 *= 1.07
    #         ears2 += 1

    #     return ears2

        



calculation_service = Calculation()
