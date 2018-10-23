import math
import matplotlib.pyplot as plt

iniV = int(input("Input initial velocity: "))
angle = math.radians(int(input("Input throwing angle: ")))
g = 9.8

print(angle)

time = (2*(iniV*(math.sin(angle))))/g
time = round(time)
print(time)

def getHorizontal(iniV, time, angle):
    hvalues = []
    for second in range(0, time+1):
        hvalues.append(iniV * second * math.cos(angle))
    return hvalues

def getVertical(iniV,time, g, angle):
    vvalues = []
    for second in range(0, time+1):
        vvalues.append((iniV * second * math.sin(angle)) - (0.5 * g * (second**2)))
        # print(vvalues)
    return vvalues

hvalues = getHorizontal(iniV, time, angle)
vvalues = getVertical(iniV,time, g, angle)

plt.ylabel = "vertical displacement (m)"
plt.xlabel = "horizontal displacement (m)"

plt.plot(hvalues, vvalues, marker= "*")
plt.show()
