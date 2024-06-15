import valores_comerciales
import math

F_0 = 10000 #Hz
error_lim = 300 #Hz

for res_com in valores_comerciales.res:
    for cap_com in valores_comerciales.cap:
        f_real = 1/(2*math.pi*res_com*cap_com)
        error = abs(F_0 - f_real)
        if error < error_lim:
            print("{:.1f}\t{}\t{}".format(f_real,res_com,cap_com))