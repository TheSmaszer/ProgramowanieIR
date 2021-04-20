import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np 

mass = float(input("Enter mass m [kg] (m > 0): "))
v0 = float(input("Enter initial velocity v0 [m/s] (v0 >= 0): "))
alpha = float(input("Enter initial angle \u03B1 [rad] (0 <= \u03B1 <= \u03C0/2): "))
offset = float(input("Enter initial height h [m] (h >= 0): "))
beta = float(input("Enter the drag coefficient \u03B2 (\u03B2 > 0): "))

# v0 = 1
# alpha = 1
# mass = 10
# offset = 200
# beta = 1

g = 9.81

if(alpha<0 or alpha>np.pi/2 or v0<0 or mass<=0 or beta<=0 or offset<0):
    print("Wrong values")
    quit()

height = (beta*offset + (1/2)*mass*np.log(1 + (beta*(v0**2)*(np.sin(alpha)**2))/(g*mass)))/beta
period = max((np.sqrt(mass)*(np.arccosh(np.e**((2*beta*offset + mass*np.log(1 + (beta*(v0**2)*(np.sin(alpha)**2))/(g*mass)))/(2*mass))) + np.arctan((np.sqrt(beta)*v0*np.sin(alpha))/(np.sqrt(g*mass)))))/(np.sqrt(beta*g)),(np.sqrt(mass)*(-np.arccosh(np.e**((2*beta*offset + mass*np.log(1 + (beta*(v0**2)*(np.sin(alpha)**2))/(g*mass)))/(2*mass))) + np.arctan((np.sqrt(beta)*v0*np.sin(alpha))/(np.sqrt(g*mass)))))/(np.sqrt(beta*g)))
distance = -((mass*np.log(mass))/beta) + (mass*np.log(mass + beta*period*v0*np.cos(alpha)))/beta
print("\n#############Calculated values#############")
print(f"Total height:{round(height,3)} m")
print(f"Total time:{round(period,2)} s")
print(f"Total distance:{round(distance,3)} m")
print("###########################################")

fig = plt.figure(figsize=(10,7))
ax1 = plt.axes(xlim=(0, 1.1*distance), ylim=(0,1.1*height))
line, = ax1.plot([], [])
plt.xlabel('Distance [m]')
plt.ylabel('Height [m]')
plt.title("Projectile motion in gravitational field with drag $F_{op} = \u03B2 v^2$")
plt.grid()

lines = []
lob1 = ax1.plot([],[], color="#4B4453",label="Flight trajectory")[0]
# lob1.text("1")
lines.append(lob1)
lob2 = ax1.plot([],[],"*",markersize=10,color="#845EC2",label="Current position")[0]
lines.append(lob2)
time_text = ax1.text(0.05*distance, 0.05*height, '', fontsize=10, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=.5'))
plt.legend()


def init():
    for line in lines:
        line.set_data([],[])
    return lines

x1,y1 = [],[]
x2,y2 = [],[]

def animate(i):
    time_text.set_text(f"Current time: {round(i,2)} [s] \nParameters: \u03B2={beta}, m={mass}[kg], h={offset}[m],\nv0={v0}[m/s], \u03B1={alpha}[rad]")
    x = -((mass*np.log(mass))/beta) + (mass*np.log(mass + beta*i*v0*np.cos(alpha)))/beta
    # vx = -(mass/(-beta*i - (mass)/v0*np.cos(alpha)))
    if (i <= (np.sqrt(mass)*np.arctan((np.sqrt(beta)*v0*np.sin(alpha))/(np.sqrt(g*mass))))/(np.sqrt(beta*g))):
#RISE
        y = -((mass*np.log(np.cosh((np.sqrt(beta*g)*i)/np.sqrt(mass) - np.arctan((np.sqrt(beta)*v0*np.sin(alpha))/(np.sqrt(g*mass))))))/beta) + (beta*offset + (1/2)*mass*np.log(1 + (beta*(v0**2)*(np.sin(alpha)**2))/(g*mass)))/beta
        # vy = (np.sqrt(g*mass)*np.tan((-np.sqrt(beta*g)*i +np.sqrt(mass)*np.arctan((np.sqrt(beta)*v0*np.sin(alpha))/(np.sqrt(g*mass))))/np.sqrt(mass)))/np.sqrt(beta)
    else:
#FALL
        # vy = (np.sqrt(g*mass)*np.tanh((-np.sqrt(beta*g)*i +np.sqrt(mass)*np.arctan((np.sqrt(beta)*v0*np.sin(alpha))/(np.sqrt(g*mass))))/np.sqrt(mass)))/np.sqrt(beta)
        y = (2*beta*offset - 2*mass*np.log(np.cosh((np.sqrt(beta*g)*i)/np.sqrt(mass) - np.arctan((np.sqrt(beta)*v0*np.sin(alpha))/(np.sqrt(g*mass))))) + mass*np.log(1 + (beta*(v0**2)*np.sin(alpha)**2)/(g*mass)))/(2*beta)
    # print(vy, vx)
    x1.append(x)
    y1.append(y)

    xlist = [x1, x]
    ylist = [y1, y]

    for lnum,line in enumerate(lines):
        line.set_data(xlist[lnum], ylist[lnum]) # set data for each line separately.
    return lines, time_text

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=np.linspace(0, period,200), interval=5,repeat=False)
xticks = list(ax1.get_xticks())
xticks.append(round(distance,1))
ax1.set_xticks(xticks)
yticks = list(ax1.get_yticks())
yticks.append(round(height,1))
ax1.set_yticks(yticks)
fig.tight_layout()
plt.show()