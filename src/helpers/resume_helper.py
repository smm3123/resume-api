import src.schemas.resume as resume_schema
import src.helpers.work_helper as work_helper
import src.helpers.education_helper as education_helper
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
    quorum = work_helper.get_quorum_work()
    reyrey = work_helper.get_reyrey_work()
    mckesson = work_helper.get_mckesson_work()
    work = [quorum, reyrey, mckesson]
    return work


def get_education() -> List[resume_schema.Education]:
    ut_austin = education_helper.get_ut_austin_education()
    osu = education_helper.get_osu_education()
    uh = education_helper.get_uh_education()
    education = [ut_austin, osu, uh]
    return education


def get_skills() -> List[resume_schema.Skill]:
    skills = ["C#", "SQL (MS SQL Server)", "Python", "JavaScript", "HTML", "CSS/Sass", "XML", "XSLT", "C", "Java",
              "ASP.NET", "jQuery", "Bootstrap", "Node.js", "Selenium", "MS Unit Test Framework", "iText",
              "Git", "SVN", "Visual Studio", "Visual Studio Code", "SQL Server Management Studio",
              "Jenkins", "Octopus Deploy"]
    skills_list = []
    for skill in skills:
        skills_list.append(resume_schema.Skill(skill))
    return skills_list


def get_awards() -> List[resume_schema.Award]:
    academic_scholarship = resume_schema.Award("Academic Scholarship", "University of Houston")
    deans_list = resume_schema.Award("Dean's List", "University of Houston")
    magna_cum_laude = resume_schema.Award("Magna Cum Laude", "University of Houston")
    awards = [academic_scholarship, deans_list, magna_cum_laude]
    return awards


def get_languages() -> List[resume_schema.Language]:
    english = resume_schema.Language("English", "Native")
    urdu = resume_schema.Language("Urdu", "Fluent")
    spanish = resume_schema.Language("Spanish", "Beginner")
    languages = [english, urdu, spanish]
    return languages


def get_resume() -> resume_schema.Resume:
    resume = resume_schema.Resume()
    resume.basics = get_basics()
    resume.work = get_work()
    resume.education = get_education()
    resume.skills = get_skills()
    resume.awards = get_awards()
    resume.languages = get_languages()
    return resume
