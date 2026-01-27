from pydantic import BaseModel

class CalculationSolarPanelIn(BaseModel):
    panel_kpd: float
    panel_power: float
    city_id: int

class CalculationSolarPanelOut(BaseModel):
    total: float



# TODO данные, которые пользователь вводит руками
class CalculationWindGeneratorIn(BaseModel):
    city_id: int



class CalculationWindGeneratorOut(BaseModel):
    total: float

