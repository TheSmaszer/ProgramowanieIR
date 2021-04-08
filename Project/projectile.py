import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np 

v0 = 2
alpha = np.pi/4
# mass = int(input("Podaj masę: "))
mass = 1
offset = 1
beta = 10
g = 9.81

height = (beta*offset - mass*np.log(1/np.sqrt(1 + (beta * v0**2 * np.sin(alpha)*2)/(g*mass))))/beta
period = (np.sqrt(mass)*(np.arccosh(np.e**((beta*offset - mass*np.log(1/np.sqrt(1 + (beta*v0**2*np.sin(alpha)**2)/(g*mass))))/mass)) + np.arctan((np.sqrt(beta)*v0*np.sin(alpha))/(np.sqrt(g)*np.sqrt(mass)))))/(np.sqrt(beta)*np.sqrt(g))
distance = -((mass*np.log(mass))/beta) + (mass*np.log(mass + beta*period*v0*np.cos(alpha)))/beta

fig = plt.figure()
ax1 = plt.axes(xlim=(0-0.05*distance, 1.1*distance), ylim=(0-0.05*height,1.1*height))
line, = ax1.plot([], [])
plt.xlabel('Distance [m]')
plt.ylabel('Height [m]')
plt.grid()

lines = []
lob1 = ax1.plot([],[], "b",label="Flight path")[0]
# lob1.text("1")
lines.append(lob1)
lob2 = ax1.plot([],[],"*")[0]
lines.append(lob2)
plt.legend()


def init():
    for line in lines:
        line.set_data([],[])
    return lines

x1,y1 = [],[]
x2,y2 = [],[]

def animate(i):

    x = -((mass*np.log(mass))/beta) + (mass*np.log(mass + beta*i*v0*np.cos(alpha)))/beta
    if (i <= (np.sqrt(mass)*np.arctan((np.sqrt(beta)*v0*np.sin(alpha))/(np.sqrt(g)*np.sqrt(mass))))/(np.sqrt(beta)*np.sqrt(g))):
        y = (mass*np.log(np.cos((np.sqrt(beta)*np.sqrt(g)*i)/np.sqrt(mass) - np.arctan((np.sqrt(beta)*v0*np.sin(alpha))/(np.sqrt(g)*np.sqrt(mass))))))/beta + (beta*offset - mass*np.log(1/np.sqrt(1 + (beta*v0**2*np.sin(alpha)**2)/(g*mass))))/beta
    else:
        y = -((mass*np.log(np.cosh((np.sqrt(beta)*np.sqrt(g)*i)/np.sqrt(mass) - np.arctan((np.sqrt(beta)*v0*np.sin(alpha))/(np.sqrt(g)*np.sqrt(mass))))))/beta) + (beta*offset - mass*np.log(1/np.sqrt(1 + (beta*v0**2*np.sin(alpha)**2)/(g*mass))))/beta
    x1.append(x)
    y1.append(y)

    xlist = [x1, x]
    ylist = [y1, y]

    ax1.text(0, 0, f'Time is {round(i*5,2)}',fontsize="9",bbox={'facecolor': 'white', 'alpha': 0.8, 'pad': 2})

    for lnum,line in enumerate(lines):
        line.set_data(xlist[lnum], ylist[lnum]) # set data for each line separately.
    return lines

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=np.linspace(0, period,100), interval=5,repeat=False)
# loc, ticks = ax1.get_xticks()
# print(type(ticks))
# print(ticks)
# # ax1.set_xticks()
plt.show()
print(type(lob1))