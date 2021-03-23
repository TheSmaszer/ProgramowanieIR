import matplotlib.pyplot as plt
import numpy as np

def frange(a,b,step):
    lst = []
    b = float(b)
    a = float(a)
    step = float(step)
    while a < b:
        lst.append(a)
        a = a + step
    return lst
# print(frange(1,5,0.2)
def plotf(func, a, b,title=""):
    x = frange(a,b,0.01)
    plt.plot(x,func(x))
    plt.xlabel("Wartości $x$")
    plt.ylabel("Wartości funkcji")
    plt.title(title)
    plt.grid()
    plt.show()

def plotsin(a,b):
    def f(k):
        return np.multiply(k,np.sin(k)) - np.multiply(k,k)
    plotf(f,a,b,title = "Wykres $f \, (x) = x \: \sin x - x^2$")

# a = input("Podaj lewy przedział: ")
# b = input("Podaj prawy przedział: ")
# plotsin(a,b)

plotsin(-10,10)