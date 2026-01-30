from fastapi import APIRouter
from schemas.city import CityBaseSchema
from database.session import SessionDep
from services.city import city_service

router = APIRouter(prefix='/city', tags=['city'])


@router.get('/')
async def city_list_route(
    session: SessionDep,
) ->list[CityBaseSchema]:
    return await city_service.list(session)

