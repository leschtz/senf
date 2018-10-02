import click
import shutil
import os

LECTURE_DIRECTORIES = [
                "books",
                "practicals",
                "exam-preparation",
                "lecture"
                ]

LECTURE_FILES = [
                "links",
                ".studyrc"
                ]

SEMESTER = None

def get_env_vars(ctx, args, incomplete):
        return [k for k in os.environ.keys() if incomplete in k]

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
            click.echo("THIS IS NOT WORKING")

def touch_file(filename):
    with open(filename, 'a'):
        os.utime(filename, None)

def get_lecture(ctx, args, incomplete):
    init_lecture()
    return [k for k in os.listdir(SEMESTER) if incomplete in k]

@click.group()
def cli():
    init_lecture()

@cli.command()
@click.argument('directory', type=click.STRING, autocompletion=get_lecture)
def cd(directory):
    click.echo("not yet implemented")

@cli.command()
@click.argument('lecture_name', type=click.STRING)
def mklecture(lecture_name):
    if os.path.exists(SEMESTER + lecture_name):
        # TODO error warning
        click.echo("this dir already exists")
        return

    LECTURE_ABS_PATH = SEMESTER + lecture_name + "/"    
    os.mkdir(LECTURE_ABS_PATH)

    for directory in LECTURE_DIRECTORIES:
        os.mkdir(LECTURE_ABS_PATH + directory + "/")        

    for l_file in LECTURE_FILES:
            touch_file(LECTURE_ABS_PATH + l_file)

