from fastapi import FastAPI
from libs.core.handlers.save_address_handler import (
    SaveAddressHandler,
    SaveAddressRequest,
)
from libs.infrastructure.services.memory_address_repository import (
    MemoryAddressRepository,
)

app = FastAPI()


@app.get("/hello")
async def hello():
    return "hello!"


@app.get("/address/save")
async def save(request: SaveAddressRequest):
    handler = SaveAddressHandler(address_repository=MemoryAddressRepository())
    await handler.handle(request)
