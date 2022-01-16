from unittest.mock import MagicMock

import pytest

from libs.core.handlers.save_address_handler import (
    SaveAddressHandler,
    SaveAddressRequest,
)
from libs.core.services.address_repository import AddressRepository
from tests.core.models.test_address import generate_address


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
    request = SaveAddressRequest(address=generate_address())

    await sut.handle(request=request)

    address_repository_mock.save.assert_called_once_with(address=request.address)
