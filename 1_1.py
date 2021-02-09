#!/usr/bin/python3

import os

with open("expenses_report.dat") as report:
    expenses = report.readlines()

    e=0
    s=0
    for exp in expenses:
        e+=1
        s=0

        for sum in expenses:
            s+=1
            if int(exp) + int(sum) ==2020:
                n1=str(exp.rstrip('\n'))
                n2=str(sum.rstrip('\n'))
                l1=str(e)
                l2=str(s)

    print("The two numbers that add to 2020 are " + n1 + " on line " + l1 + " and " + n2  + " on line " + l2 + "\n")
    print("They multiply to " + str(int(n1)*int(n2)) + '\n')
report.close()

#The two numbers that add to 2020 are 1939 on line 123 and 81 on line 36
#They multiply to 157059

# PART 2

with open("expenses_report.dat") as report:
    expenses = report.readlines()

    a=0
    b=0
    c=0
    for exp in expenses:
        a+=1
        b=0

        for sum in expenses:
            b+=1
            c=0
            for third in expenses:
                c+=1
                if int(exp) + int(sum)  + int(third)== 2020:
                    n1=str(exp.rstrip('\n'))
                    n2=str(sum.rstrip('\n'))
                    n3=str(third.rstrip('\n'))
                    l1=str(a)
                    l2=str(b)
                    l3=str(c)

    print("\nPART 2\n")
    print("The three numbers that add to 2020 are " + n1 + ", " + n2 + " and " + n3)
    print("on line " + l1 + ", " +  l2  + " and " + l3 + "\n")
    print("They multiply to " + str(int(n1)*int(n2)*int(n3) ))
report.close()

#The three numbers that add to 2020 are 1310, 358 and 352 on line 127, 115 and 94
#They multiply to 165080960 
