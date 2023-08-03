"""
Define class object for email instances using dataclasses

USAGE: 
  - import classes.email
"""
from dataclasses import dataclass

@dataclass
class Email:
    """
    Define class object for email instances

    Standards:
     - International Telecommunication Union Telecommunication Standardization Sector (ITU-T) E.123

    References:
     - https://designsystem.digital.gov/patterns/create-a-user-profile/email-address/
     
    """
    type: str = '' # e.g. main, work, school, or personal
    address: str = ''