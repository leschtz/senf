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

SEMESTER = None

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
    global SEMESTER
    if os.environ['TEST']:
        # print("THIS IS A TEST ENVIRONMENT!!!")
        SEMESTER = os.path.expanduser(os.getcwd() + "/test/")
        # print(SEMESTER)
    else:
        semester_tmp = os.environ['SEMESTER']
        if semester_tmp:
            SEMESTER = os.path.expanduser(semester_tmp)
        else:
            # TODO implement warning here
            senf_error("THIS IS NOT WORKING")


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
@click.argument("course", type=click.STRING, autocompletion=get_course)
def cd(course):
    senf_error("THIS FUNCTION IS NOT YET IMPLEMENTED")

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
