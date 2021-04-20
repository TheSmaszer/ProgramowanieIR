import sys

args = sys.argv[1:]

if(args[0] == "r"):
    # print([int(args[1][i]) for i in range(len(args[1]))]) 
    var = int(args[1])
    result = ""
    i = True
    while i:
        if(var>=1000):
            var = var-1000
            result = result + "M"
        elif(900<=var and var<=999):
            var = var-900
            result = result + "CM"
        elif(var>=500):
            var = var-500
            result = result + "D"
        elif(400<=var and var<=499):
            var = var -400
            result = result + "CD"
        elif(var>=100):
            var = var-100
            result = result + "C"
        elif(90<=var and var<=99):
            var = var - 90
            result = result + "XC"
        elif(var>=50):
            var = var-50
            result = result + "L"
        elif(40<=var and var<=49):
            var = var -40
            result = result + "XL"
        elif(var>=10):
            var = var-10
            result = result + "X"
        elif(var==9):
            var = var -9
            result = result + "IX"
        elif(var>=5):
            var = var-5
            result = result + "V"
        elif(var==4):
            var = var -4
            result = result + "IV"
        elif(var>=1):
            var = var-1
            result = result + "I"
        else:
            i=False
        
        
    print(result)
elif(args[0] == "a"):
    var = args[1]
    varlist=[]
    for char in var:
        if(char == "I"):
            varlist.append(1)
        if(char == "V"):
            varlist.append(5)
        if(char == "X"):
            varlist.append(10)
        if(char == "L"):
            varlist.append(50)
        if(char == "C"):
            varlist.append(100)
        if(char == "D"):
            varlist.append(500)
        if(char == "M"):
            varlist.append(1000)
    total = 0
    for i in range(0,len(varlist)-1):
        if(varlist[i]>=varlist[i+1]):
            total = total + varlist[i]
        else:
            total = total - varlist[i]
    total = total + varlist[-1]
    print(total)