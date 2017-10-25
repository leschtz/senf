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
          printf "WORKON: '%s'\n" "$COURSE"
          source senf-helper
          source "$COURSE/.studyrc"
  fi
}

senf-list ()
{
  LIST=$(ls -l $SEMESTER | egrep '^d' | awk '{print $9}')
  for DIR in $LIST
  do
    if [[ -z ${COURSE+x} ]]
    then
      echo -e "$DIR"
      continue
    fi

    if [[ "$(basename $COURSE)" != "$DIR" ]]
    then
      echo -e "$DIR"
    else
      echo -e "\033[0;34m* $DIR\033[0m"
    fi
  done

  unset LIST
}

senf-deactivate ()
{
  unset COURSE
  unset -f senf-mv senf-cd senf-check-course
}
