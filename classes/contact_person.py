"""
Define class object for personal contact information instances using dataclasses

USAGE: 
  - import classes.contact_person
"""
import dataclasses
import classes.person_name
import classes.telephone
import classes.email
import classes.address
import classes.url
import classes.role

@dataclasses.dataclass
class Contact_Person:
    """
    Class for a contact person object

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
    name: classes.person_name.Person_Name = dataclasses.field(default_factory=classes.person_name.Person_Name)
    roles: list[classes.role.Role] = dataclasses.field(default_factory=list)
    telephones: list[classes.telephone.Telephone] = dataclasses.field(default_factory=list)
    emails: list[classes.email.Email] = dataclasses.field(default_factory=list)
    addresses: list[classes.address.Address] = dataclasses.field(default_factory=list)
    urls: list[classes.url.URL] = dataclasses.field(default_factory=list)