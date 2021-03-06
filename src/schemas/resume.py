"""
Class definitions based off of the JSON Resume schemas found here: https://jsonresume.org/schema/
"""

from datetime import datetime
from typing import List, Optional


class Profile:
    network: str
    username: str
    url: str

    def __init__(self, network: str, username: str, url: str):
        self.network = network
        self.username = username
        self.url = url


class Location:
    address: str
    postal_code: str
    city: str
    state: str
    country_code: str
    region: str

    def __init__(self, address: str, postal_code: str, city: str, state: str):
        self.address = address
        self.postal_code = postal_code
        self.city = city
        self.state = state


class Basics:
    name: str
    label: str
    picture: str
    email: str
    phone: str
    website: str
    summary: str
    location: Location
    profiles: List[Profile]


class Work:
    organization: Optional[str]
    company: Optional[str]
    position: str
    website: str
    start_date: datetime
    end_date: datetime
    summary: str
    highlights: List[str]

    def __init__(self, is_volunteer: bool, name: str, position: str, start_date: datetime, end_date: datetime):
        if is_volunteer:
            self.organization = name
        else:
            self.company = name
        self.position = position
        self.start_date = start_date
        self.end_date = end_date


class Education:
    institution: str
    area: str
    study_type: str
    start_date: datetime
    end_date: datetime
    gpa: str
    courses: List[str]

    def __init__(self, institution: str, area: str, study_type: str):
        self.institution = institution
        self.area = area
        self.study_type = study_type


class Award:
    title: str
    date: datetime
    awarder: str
    summary: str

    def __init__(self, title: str, awarder: str):
        self.title = title
        self.awarder = awarder


class Publication:
    name: str
    publisher: str
    release_date: datetime
    website: str
    summary: str


class Skill:
    name: str
    level: str
    keywords: List[str]

    def __init__(self, name: str, level: str, keywords: List[str]):
        self.name = name
        self.level = level
        self.keywords = keywords


class Language:
    language: str
    fluency: str

    def __init__(self, language: str, fluency: str):
        self.language = language
        self.fluency = fluency


class Interest:
    name: str
    keywords: List[str]


class Reference:
    name: str
    reference: str


class Resume:
    basics: Basics
    work: List[Work]
    volunteer: List[Work]
    education: List[Education]
    awards: List[Award]
    publications: List[Publication]
    skills: List[Skill]
    languages: List[Language]
    interests: List[Interest]
    references: List[Reference]
