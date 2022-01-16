from typing import Dict

from libs.core.models.address import Address, AddressId
from libs.core.services.address_repository import AddressRepository


class MemoryAddressRepository(AddressRepository):
    __store: Dict[AddressId, Address]

    def __init__(self) -> None:
        self.__store = {}

    async def save(self, address: Address) -> None:
        pass

    async def get(self, address_id: AddressId) -> Address:
        pass
