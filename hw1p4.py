''' A simple program to plot the train packet problem '''

from math import factorial
import matplotlib.pyplot as plt

MBPS = 10
P_SIZE = 12000
P_NUM = 100
TT = ((P_NUM*P_SIZE)/float(1000000)/MBPS)
NMAX = int(input("Enter the max number of trains: "))
N = 2
TRAINS = []
PERCENTS = []
P = 0
while N <= NMAX:
    TRAINS.append(N)
    P = 1-((1-(N*TT))**(N-1))
    #P = (factorial(N)/float(factorial(N-2)*2)) * (TT+TT)
    print ("With", str(N), "trains there is a", str(P) +" chance of a collision")
    PERCENTS.append(P)
    N += 1

plt.plot(TRAINS, PERCENTS)
plt.axis([0, NMAX, 0, 1])
plt.xlabel('# of trains')
plt.ylabel('collision probability')
plt.title(str(MBPS)+' MBPS')
plt.show()
