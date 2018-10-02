#! /bin/bash
# created by leschtz

senf-workon() {
  COURSE=$(find "$SEMESTER" -maxdepth 1 -name "$1" -type d -print -quit)
  if [[ -z $COURSE ]]; then
          printf 'There is no course %s for this semester!\n' "$1"
  else
          printf 'WORKON: '%s'\n' "$COURSE"
          source "$COURSE"/.studyrc
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
