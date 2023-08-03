"""
Define class object for telephone instances using dataclasses

USAGE: 
  - import classes.telephone
"""
from dataclasses import dataclass

@dataclass
class Telephone:
    """
    Define class object for telephone instances

    Standards:
     - International Telecommunication Union Telecommunication Standardization Sector (ITU-T) E.123
     - International Telecommunication Union Telecommunication Standardization Sector (ITU-T) E.164

    References:
     - https://designsystem.digital.gov/patterns/create-a-user-profile/phone-number/
     
    """
    type: str = '' # e.g. mobile, main {voice or tty or fax}, office {voice or tty or fax}, home {voice or tty or fax}
    number: str = ''