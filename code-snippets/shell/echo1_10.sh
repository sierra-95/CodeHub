#!/usr/bin/env bash
#prints 1-10
#execute ./
i=1
while [ $i -le 10 ]
do
echo "Number=$i"
    if [ $i -eq 9 ]
    then
        echo "Almost done"
    fi    
((i++))
done    