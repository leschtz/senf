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

senf-init [course-name]
senf-workon [course-name]
senf-list
senf-deactivate

senf-mv [course-directory] [file1] [...] [fileN]
senf-zip [course-directory]
senf-send [application] [course-directory]
```
