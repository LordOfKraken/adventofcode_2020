#!/usr/bin/python3

import os
import re

with open("passwords.dat") as f:
    valid = 0
    total =0
    while True:
        line = f.readline()
        if not line:
            break
        total +=1
        print(line)
        line=line.rstrip()
        policy = re.split('[: ]',line)
        policy[:] = [x for x in policy if x]
        print(policy)
        #print("Line {}: {}".format(total, pwd.strip()))
