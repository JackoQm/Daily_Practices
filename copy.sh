#!/bin/bash
SOURCE=~/Developer/OJ/
DEST=~/Developer/Daily_Practices/
FILE=main.py
if [ $# -eq 2 ]
then 
  case $1 in
  "-w")
    cp ${SOURCE}/${FILE} ${DEST}/LeetCode/WA/$2.py
  ;;
  "-u")
    cp ${SOURCE}/${FILE} ${DEST}/LeetCode/Unsolved/$2.py
  ;;
  "-t")
    cp ${SOURCE}/${FILE} ${DEST}/LeetCode/TLE/$2.py
  ;;
  *)
    echo "Failed! \"$1\" not found!"
  ;;
  esac
else
  cp ${SOURCE}/${FILE} ${DEST}/LeetCode/AC/$1.py
fi

