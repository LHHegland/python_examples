"""
Define class object for Internet URL (Uniform Resource Locator) instances using dataclasses

USAGE: 
  - import classes.url
"""
from dataclasses import dataclass

@dataclass
class URL:
    """
    Define class object for Internet URL (Uniform Resource Locator) instances using dataclasses

    Standards:
     - International Telecommunication Union Telecommunication Standardization Sector (ITU-T) E.123
     
    References: None
    """
    type: str = '' # website, blog, calendar, GitHub, Facebook, Twitter, Instagram, YouTube, LinkedIn, FTP, etc.
    address: str = ''