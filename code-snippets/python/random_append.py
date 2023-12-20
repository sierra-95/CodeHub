#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
my_list=[]
for i in range(1,6):
    my_list.append(random.randint(0,10))

#sort using 
sorted(my_list)
my_list.sort(reverse=False)