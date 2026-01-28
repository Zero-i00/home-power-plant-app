from fastapi import FastAPI
from config import settings
from database.orm import Base
from database.session import engine, session_factory
from database.seeder import seed_database
from contextlib import asynccontextmanager
from routes import calculation_router

from models import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with session_factory() as session:
        await seed_database(session)
    yield


app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan
)

app.include_router(calculation_router)

@app.get('/')
async def health_check():
    return {
        "ok": True
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        "main:app",
        reload=True,
        host=settings.app_host,
        port=settings.app_port, 
    )