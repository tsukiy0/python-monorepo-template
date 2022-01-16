from dataclasses import dataclass

from libs.core.models.address import Address
from libs.core.services.address_repository import AddressRepository


@dataclass
class SaveAddressRequest:
    address: Address


class SaveAddressHandler:
    __address_repository: AddressRepository

    def __init__(
        self,
        address_repository: AddressRepository,
    ) -> None:
        self.__address_repository = address_repository

    async def handle(self, request: SaveAddressRequest) -> None:
        await self.__address_repository.save(address=request.address)
