#!/usr/bin/python3

import os
import re

with open("3_1.dat") as f:
    slope=[3,1] # right,down
    place=[0,0] # starting point, top left corner
    trees = 0
    lines = f.readlines()
    lines[:] = [x.rstrip() for x in lines if x]
    height = len(lines)
    width = len(lines[0])
    while place[1]<height:
        if lines[place[1]][place[0]] != ".":
            trees+=1
        place[0]=(place[0]+slope[0])%width
        place[1]+=slope[1]
    print(trees,"trees found on the 3,1 slope")

    slopes=[[1,1],[5,1],[7,1],[1,2]]
    for slope in slopes:
        new_trees = 0
        place = [0,0]
        while place[1] < height:
            if lines[place[1]][place[0]] != ".":
                new_trees+=1
            place[0]=(place[0]+slope[0])%width
            place[1]+=slope[1]
        print(new_trees,"new trees found on the slope",slope[0],slope[1])
        trees = trees*new_trees

print(trees,"total product of trees")
