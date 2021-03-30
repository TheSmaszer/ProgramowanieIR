import matplotlib.pyplot as plt
import numpy as np
def gfrange(a,b,d):
    list = []
    while a<b:
        list.append(a)
        a = a + d
    return list

x = gfrange(-0.5,0.5,0.01)

plt.title("Wykresy funkcji $y = x, sin(x)$ oraz $tg(x)$")
plt.plot(x,x, label="y = x")
plt.plot(x,np.sin(x),label="y = sin(x)")
plt.plot(x,np.tan(x),label="y = tg(x)")
plt.grid()
plt.xlabel("Argumenty funkcji")
plt.ylabel("Wartości funkcji $y = \sin(x)$")
plt.ylim([-1,1])
plt.legend()

ext = input("W jakim rozszerzeniu mam zapisać wykres?(png,jpg,svg,pdf):")
if ext == "png" or ext == "jpg" or ext == "svg" or ext == "pdf":
    plt.savefig("trigplot." + ext)
    print("Udało się")
else:
    print("Złe rozszerzenie - nie zapisano pliku")

plt.show()