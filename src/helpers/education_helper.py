from src.schemas.resume import Education


def get_ut_austin_education() -> Education:
    ut_austin = Education("University of Texas at Austin", "Computer Science", "Master of Science")
    ut_austin.start_date = "2021-08-25"
    ut_austin.end_date = "Present"
    return ut_austin


def get_osu_education() -> Education:
    osu = Education("Oregon State University", "Computer Science", "Bachelor of Science")
    osu.start_date = "2019-09-09"
    osu.end_date = "2021-08-13"
    osu.gpa = "3.76"
    osu.courses = [
        "CS 161 - Intro to Computer Science I",
        "CS 162 - Intro to Computer Science II",
        "CS 225 - Discrete Mathematics",
        "CS 261 - Data Structures",
        "CS 271 - Computer Architecture and Assembly Language",
        "CS 290 - Web Development",
        "CS 325 - Analysis of Algorithms",
        "CS 344 - Operating Systems I",
        "CS 352 - Intro to Usability Engineering",
        "CS 361 - Software Engineer I",
        "CS 362 - Software Engineering II",
        "CS 372 - Intro to Computer Networks",
        "CS 450 - Computer Graphics",
        "CS 467 - Capstone Project"
    ]
    return osu


def get_uh_education() -> Education:
    uh = Education("University of Houston", "Management Information Systems", "Bachelor of Business Administration")
    uh.start_date = "2015-08-24"
    uh.end_date = "2019-05-18"
    uh.gpa = "Cumulative: 3.54, Major: 4.0"
    uh.course = [
        "MIS 3300 - Intro to Computers and MIS",
        "MIS 3360 - Systems Analysis and Design",
        "MIS 3370 - Information Systems Development Tools",
        "MIS 3376 - Database Management I",
        "MIS 3371 - Transaction Processing I",
        "MIS 4372 - Transaction Processing II",
        "MIS 4378 - Administration of Information Systems",
        "MIS 4374 - IT Project Management",
        "MIS 4397 - Open Systems",
        "MIS 4397 - R Programming for Business Analytics"
    ]
    return uh
