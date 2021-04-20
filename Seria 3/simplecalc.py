import sys
import numpy as np
args = sys.argv[1:]

i = False
for arg in args:
    if(arg=="/e" or arg=="/expression" or arg=="-e" or arg=="--expression"):
        i = True
        args.remove(arg)

if(args[0] == "/a" or args[0] == "/add" or args[0] == "-a" or args[0] == "--add"):
    sum = 0
    for arg in args[1:]:
        sum = sum + float(arg)
    
    if(i):
        print(" + ".join(args[1:]) + " = " + str(sum))
    else:
        print(sum)

elif(args[0] == "/m" or args[0] == "/mul" or args[0] == "-m" or args[0] == "--mul"):
    prod = 1
    for arg in args[1:]:
        prod = prod * float(arg)

    if(i):
        print(" * ".join(args[1:]) + " = " + str(prod))
    else:
        print(prod)

elif(args[0] == "/?" or args[0] == "-h" or args[0] == "--help" or True):
    print("""Syntax: simplecalc.py [args] numbers [/e or /expression or -e or --expression]
    /e or /expression or -e or --expression returns operation with result
    Correct [args]:
        /a or /add or -a or --add for addition 
        /m or /mul or -m or --mul for multiplication
        /? or -h or --help for help
    """)
