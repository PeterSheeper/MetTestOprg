#!/usr/bin/env python3

import sys

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    printLength = False
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                print(param.swapcase(),end="")
                shouldDo=False
            elif format_string[idx] == '#' and format_string[idx+1] == '.':
                idy = idx+2
                number = 0
                while isnumeric(format_string[idy]):
                    number = number * 10
                    number += format_string[idy]
                number = int(format_string[idx+2])
                shouldDo=False
                printLength = True
            else:
                print(format_string[idx].swapcase(),end="")
        else:
            if not printLength:
                shouldDo=True
            
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
