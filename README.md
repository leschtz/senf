# senf - study environment
senf offers some handy bash functions for students.

## How does it work?
senf sets an environment variable `$COURSE`, when you start your study environment. This variable offers you easier access to your course hierarchy.

## Features
1. move files easily to your target course
2. every course has a properly defined hierarchy
3. set course specific aliases or functions with the `.studyrc` file
4. zip course-specific folders with one command
5. send course-data with your favourite application

## Example
A simple example would be moving course related content to your course folder hierarchy.
```bash
# create a new course
senf-init soma

# course is called soma
senf-workon soma

# cd into your local downloads location
cd ~/Downloads

# move the previously downloaded presentation slide to your presentation folder
senf-mv presentation soma-presentation-01.pdf

# leave your student environment
senf-deactivate
```

## Usage (planned)
```
senf-[command] [parameters]

# all-time working functions
senf-init [course-name]
senf-workon [course-name]
senf-list
senf-deactivate

# working while in an environment
senf-mv [course-directory] [file1] [...] [fileN]
senf-zip [course-directory]
senf-send [application] [course-directory]
```

## Structure
`senf-init [course-name]` creates a new course, by setting up the according directory structure. The structure is as follows:

```
[course-name]/
    links
    books/
    exam-preparation/
    practicals/
    presentation/
```
You can change this accordingly, by changing the the hard-coded values in the script.

### Structure Definition
* `links` is a normal textfile, containing links to relevant websites. It is planned, to utilize the content for some scripts. [MORE TO FOLLOW]

* `books/` is a directory, for relevant papers, books, etc..

* `exam-preparation` is a directory, for exam relevant information, like old exams, your own 'exam preparation' notes, question catalogues and anything else, closely related to the exam.

* `practicals`, is a directory, for homework, laboratory stuff, vcs stuff, etc.. This can either be the repository itself or contain the repository as a sub-directory.

* `presentation`, is a directory, for the lectures stuff.
