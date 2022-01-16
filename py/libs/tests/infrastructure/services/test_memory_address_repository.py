import pytest

from libs.infrastructure.services.memory_address_repository import (
    MemoryAddressRepository,
)
from tests.core.models.test_address import generate_address


@pytest.fixture
def sut() -> MemoryAddressRepository:
    return MemoryAddressRepository()


@pytest.mark.asyncio
async def test_save_and_get(
    sut: MemoryAddressRepository,
):
    address = generate_address()

    await sut.save(address=address)
    actual = await sut.get(address.id)

    assert actual == address


@pytest.mark.asyncio
async def test_get__when_not_exists_then_raise(
    sut: MemoryAddressRepository,
):
    address = generate_address()

    with pytest.raises(FileNotFoundError):
        await sut.get(address.id)
