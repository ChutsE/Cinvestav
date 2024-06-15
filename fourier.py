import matplotlib.pyplot as plt
import math
import numpy

A = 1
F = 1000
T = 1/F
R = 3300 #ohmns
C = .000000004 #faradios

Armonicos = 50000

X = numpy.linspace(0, T, 1000)
Y = []
for x in X:
    f_sum = 0
    for n in range(1, Armonicos + 1):
        if n%2 == 1:
            f = n*F
            Ganancia = 2*math.pi*f*R*C/math.sqrt(1+2*math.pi*f*R*C)
            f_sum += Ganancia*4*(math.sin(2*math.pi*f*x))/(n*math.pi)
        else:
            pass
    Y.append(f_sum)

plt.plot(X, Y)
plt.show()
