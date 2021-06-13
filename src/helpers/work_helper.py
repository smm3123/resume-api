from src.schemas.resume import Work
is_volunteer = False


def get_quorum_work() -> Work:
    quorum = Work(is_volunteer, "Quorum Software", "Software Engineer", "2021-06-14", "Present")
    return quorum


def get_reyrey_work() -> Work:
    reyrey = Work(is_volunteer, "Reynolds & Reynolds", "Software Developer", "2019-06-03", "2021-06-04")
    reyrey.summary = "Worked as a full stack .NET software engineer on AppOne's applications"
    reyrey.highlights = [
        "Developed full-stack .NET Web Forms and MVC applications for AppOne, an indirect lending SaaS solution, using "
        "C#, SQL, HTML, CSS/Sass, and JavaScript/jQuery",
        "Maintained various MS SQL Server databases, using SQL Server Profiler to troubleshoot issues and SQL Server "
        "Management Studio to write queries and stored procedures",
        "Handled continuous integration and continuous deployment through Jenkins and Octopus Deploy",
        "Responsible for AppOne's forms engine, utilizing the iText library to process PDFs for the applications' "
        "users",
        "Led integration of AppOne and ReySign to provide users with a seamless process for applying signatures to "
        "forms",
        "Integrated AppOne with Product Rating and Booking's (PRB) API to give users the ability to configure products "
        "and forms through PRB and import them back to AppOne",
        "Displayed initiative through refactoring all instances of legacy inline server-side code to code-behind model "
        "to improve separation of concerns and to allow the build server to properly catch compilation errors",
        "Researched and programmed an internal tool that used AppOne's forms engine to enable the support team to "
        "manage custom forms and form prompts"
    ]
    return reyrey


def get_mckesson_work() -> Work:
    mckesson = Work(is_volunteer, "McKesson Specialty Health", "IT Intern", "2018-05-04", "2018-08-13")
    mckesson.summary = "Interned with the IT Infrastructure Library (ITIL) team"
    mckesson.highlights = [
        "Automated the Change Manager's workflow using Python, reducing the weekly time needed to complete the tasks "
        "from over 4 hours to under 5 minutes",
        "Facilitated the installation and testing of two major SalesForce IT Service Management system updates",
        "Completed projects and reduced backlog items in an Agile environment using Jira for project management",
        "Contributed to IT Infrastructure Library (ITIL) processes such as Problem, Change, and Incident Management"
    ]
    return mckesson
