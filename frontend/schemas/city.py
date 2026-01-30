from pydantic import BaseModel

class CitySchema(BaseModel):
    id: int
    name: str
