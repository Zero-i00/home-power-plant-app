from pydantic import BaseModel, ConfigDict
from models.city import MonthEnum

class CityParameterSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int

    month: MonthEnum

    insolation: int
    wind_speed: int
    air_density: int

    city_id: int


class CityBaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class CitySchema(CityBaseSchema):
    parameters: list[CityParameterSchema]
