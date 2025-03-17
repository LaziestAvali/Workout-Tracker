from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(fast_api_object: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

@app.get('/')
async def test():
    return {'test': True}