"""
Define class object for organizational role instances using dataclasses

USAGE: 
  - import classes.role
"""
import dataclasses
import classes.telephone
import classes.email
import classes.address
import classes.url

@dataclasses.dataclass
class Role:
    """
    Define class object for organizational role instances using dataclasses

    Standards:
     - International Telecommunication Union Telecommunication Standardization Sector (ITU-T) E.123
     - International Telecommunication Union Telecommunication Standardization Sector (ITU-T) E.164
     - ISO 19160-1:2015 Addressing
     - United States Postal Service Addressing Standards (Publication 28)

    References:
     - https://designsystem.digital.gov/patterns/create-a-user-profile/contact-preferences/
     - https://designsystem.digital.gov/patterns/create-a-user-profile/phone-number/
     - https://designsystem.digital.gov/patterns/create-a-user-profile/email-address/
     - https://designsystem.digital.gov/patterns/create-a-user-profile/address/
     
    """
    role: str = '' # job title, position
    organization: str = ''
    telephones: list[classes.telephone.Telephone] = dataclasses.field(default_factory=list)
    emails: list[classes.email.Email] = dataclasses.field(default_factory=list)
    addresses: list[classes.address.Address] = dataclasses.field(default_factory=list)
    urls: list[classes.url.URL] = dataclasses.field(default_factory=list)