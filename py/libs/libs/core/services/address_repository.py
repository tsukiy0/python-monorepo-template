from typing import Protocol

from libs.core.models.address import Address, AddressId


class AddressRepository(Protocol):
    async def save(self, address: Address) -> None:
        pass

    async def get(self, address_id: AddressId) -> Address:
        pass
