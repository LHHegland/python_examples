"""
Define class object for address instances using dataclasses

USAGE: 
  - import classes.address
"""
from dataclasses import dataclass

@dataclass
class Address:
    """
    Define class object for address instances

    Standards:
     - ISO 19160-1:2015
     - United States Postal Service Addressing Standards (Publication 28)

    References:
     - https://designsystem.digital.gov/patterns/create-a-user-profile/address/
     
    """
    type: str = '' # e.g. mailing, physical, main {mailing or physical}, office {mailing or physical}, home {mailing or physical}
    address_1: str = ''
    address_2: str = ''
    address_3: str = ''
    city: str = ''
    state_province: str = ''
    zip_postal_code: str = ''
    country: str = ''