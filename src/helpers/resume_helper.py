import src.schemas.resume as resume_schema
from typing import List


def get_profiles() -> List[resume_schema.Profile]:
    linkedin = resume_schema.Profile("LinkedIn", "Syed Mahdi", "www.linkedin.com/in/smmahdi/")
    github = resume_schema.Profile("GitHub", "smm3123", "www.github.com/smm3123")
    profiles = [linkedin, github]
    return profiles


def get_location() -> resume_schema.Location:
    return resume_schema.Location(None, None, "Houston", "TX")


def get_basics() -> resume_schema.Basics:
    basics = resume_schema.Basics()
    basics.name = "Syed Mahdi"
    basics.label = "Software Engineer"
    basics.email = "syedmahdi3123@gmail.com"
    basics.location = get_location()
    basics.profiles = get_profiles()
    return basics


def get_work() -> List[resume_schema.Work]:
    is_volunteer = False
    quorum = resume_schema.Work(is_volunteer, "Quorum Software", "Software Engineer", "2021-06-14", "Present")
    reyrey = resume_schema.Work(is_volunteer, "Reynolds & Reynolds", "Software Developer", "2019-06-03", "2021-06-04")
    mckesson = resume_schema.Work(is_volunteer, "McKesson Specialty Health", "IT Intern", "2018-05-04", "2018-08-13")
    work = [quorum, reyrey, mckesson]
    return work


def get_resume() -> resume_schema.Resume:
    resume = resume_schema.Resume()
    resume.basics = get_basics()
    resume.work = get_work()
    return resume
