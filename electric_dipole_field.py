import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

def makefield(xs, ys):
    # Dipole: +1 at (-1,0), -1 at (1,0)
    charges = [
        (+1.0, -1.0, 0.0),
        (-1.0,  1.0, 0.0),
    ]

    n = len(xs)
    Exs = [[0.0 for _ in range(n)] for _ in range(n)]
    Eys = [[0.0 for _ in range(n)] for _ in range(n)]

    for j, x in enumerate(xs):
        for k, y in enumerate(ys):
            for q, posx, posy in charges:
                R = sqrt((x - posx)**2 + (y - posy)**2)
                if R == 0:
                    continue
                Exs[j][k] += q * (x - posx) / R**3
                Eys[j][k] += q * (y - posy) / R**3

    return Exs, Eys, charges


def plotfield(boxl, n):
   
    xs = [-boxl/2 + i*boxl/(n-1) for i in range(n)]
    ys = xs[:]

    Exs, Eys, charges = makefield(xs, ys)

    xs = np.array(xs)
    ys = np.array(ys)
    Exs = np.array(Exs)
    Eys = np.array(Eys)

    plt.figure(figsize=(6, 6))
    plt.streamplot(xs, ys, Exs, Eys, color='m', density=1.5)

    # Plot the charges (bodies)
    for q, x0, y0 in charges:
        if q > 0:
            plt.plot(x0, y0, 'ro', markersize=10, markeredgecolor='k')
        else:
            plt.plot(x0, y0, 'bo', markersize=10, markeredgecolor='k')

    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.title('Electric field of dipole')
    plt.axis('equal')
    plt.xlim(-boxl/2, boxl/2)
    plt.ylim(-boxl/2, boxl/2)
    plt.show()


plotfield(4.0, 40)  


