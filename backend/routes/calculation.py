from fastapi import APIRouter
from database.session import SessionDep
from services.calculation import calculation_service
from schemas.calculation import CalculationSolarPanelIn, CalculationSolarPanelOut, CalculationWindGeneratorIn, CalculationWindGeneratorOut

router = APIRouter(prefix='/calculation', tags=[' calculation'])

@router.post('/solar/')
async def calculation_solar_panel(
    session: SessionDep,
    data: CalculationSolarPanelIn
) -> CalculationSolarPanelOut:
    result = await calculation_service.solar_station(
        session=session, 
        city_id=data.city_id,
        panel_kpd=data.panel_kpd,
        panel_power=data.panel_power,
        price_energy_sun=data.price_energy_sun,
        price_sun=data.price_sun

    )

    return CalculationSolarPanelOut(total=result)



@router.post('/wind_generator/')
async def calculation_wind_generator(
     session: SessionDep,
    data: CalculationWindGeneratorIn
) -> CalculationWindGeneratorOut:
    result = await calculation_service.wind_generator(
        session=session, 
        city_id=data.city_id,
        blade_length=data. blade_length,
        price_wind=data.price_wind,
        price_energy_wind=data.price_energy_wind 
    )

    return CalculationWindGeneratorOut(total=result)