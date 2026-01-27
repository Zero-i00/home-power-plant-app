from pydantic import BaseModel, ConfigDict

class CityParameterSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int

    insolation: int
    wind_speed: int
    air_density: int

    city_id: int


class CitySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str

    parameters: list[CityParameterSchema]
