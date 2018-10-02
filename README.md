# senf - study environment
senf offers some handy bash and python functions for students.

## How does it work?
senf sets various environment variables, eg. `$COURSE`, when you start your study environment. This variable offers you easier access to your course hierarchy.

## Features
0. most importantly: auto-completion
1. move files easily to your target course
2. every course has a properly defined hierarchy
3. set course specific aliases or functions with the `.studyrc` file
4. zip course-specific folders with one command
5. send course-data with your favourite application

## Example
A simple example would be moving course related content to your course folder hierarchy.
```
# workon an existing course
senf-workon [course]

# create a lecture
senf mklecture [course]

# leave your student environment
senf-deactivate
```

## Usage
```bash
senf-workon [course]
senf-deactivate

senf-set-study [study]
senf-set-semester [semester]
```

```python
senf mklecture [course]
```
## Structure
`senf mklecture [course]` creates a new course, by setting up the according directory structure. The structure is as follows:

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
- `links` is a normal textfile, containing links to relevant websites. It is planned, to utilize the content for some scripts. [MORE TO FOLLOW]
- `books/` is a directory, for relevant papers, books, etc..
- `exam-preparation` is a directory, for exam relevant information, like old exams, your own 'exam preparation' notes, question catalogues and anything else, closely related to the exam.
- `practicals`, is a directory, for homework, laboratory stuff, vcs stuff, etc.. This can either be the repository itself or contain the repository as a sub-directory.
- `presentation`, is a directory, for the lectures stuff.
