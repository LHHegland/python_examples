"""
Define class object for personal name instances using dataclasses

USAGE: 
  - import classes.person_name
"""
import dataclasses

@dataclasses.dataclass
class Person_Name:
    """
    Define class object for personal name instances using dataclasses

    Standards: No official standards exist.

    References:
     - https://designsystem.digital.gov/patterns/create-a-user-profile/name/

    """
    prefix: str = ''
    first: str = ''
    middle: str = ''
    last: str = ''
    suffix: str = ''
    credentials: list[str] = dataclasses.field(default_factory=list)