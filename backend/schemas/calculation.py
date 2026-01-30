from pydantic import BaseModel

class CalculationSolarPanelIn(BaseModel):
    sist_kpd: float
    panel_power: float
    price_sun: float
    city_id: int
    price_energy_sun: float
    


class CalculationSolarPanelOut(BaseModel):
    years: int
    months: int



# TODO данные, которые пользователь вводит руками
class CalculationWindGeneratorIn(BaseModel):
    city_id: int
    price_wind: float
    blade_length: float
    price_energy_wind: float


class CalculationWindGeneratorOut(BaseModel):
    years: int
    months: int



class CalculationAllGeneratorIn(BaseModel):
    city_id: int
    
    # Солнечная
    sist_kpd: float
    panel_power: float

    # Ветреная
    blade_length: float
    
    
    
    price_total: float
    price_energy_total: float


class CalculationAllGeneratorOut(BaseModel):
    total: float

