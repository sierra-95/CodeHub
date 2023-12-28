#!/usr/bin/env bash
#prints 00-100 
for i in {0..100}
do
    echo $((i/10))$((i%10))
done