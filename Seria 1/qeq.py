import cmath as cm
a = float(input("Podaj parametr a równania postaci ax^2+bx+c=0: "))
b = float(input("Podaj parametr b równania postaci ax^2+bx+c=0: "))
c = float(input("Podaj parametr c równania postaci ax^2+bx+c=0: "))

delta = b**2 - 4*a*c
if(a!=0):
    if not delta:
        x = -b/2*a
        print(f"x = {x}")
    else:
        x1 = (-b+cm.sqrt(delta))/2*a
        x2 = (-b-cm.sqrt(delta))/2*a
        print("x1 = {0}\nx2 = {1}".format(x1,x2))
else:
    x = -c/b
    print(f"x = {x}")
