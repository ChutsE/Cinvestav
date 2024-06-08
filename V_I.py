import matplotlib.pyplot as plot
import math

Vp = 30     # V
C = 0.0000000001 # 0.1uF

V = []
I = []

v = 0
for n in range(1, 21):
    #Voltaje 
    v_next = Vp * math.sin(math.pi*n/10)
    #Corriente
    i = C * (v_next-v)
    
    print("n{}\t{:.2f}\t{}".format(n,v,i))
    V.append(v)
    I.append(i)    
    v = v_next
    
plot.plot(V)
plot.plot(I)
plot.show()