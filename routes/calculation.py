from fastapi import APIRouter
from database.session import SessionDep
from services.calculation import calculation_service
from schemas.calculation import CalculationSolarPanelIn, CalculationSolarPanelOut

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
    )

    return CalculationSolarPanelOut(total=result)

