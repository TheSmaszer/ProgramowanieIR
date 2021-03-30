a = float(input("Podaj parametr a równania postaci ax+b=0: "))
b = float(input("Podaj parametr b równania postaci ax+b=0: "))
if(a!=0):
    x=-b/a
    print("x = {0}".format(x))
else:
    print("Brak rozwiązań")
