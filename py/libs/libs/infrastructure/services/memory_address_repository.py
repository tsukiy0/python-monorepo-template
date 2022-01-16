from typing import List

from libs.core.models.address import Address, AddressId
from libs.core.services.address_repository import AddressRepository


class MemoryAddressRepository(AddressRepository):
    __store: List[Address]

    def __init__(self) -> None:
        self.__store = []

    async def save(self, address: Address) -> None:
        self.__store.append(address)

    async def get(self, address_id: AddressId) -> Address:
        try:
            address = [x for x in self.__store if x.id == address_id]
            return address[0]
        except IndexError:
            raise FileNotFoundError("address does not exist")
