#!/usr/bin/python3

import os
import re

#luggage_list ={ bag_type : {"quantity" : [], "bag_type" :[]}}

luggage_list = {}

with open("7_1.dat") as file:
    f = file.readlines()
    for line in f:
        line.rstrip()
        line = line.split(" bags contain");
        luggage_list[line[0]] = {"quantity" : [], "bag_type" : []}
        inside_bags = line[1].split(',')
        for entry in inside_bags:
            e = entry.split()
            luggage_list[line[0]]['quantity'].append(e[0])
            luggage_list[line[0]]["bag_type"].append(e[1] + " " + e[2])

#print(luggage_list)
total=0
accepted_colors = {"shiny gold" : 1}
#for bag in luggage_list:
#    if "shiny gold" in luggage_list[bag]["bag_type"]:
#        accepted_colors[bag] = 1
#        total+=1

full_colors = {}


while True:
    full_colors = accepted_colors.copy()
    for bag in luggage_list:
        for color in full_colors.copy():
            if color in luggage_list[bag]["bag_type"]:
                if bag in accepted_colors.keys():
                    accepted_colors[bag] +=1
                else:
                    accepted_colors[bag] =1
                    total+=1
    if full_colors.keys() == accepted_colors.keys():
        break;


print(total,"acceptable colors found")

print(full_colors.values())
