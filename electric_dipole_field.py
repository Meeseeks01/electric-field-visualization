import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from copy import deepcopy

def makefield(xs, ys):
    qtopos = {1: (-1,0), -1: (1.0, 0)}
    n = len(xs)
    Exs = [[0. for k in range(n)] for j in range(n)]
    Eys = deepcopy(Exs)
    for j,x in enumerate(xs):
        for k,y in enumerate(ys):
            for q,pos in qtopos.items():
                posx, poxy = pos
                R = sqrt((x-posx)**2 + (y-poxy)**2)
                Exs[j][k] += q * (x - posx) / R**3
                Eys[j][k] += q * (y - poxy) / R**3
    return Exs, Eys

def plotfield(boxl,n):
    xs = [-boxl/2 + i*2*boxl/(n-1) for i in range(n)]
    ys = xs[:]
    Exs, Eys = makefield(xs, ys)
    xs=np.array(xs); ys=np.array(ys)
    Exs=np.array(Exs); Eys=np.array(Eys)
    plt.streamplot(xs, ys, Exs, Eys, color='m', density=1.5)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.title('Electric field of dipole')
    plt.show()

plotfield(2.,20)
