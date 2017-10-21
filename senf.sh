#! /bin/bash
# created by leschtz

SEMESTER="$HOME/university/00-bachelor-computer-science/05-semester/"
export SEMESTER

senf-check-course ()
{
  if [[ -z ${COURSE+x} ]]
  then
    exit -1
  fi
}
#senf-main()
senf-init ()
{
  read -p "Do you really want to create a course called $1? " -n 1 -r

  if [[ $REPLY =~ ^[Yy]$ ]]
  then
    pushd $SEMESTER
    mkdir -p $1/{presentation,exam-preparation,books,practicals}
    touch $1/links
    touch $1/.studyrc
    popd
    printf "Succesfully created '$1' in '$SEMESTER'\n"
  else
    printf "\nAborted.\n"
  fi

}

senf-workon ()
{
  if [[ ! "$#" -eq 1 ]]; then
    exit 3
  fi

  COURSE=$(find $SEMESTER -maxdepth 1 -name $1 -type d -print -quit)
  if [[ -z $COURSE ]]; then
          printf "There is no course %s for this semester!\n" "$1"
  else
          source "$COURSE/.studyrc"
  fi
}

senf-deactivate ()
{
  echo "deactivate"
        unset COURSE
}

senf-move ()
{
  senf-check-course
  if [[ ! -d "$COURSE/$1" ]]
  then
    printf "There is no directory %s for your course %s.\n" "$1" "$(basename $COURSE)"
    exit 2
  fi

  directory="$COURSE/$1"

  mv "$@" "$directory"
}

senf-cd ()
{
  senf-check-course
  echo "$@ $#"
  if [[ "$#" -eq 0 ]]
  then
    printf "Moving to std: %s...\n" "$COURSE"
    cd "$COURSE"
  elif [[ -d "$($COURSE/$1)" ]]
  then
    printf "Moving to %s/%s...\n" "$COURSE" "$1"
    cd "$COURSE/$1"
  else
    printf "Not a valid destination...\n"
    exit 3
  fi
}


################################################################################
######## MAIN
################################################################################

case "$1" in
  "init")
    senf-init $2
    ;;
  "workon")
    senf-workon $2
    ;;
  "deactivate")
    senf-deactivate
    ;;
  "mv")
    senf-move "${@:2}"
    ;;
  "cd")
    senf-cd "${@:2}"
    ;;
  *)
    printf "%s is not a valid command\n" "$1"
    exit 1
    ;;
esac
