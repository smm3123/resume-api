import src.resume as resume_classes
from typing import List


def get_profiles() -> List[resume_classes.Profile]:
    linkedin = resume_classes.Profile("LinkedIn", "Syed Mahdi", "www.linkedin.com/in/smmahdi/")
    github = resume_classes.Profile("GitHub", "smm3123", "www.github.com/smm3123")
    profiles = [linkedin, github]
    return profiles


def get_basics() -> resume_classes.Basics:
    basics = resume_classes.Basics()
    basics.name = "Syed Mahdi"
    basics.label = "Software Engineer"
    basics.email = "syedmahdi3123@gmail.com"
    basics.location = "Houston, TX"
    basics.profiles = get_profiles()
    return basics


def get_resume() -> resume_classes.Resume:
    resume = resume_classes.Resume()
    resume.basics = get_basics()
    return resume
