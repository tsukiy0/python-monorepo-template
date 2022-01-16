from faker import Faker

from libs.core.models.address import Address, AddressId


def generate_address() -> Address:
    fake = Faker()
    return Address(
        id=AddressId(value=fake.pystr()),
        street_number=fake.building_number(),
        street_name=fake.street_name(),
        street_type=fake.street_suffix(),
        city=fake.city(),
        state=fake.city(),
        postcode=fake.postcode(),
    )
