#!/usr/bin/python3

import os
import re

with open("2_1.dat") as f:
    valid = 0
    new_valid = 0
    total =0
    while True:
        line = f.readline()
        if not line:
            break
        total +=1
        line=line.rstrip() # remove newline
        line = re.split('[: ]',line) # split the data
        line[:] = [x for x in line if x] # remove blankes
        policy = re.split('-',line[0])
        min = int(policy[0])
        max = int(policy[1])
        letter = line[1]
        password = line[2]
        if password.count(letter) <= max and password.count(letter) >= min :
            valid+=1

        # part 2
        min-=1
        max-=1
        if len(password) < max:
            if password[min] == letter:
                new_valid +=1
        elif password[min] == letter and not password[max] == letter:
            new_valid+=1
        elif password[max] == letter and not password[min] == letter:
            new_valid+=1
        else:
            ""
print("There are",valid,"valid passwords within the ",total,"total passwords in the database")
print("The new policy identify",new_valid,"valid password")
