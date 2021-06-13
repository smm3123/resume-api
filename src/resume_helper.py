from src.resume import *


def get_profiles() -> List[Profile]:
    linkedin = Profile("LinkedIn", "Syed Mahdi", "www.linkedin.com/in/smmahdi/")
    github = Profile("GitHub", "smm3123", "www.github.com/smm3123")
    profiles = [linkedin, github]
    return profiles


def get_basics() -> Basics:
    basics = Basics()
    basics.name = "Syed Mahdi"
    basics.label = "Software Engineer"
    basics.email = "syedmahdi3123@gmail.com"
    basics.location = "Houston, TX"
    basics.profiles = get_profiles()
    return basics


def get_resume() -> Resume:
    resume = Resume()
    resume.basics = get_basics()
    return resume
