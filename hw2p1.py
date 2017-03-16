''' A simple program to plot the train packet problem '''

from math import factorial
import matplotlib.pyplot as plt

X = [0, 5, 10, 15, 20, 25, 30]

Y = [6, 6, 6, 12, 18, 36, 128]

plt.plot(X, Y)
#plt.axis([0, NMAX, 0, 1])
plt.xlabel('SNR')
plt.ylabel('Bit Rate')
#plt.title(str(MBPS)+' MBPS')
plt.show()
