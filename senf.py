import click
import shutil
import os

import configparser

######################################################################
# data
######################################################################
COURSE_DIR_STRUCTURE = ["books", "practicals", "exam-preparation", "lecture"]
COURSE_FILES = ["links", ".studyrc", ".info"]

STUDY = None
SEMESTER = None
COURSE = None

## COLORS
RED = "red"
GREEN = "green"
BLUE = "blue"

class Study(object):
    def __init__(self):
        self.study = os.environ.get("STUDY")
        if not self.study:
            raise ValueError

        try:
            self.working_semester = Semester()
        except ValueError:
            print("Please set the $SEMESTER variable.")

        self.semesters = _fetch_semester()

    def _fetch_semester(self):
        self.semester = find_files(self.study, term="semester", files=False)


class Semester(object):
    def __init__(self):
        self.semester = os.environ.get("SEMESTER")
        if not self.semester:
            raise ValueError

        self.courses = find_files(self.semester, files=False)

class Course(object):
    def __init__(self):
        self.course = None

######################################################################
# Output handling
######################################################################
def senf_error(msg):
    click.echo(click.style("[ERROR]: " + msg, fg=RED))

def senf_ok(msg):
    click.echo(click.style("[OK   ]: " + msg, fg=GREEN))

def senf_info(msg):
    click.echo(click.style("[INFO ]: " + msg, fg=BLUE))

def senf(msg):
    click.echo(click.style(msg, fg=BLUE))

######################################################################
# helpers
######################################################################
def touch_file(filename):
    with open(filename, "a"):
        os.utime(filename, None)

def find_files(directory, term="", dirs=True, files=True):
    data = []
    for file in os.listdir(self.study):
        if term in file:
            if dirs and os.path.isdir(file):
                data.append(file)
            if files and os.path.isfile(file):
                data.append(file)
    return data

def read_description():
    pass

######################################################################
# controller
######################################################################
def init_lecture():
    global STUDY
    global SEMESTER
    global COURSE

    STUDY = os.environ.get("STUDY")
    SEMESTER = os.environ.get("SEMESTER")
    COURSE = os.environ.get("COURSE")

    if not (STUDY and SEMESTER):
        senf_error("Could not initialize the environment.")


######################################################################
# callbacks for autocompletion
######################################################################
def get_course(ctx, args, incomplete):
    init_lecture()
    return [os.path.abspath(k) for k in os.listdir(SEMESTER) if incomplete in k]

def get_lecture(ctx, args, incomplete):
    init_lecture()

    if COURSE is not None:
        return [k for k in os.listdir(COURSE) if incomplete in k]
    else:
        return [k for k in os.listdir(SEMESTER) if incomplete in k]

def get_cwd(ctx, args, incomplete):
    init_lecture()
    cwd = os.getcwd()

    return [k for k in os.listdir(cwd) if incomplete in k]

######################################################################
# Command Line Interface
######################################################################
@click.group()
def cli():
    init_lecture()


@cli.command(help="create the base for a new lecture in your current environment")
@click.argument("course", type=click.STRING)
def mklecture(course):
    if os.path.exists(SEMESTER + "/" + course):
        senf_error("This lecture already exists.")
        return

    COURSE_ABS_PATH = SEMESTER + "/" + course + "/"
    os.mkdir(COURSE_ABS_PATH)

    for directory in COURSE_DIR_STRUCTURE:
        os.mkdir(COURSE_ABS_PATH + directory + "/")

    for l_file in COURSE_FILES:
        touch_file(COURSE_ABS_PATH + l_file)


@cli.command(help="move various files to the provided directory")
@click.argument("directory", nargs=1, type=click.Path(), autocompletion=get_lecture)
@click.argument("files", type=click.STRING, nargs=-1, autocompletion=get_cwd)
def mv(directory, files):
    if COURSE:
        dst = COURSE + "/" + directory
    else:
        dst = SEMESTER + "/" + directory

    for f in files:
        shutil.move(f, dst)
        senf_info("Moving file {} to {} ".format(f, dst))

@cli.command(help="")
def ls():
    if SEMESTER:
        courses = os.listdir(SEMESTER)[::-1]

        data = os.linesep.join(courses)
        
        for d in courses:
            config = configparser.ConfigParser()
            info_file = SEMESTER + os.sep + d + os.sep + ".info"
            string = "\t{} -- NONE: ".format(d)
            if os.path.isfile(info_file):
                config.read(info_file)
                string = "\t{} -- {}: {}".format(d, config["DEFAULT"]["CourseName"], config["DEFAULT"]["CourseDescription"])
            senf(string)
    else:
        senf_error("Variable $SEMESTER not set.")

@cli.command(help="just print out the environment variables")
def debug():
    senf_info("STUDY: " + str(os.environ.get("STUDY")))
    senf_info("SEMESTER " + str(os.environ.get("SEMESTER")))
    senf_info("COURSE " + str(os.environ.get("COURSE")))


######################################################################
# process changing commands, which have to be implemented in a shell
# script.
# implementation for the according hints are done in python though
######################################################################
@cli.command()
def workon():
    senf_info("Please use the provided senf-workon bash script for this action")


@cli.command()
def cd():
    senf_info("Please use the provided senf-cd bash script for this action.")
    return
