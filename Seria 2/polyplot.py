import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

def poly(x,n):
    i=1
    polynomial = 3
    while i <= n:
        polynomial = polynomial * (x-i) 
        i=i+1
    return polynomial

x = np.arange(1,5.5,0.05)
plt.plot(x,[poly(x0,1) for x0 in x],label = "y = 3(x-1)")
plt.plot(x,[poly(x0,2) for x0 in x],label = "y = 3(x-1)(x-2)")
plt.plot(x,[poly(x0,3) for x0 in x],label = "y = 3(x-1)(x-2)(x-3)")
plt.plot(x,[poly(x0,4) for x0 in x],label = "y = 3(x-1)(x-2)(x-3)(x-4)")
plt.plot(x,[poly(x0,5) for x0 in x],label = "y = 3(x-1)(x-2)(x-3)(x-4)(x-5)")
plt.legend()
plt.title("Wykresy funkcji wielomianowych")
plt.xlabel("Argumenty")
plt.ylabel("Wartości funkcji")
plt.grid()
plt.show()


with PdfPages('polyplot.pdf') as pdf:
    size = (5,5)
    plt.figure(figsize = size)
    plt.plot(x,[poly(x0,1) for x0 in x])
    plt.title("Wykres y = 3(x-1)")
    plt.xlabel("Argumenty")
    plt.ylabel("Wartości funkcji")
    plt.grid()
    pdf.savefig()
    plt.close()

    plt.figure(figsize = size)
    plt.plot(x,[poly(x0,2) for x0 in x])
    plt.title("Wykres y = 3(x-1)(x-2)")
    plt.xlabel("Argumenty")
    plt.ylabel("Wartości funkcji")
    plt.grid()
    pdf.savefig()
    plt.close()

    plt.figure(figsize = size)
    plt.plot(x,[poly(x0,3) for x0 in x])
    plt.title("Wykres y = 3(x-1)(x-2)(x-3)")
    plt.xlabel("Argumenty")
    plt.ylabel("Wartości funkcji")
    plt.grid()
    pdf.savefig()
    plt.close()

    plt.figure(figsize = size)
    plt.plot(x,[poly(x0,4) for x0 in x])
    plt.title("Wykres y = 3(x-1)(x-2)(x-3)(x-4)")
    plt.xlabel("Argumenty")
    plt.ylabel("Wartości funkcji")
    plt.grid()
    pdf.savefig()
    plt.close()

    plt.figure(figsize = size)
    plt.plot(x,[poly(x0,5) for x0 in x])
    plt.title("Wykres y = 3(x-1)(x-2)(x-3)(x-4)(x-5)")
    plt.xlabel("Argumenty")
    plt.ylabel("Wartości funkcji")
    plt.grid()
    pdf.savefig()
    plt.close()