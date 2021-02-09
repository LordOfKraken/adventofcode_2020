#!/usr/bin/python3

import os
import re

with open("5_1.dat") as f:
    ids =[]
    lines = f.readlines()
    lines[:] = [x.rstrip() for x in lines if x]
    MAX_ROW = 127
    MAX_COL = 7
    max_id = 0

    for line in lines:
        urow = MAX_ROW
        ucol = MAX_COL
        lrow = 0
        lcol = 0
        rows_range = [r for r in range(0,128)]
        cols_range = [c for c in range(0,8)]
        for rule in line:
            if len(rows_range) == 1:
                if rule == "L":
                    ucol -= (ucol-lcol)*0.5
                    cols_range=[c for c in cols_range if c < ucol]
                if rule == "R":
                    lcol += (ucol-lcol)*0.5
                    cols_range=[c for c in cols_range if c > lcol]
            else:
                if rule == "F":
                    urow -= (urow-lrow)*0.5
                    rows_range=[r for r in rows_range if r < urow]
                elif rule == "B":
                    lrow += (urow-lrow)*0.5
                    rows_range=[r for r in rows_range if r > lrow]
                else:
                    print("Unrecognized rule")

        if len(cols_range)==1:
            col = ucol-1
            row = urow-1
            seat_id = 8*rows_range[0] + cols_range[0];
            ids.append(seat_id)
            print("Seat ",rows_range[0],"-",cols_range[0]," ID: ",seat_id,sep="")
            if seat_id > max_id:
                max_id = seat_id;

    print("Max seat id",max_id)
    for id in range(0,max_id):
        if not id in ids and id+1 in ids and id-1 in ids:
            print("My seat id",id)
