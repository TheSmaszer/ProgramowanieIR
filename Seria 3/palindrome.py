import sys

def isPalindrome(str):
    import string
    str = str.translate(str.maketrans('', '', string.punctuation + " ")).lower()
    if(str == str[::-1]):
        return True
    else:
        return False

i = False
for arg in sys.argv[1:]:
    if(arg=="/all" or arg=="/a" or arg=="-a" or arg=="--all"):
        i = True 

if(i==True):
    print("Argument | isPalindrome")
    for arg in sys.argv[1:]:
        if(arg=="/all" or arg=="/a" or arg=="-a" or arg=="--all"):
            pass
        else:
            print(arg," | ",isPalindrome(arg))
else:
    for arg in sys.argv[1:]:
        if(isPalindrome(arg)==True):
            print(arg)