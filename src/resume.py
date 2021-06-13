from datetime import datetime
from typing import List, Optional


class Profile:
    network: str
    username: str
    url: str


class Location:
    address: str
    postal_code: str
    city: str
    country_code: str
    region: str


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


class Education:
    institution: str
    area: str
    study_type: str
    start_date: datetime
    end_date: datetime
    gpa: str
    courses: List[str]


class Award:
    title: str
    date: datetime
    awarder: str
    summary: str


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


class Language:
    language: str
    fluency: str


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
