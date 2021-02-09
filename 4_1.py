#!/usr/bin/python3

import os
import re

sample = {
    "byr":"",
    "iyr":"",
    "eyr":"",
    "hgt":"",
    "hcl":"",
    "ecl":"",
    "pid":"",
    "cid":""
    }
keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
opt_keys = ["cid"]

ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

total = 0
valid = 0


with open("4_1.dat") as f:
    record = {}
    for line in f:
        if line == '\n':
            total+=1
            check=0
            # check all the needed keys
            if set(keys).issubset(record.keys()):
                # validate all the keys
                if  int(record['byr']) >= 1920 and int(record['byr']) <= 2002 and \
                    int(record['iyr']) >= 2010 and int(record['iyr']) <= 2020 and \
                    int(record['eyr']) >= 2020 and int(record['eyr']) <= 2030 and \
                    record['ecl'] in ecl:
                    check +=4
                    print("passed ages and eye color checks")

                h=re.split('(\D+)',record['hgt'])
                h[:] = [x for x in h if x]
                if len(h)==2 and re.findall('\d+',h[0])[0]==h[0]:
                    if h[1] == 'cm' and int(h[0]) >= 150 and int(h[0]) <= 193:
                        print('height check passed, cm')
                        check+=1
                    elif h[1] == 'in' and int (h[0]) >= 59 and int(h[0]) <= 76:
                        print('height check passed, in')
                        check+=1
                    else:
                        pass

                if len(re.findall('\d+',record['pid'])[0]) == 9:
                    print("pid check passed")
                    check+=1

                if re.findall('#*\w+',record['hcl']) and len(re.findall('#*\w+',record['hcl'])[0]) == 7:
                    print("hair color check passed")
                    check+=1

                if check==7:
                    valid+=1
                    print("valid",check)
                else:

                    print("not valid, wrong field entry",check)
            else:
                print("not valid, fields missing")
            # reset the record
            print(record)
            print("record ending\n")
            record = {}
        else:
            line=line.rstrip()
            # split the line and fill the record
            entries = re.split(' ',line)
            for e in entries:
                k,v=re.split(':',e)
                record[k]=v


print(valid,"valid passports within ",total," given entries")
