import sys
args = sys.argv[1:]

if(args[0]=="check"):
    brackets = str(args[1])
    i=0
    for char in brackets:
        if(char=="("):
            i += 1
        if(char==")"):
            i -= 1
    print(i)
if(args[0]=="fix"):
    pass
if(args[0]=="list"):
    pass
