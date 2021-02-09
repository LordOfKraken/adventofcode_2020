#!/usr/bin/python3

import os
import re

with open("6_1.dat") as file:
    f = file.readlines()
    record = []
    yes_total = 0
    groups = 0

    for line in f:
        if line == '\n':
            groups+=1
            yes_total += len(record)
            #print("\nGroup ",groups," : ", len(record),"(",yes_total,")")
            #print(record)
            record = []
        else:
            line=line.rstrip()
            for a in line:
                if not a in record:
                    record.append(a)
    # flush last line
    groups+=1
    yes_total += len(record)
    #print("\nGroup ",groups," : ", len(record),"(",yes_total,")")
    #print(record)
    print("Groups analyzed: ",groups)
    print("Total affirmative answers :", yes_total)
    del record



    # ****** Part 2 ****** #

    record = []
    groups = 0
    people = 0
    yes_total = 0
    for line in f:
        if line == '\n':
            groups+=1
            people = 0
            yes_total += len(record)
            print("Group ",groups," : ", len(record),"(",yes_total,")")
            print(record,"\n")
            record = []
        else:
            line=line.rstrip()
            print(line)
            if people == 0:
                record = [ a for a in line if a not in record]
            else:
                record = [r for r in record if r in line]
            people +=1

    # flush last line
    groups+=1
    people=0
    yes_total += len(record)
    print("Group ",groups," : ", len(record),"(",yes_total,")")
    print(record,"\n")
    record = []

    print("Total affirmative answers :", yes_total)
