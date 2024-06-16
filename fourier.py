import matplotlib.pyplot as plt
import math
import numpy
import time
from numba import jit

A = 1
F = 1000
T = 1/F
R = 3300 #ohmns
C = .000000004 #faradios

@jit
def fourier(Armonicos = 500, lines = 1000):
    X = numpy.linspace(0, T, lines)
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
    return X, Y

t_prev = time.time()
_X, _Y = fourier(50000, 1000)
t_diff = time.time() - t_prev
print(t_diff)
plt.plot(_X, _Y)
plt.show()
