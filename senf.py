import click
import shutil
import os

######################################################################
# data
######################################################################
COURSE_DIR_STRUCTURE = [
                "books",
                "practicals",
                "exam-preparation",
                "lecture"
                ]

COURSE_FILES = [
                "links",
                ".studyrc"
                ]

STUDY = None
SEMESTER = None
COURSE = None

## COLORS
RED = "red"
GREEN = "green"
BLUE = "blue"

######################################################################
# Output handling
######################################################################
def senf_error(msg):
    click.echo(click.style("[ERROR]: " + msg, fg=RED))

def senf_ok(msg):
    click.echo(click.style("[OK   ]: " + msg, fg=GREEN))

def senf_info(msg):
    click.echo(click.style("[INFO ]: " + msg, fg=BLUE))

######################################################################
# helpers
######################################################################
def touch_file(filename):
    with open(filename, 'a'):
        os.utime(filename, None)

######################################################################
# controller
######################################################################
def init_lecture():
    global STUDY
    global SEMESTER
    global COURSE
    
    if os.environ['TEST']:
        # print("THIS IS A TEST ENVIRONMENT!!!")
        SEMESTER = os.path.expanduser(os.getcwd() + "/test/")
        COURSE = os.path.expanduser(SEMESTER + "test_lecture/")
        # print(SEMESTER)
    else:
        semester_tmp = os.environ['SEMESTER']
        study_tmp = os.environ['STUDY']
        course_tmp = os.environ['COURSE']

        if course_tmp:
            COURSE = course_tmp

        if semester_tmp and study_tmp:
            SEMESTER = os.path.expanduser(semester_tmp)
            STUDY = os.path.expanduser(study_tmp)
        else:
            senf_error("Could not initialize the environment.")


######################################################################
# callbacks for autocompletion 
######################################################################
def get_course(ctx, args, incomplete):
    init_lecture()
    return [k for k in os.listdir(SEMESTER) if incomplete in k]

######################################################################
# Command Line Interface 
######################################################################
@click.group()
def cli():
    init_lecture()

@cli.command()
@click.argument("course", required=False, type=click.STRING, autocompletion=get_course)
def cd(course=None):
    global COURSE
    if course:
        senf_error("THIS FUNCTION IS NOT YET IMPLEMENTED")
    else:
        os.chdir(COURSE)
        senf_info("Changing to... {}".format(COURSE))

@cli.command()
@click.argument("course", type=click.STRING)
def mklecture(course):
    if os.path.exists(SEMESTER + course):
        # TODO error warning
        click_error("This lecture already exists.")
        return

    COURSE_ABS_PATH = SEMESTER + course + "/"    
    os.mkdir(COURSE_ABS_PATH)

    for directory in COURSE_DIR_STRUCTURE:
        os.mkdir(COURSE_ABS_PATH + directory + "/")        

    for l_file in COURSE_FILES:
            touch_file(COURSE_ABS_PATH + l_file)

@cli.command()
def workon():
    senf_info("Please use the provided senf-workon bash script for this action")
