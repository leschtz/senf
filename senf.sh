#! /bin/bash
# created by leschtz

### IS IT ALLOWED TO USE set -e IN PRODUCTION?
#set -e

SEMESTER="$HOME/university/00-bachelor-computer-science/05-semester/"
export SEMESTER

## commented out as it is unknown to me if "set -e" is allowed
#senf-check-course ()
#{
#  if [[ -z ${COURSE+x} ]]
#  then
  #    exit -1
#  fi
#}

senf-init ()
{
  read -p "Do you really want to create a course called $1? " -n 1 -r

  if [[ $REPLY =~ ^[Yy]$ ]]
  then
    pushd "$SEMESTER"
    mkdir -p "$1"/{presentation,exam-preparation,books,practicals}
    touch "$1"/links
    touch "$1"/.studyrc
    popd
    printf '\nSuccesfully created '%s' in '%s'\n' "$1" "$SEMESTER"
  else
    printf '\nAborted.\n'
  fi

}

senf-workon ()
{
#  if [[ ! "$#" -eq 1 ]]; then
#    return 3
#  fi
  COURSE=$(find "$SEMESTER" -maxdepth 1 -name "$1" -type d -print -quit)
  if [[ -z $COURSE ]]; then
          printf 'There is no course %s for this semester!\n' "$1"
  else
          printf 'WORKON: '%s'\n' "$COURSE"

          # ignored by shellcheck
          # shellcheck source=/dev/null
          source helper/senf-helper
          # shellcheck source=/dev/null
          source "$COURSE"/.studyrc
  fi
}


senf-list ()
{
  list=$(ls  $SEMESTER)
  for dir in $list
  do
    if [[ -z ${COURSE+x} ]]
    then
      echo -e "$dir"
      continue
    fi

    if [[ $(basename "$COURSE") != "$dir" ]]
    then
      echo -e "$dir"
    else
      echo -e "\033[0;34m* $dir\033[0m"
    fi
  done

  unset list
}

senf-deactivate ()
{
  unset COURSE
  unset -f senf-mv senf-cd #senf-check-course
}

function _courses_autocom()
{
        local cur
        COMPREPLY=()
        cur=${COMP_WORDS[COMP_CWORD]}
        COMPREPLY=($(compgen -W "$(ls $SEMESTER)" -- $cur ))
}
complete -F _courses_autocom senf-workon
