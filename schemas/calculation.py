from pydantic import BaseModel

class CalculationSolarPanelIn(BaseModel):
    sist_kpd: float
    panel_power: float
    price_sun: float
    city_id: int
    price_energy_sun: float
    


class CalculationSolarPanelOut(BaseModel):
    total: float



# TODO данные, которые пользователь вводит руками
class CalculationWindGeneratorIn(BaseModel):
    city_id: int
    price_wind: float
    blade_length: float
    price_energy_wind: float


class CalculationWindGeneratorOut(BaseModel):
    total: float

