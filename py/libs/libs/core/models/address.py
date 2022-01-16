from dataclasses import dataclass


@dataclass
class AddressId:
    value: str


@dataclass
class Address:
    id: AddressId
    street_number: str
    street_name: str
    street_type: str
    city: str
    state: str
    postcode: str
