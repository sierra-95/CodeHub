#!/usr/bin/env python3
#executes .py files
if [ $1 ]
then
    if [ -f $1 ] && [ -s $1 ]
    then
    echo "Executing ...\n"
    python3 $1
    elif [ -d $1 ]
    then
    echo "Can't execute directories"
    else
    echo "File passed doesn't exist or is empty"
    fi    
else
echo "Please pass a valid *.py file"
fi