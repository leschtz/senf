#! /bin/bash
# created by leschtz

UNIVERSITY_DIR=$HOME/university
STUDY=$UNIVERSITY_DIR/01-master-computer-engineering
SEMESTER=$STUDY/01-semester

export UNIVERSITY_DIR
export STUDY
export SEMESTER

senf-cd() {
    pushd $COURSE
    }

senf-set-study() { 
    STUDY=$(find "$UNIVERSITY_DIR" -maxdepth 1 -name "$1" -type d -print -quit) 
    export STUDY
}


function _study_autocom(){
        local cur
        COMPREPLY=()
        cur=${COMP_WORDS[COMP_CWORD]}
        COMPREPLY=($(compgen -W "$(ls $UNIVERSITY_DIR)" -- $cur ))
}
complete -F _study_autocom senf-set-study


senf-set-semester() {
    SEMESTER=$(find "$STUDY" -maxdepth 1 -name "$1" -type d -print -quit)
    export SEMESTER
}

function _semester_autocom(){
        local cur
        COMPREPLY=()
        cur=${COMP_WORDS[COMP_CWORD]}
        COMPREPLY=($(compgen -W "$(ls $STUDY)" -- $cur ))
}
complete -F _semester_autocom senf-set-semester

senf-workon() {
    COURSE=$(find "$SEMESTER" -maxdepth 1 -name "$1" -type d -print -quit)
    if [[ -z $COURSE ]]; then
        printf 'There is no course %s for this semester!\n' "$1"
    else
        printf 'WORKON: '%s'\n' "$COURSE"
        source "$COURSE"/.studyrc
        export COURSE
    fi
}

senf-deactivate() {
    unset COURSE
}

function _courses_autocom(){
        local cur
        COMPREPLY=()
        cur=${COMP_WORDS[COMP_CWORD]}
        COMPREPLY=($(compgen -W "$(ls $SEMESTER)" -- $cur ))
}
complete -F _courses_autocom senf-workon


eval "$(_SENF_COMPLETE=source senf)"
