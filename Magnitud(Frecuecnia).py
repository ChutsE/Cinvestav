import matplotlib.pyplot as plt
import math
from numba import njit

@njit
def gain_calculation(f_1, f_2, R_rate):
    Gain_1= []
    Gain_2 = []
    Error = []
    #F_MAX = 1000000
    F_MAX = 60000
    frecuencies = [i for i in range(F_MAX)]
    for frecuency in frecuencies:
        const = (f_1**2 + frecuency**2)*(f_2**2 + frecuency**2)
        
        gain_1 = frecuency*f_1/math.sqrt(const)
        gain_2 = frecuency*f_1/math.sqrt(const + frecuency**2*R_rate*f_2*(f_2 + 2*f_1))

        Gain_1.append(gain_1)
        Gain_2.append(gain_2)

        Error.append(gain_1-gain_2)
    
    return  Gain_1, Gain_2, Error

def main():
    f_1 = 100
    f_2 = 10000
    R2_R4 = [ i/10000000 for i in range(0,20000000,10000) ]
    relative_error_array = []
    for r4_r2 in R2_R4:
        Gain_1, Gain_2, Error = gain_calculation(f_1, f_2, r4_r2)
        max_gain_1 = max(Gain_1)
        max_gain_2 = max(Gain_2)
        relative_error = (max(Error)/max_gain_1) * 100
        relative_error_array.append(relative_error)
        print("R4/R2 = {}  0.707*Max_Gain1 = {}   Max_Gain2 = {}".format(r4_r2, 0.707*max_gain_1, max_gain_2))

    plt.plot(R2_R4, relative_error_array)
    plt.ylabel("Error Relativo %")
    plt.xlabel("R4/R2") 
    plt.grid()
    plt.show()

    plt.subplot(2,1,1)
    plt.plot(Gain_1, color = 'darkred', label = 'max={:.5f}'.format(max_gain_1))
    plt.plot(Gain_2, color  = 'darkblue', label = 'max={:.5f}'.format(max_gain_2))
    plt.axvline(x = f_1, color = 'g', linestyle='-.')
    plt.axvline(x = f_2, color = 'g', linestyle='-.')
    plt.xscale("log")
    plt.xlabel("frecuency")
    plt.yscale("log")
    plt.ylabel("gain")
    plt.legend()

    plt.subplot(2,1,2)
    plt.plot(Error, color  = 'darkgreen', label = 'error')
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()