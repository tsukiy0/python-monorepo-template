from unittest.mock import MagicMock

import pytest
from faker import Faker

from libs.core.models.address import Address, AddressId
from libs.core.services.address_repository import AddressRepository
from libs.core.handlers.save_address_handler import (
    SaveAddressHandler,
    SaveAddressRequest,
)


@pytest.fixture
def address_repository_mock() -> MagicMock:
    return MagicMock(spec=AddressRepository)


@pytest.fixture
def sut(
    address_repository_mock: MagicMock,
) -> SaveAddressHandler:
    return SaveAddressHandler(
        address_repository=address_repository_mock,
    )


@pytest.mark.asyncio
async def test_handle(
    sut: SaveAddressHandler,
    address_repository_mock: MagicMock,
):
    fake = Faker()
    address = Address(
        id=AddressId(value=fake.pystr()),
        street_number=fake.building_number(),
        street_name=fake.street_name(),
        street_type=fake.street_suffix(),
        city=fake.city(),
        state=fake.city(),
        postcode=fake.postcode(),
    )
    request = SaveAddressRequest(address=address)

    await sut.handle(request=request)

    address_repository_mock.save.assert_called_once_with(address=address)
