#!/usr/bin/env bash
#adds two numbers
if [ "$#" -eq 0 ]
then
#-- echo $# shows n of args
    echo "Usage: filename\tnum1\tnum2"
else
    sum=$(($1+$2))
    echo $sum
    echo "Exit status:\"$?\""
fi
