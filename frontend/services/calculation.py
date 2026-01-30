from api.client import APIClient
from schemas.calculation import (
    CalculationSolarPanelIn,
    CalculationSolarPanelOut,
    CalculationWindGeneratorIn,
    CalculationWindGeneratorOut,
)


class CalculationService:

    @staticmethod
    async def calculate_solar(
        client: APIClient,
        data: CalculationSolarPanelIn,
    ) -> CalculationSolarPanelOut:
        result = await client.post("/calculation/solar/", data.model_dump())
        return CalculationSolarPanelOut.model_validate(result)


    @staticmethod
    async def calculate_wind_generator(
        client: APIClient,
        data: CalculationWindGeneratorIn,
    ) -> CalculationWindGeneratorOut:
        result = await client.post("/calculation/wind_generator/", data.model_dump())
        return CalculationWindGeneratorOut.model_validate(result)


calculation_service = CalculationService()
