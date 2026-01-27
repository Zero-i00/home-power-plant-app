from pydantic import BaseModel

class CalculationSolarPanelIn(BaseModel):
    panel_kpd: float
    panel_power: float
    city_id: int

class CalculationSolarPanelOut(BaseModel):
    total: float

