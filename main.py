from fastapi import FastAPI
from config import settings
from database.orm import Base
from database.session import engine
from contextlib import asynccontextmanager

from models import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title=settings.app_name,
    lifespan=lifespan
)

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