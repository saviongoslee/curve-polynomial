# Example of Interpolation.

import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import numpy as np
import ecdsa
import hashlib
import random

# Configuration

xgr = [] # Graph workaround.
ygr = []

x = []
y = []

use_graph = True

for i in range(3):
    G = ecdsa.curves.Ed25519.generator
    P = G + G
    P = P.x()

    # Randomly generated coordinates.

    _hash = hashlib.sha256(str(P).encode())
    _hex = int(_hash.hexdigest(), 16)

    x.append(_hex + random.randint(20, 100)) 
    y.append(_hex + random.randint(1, 100))

    # Adjusted coordinates (for graphing).

    _hex = (round(_hex, 2) % 1000) + random.randint(20, 100)
    _y = _hex + random.randint(1, 100)

    xgr.append(_hex)
    ygr.append(_y)

# Functions

def output_poly(adjusted_poly):
    poly = lagrange(x, y)

    print(f"\nActual Polynomial:\n{poly}\n")
    print(f"Graphed Polynomial:\n{adjusted_poly}\n")

def adjust(poly, x_range):
    n_x = np.array(x_range)
    n_y = poly(n_x)
    return n_x, n_y

def show_graph(x, y, n_x, n_y):
    if not use_graph: return

    plt.plot(n_x, n_y, label='Polynomial Fit')
    plt.scatter(x, y, color='red', label='Data Points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Polynomial Interpolation')
    plt.legend()
    plt.show()

# Program

def main():
    x_range = range(int(min(xgr)-10), int(max(xgr)+10))
    poly = lagrange(xgr, ygr)
    n_x, n_y = adjust(poly, x_range)

    output_poly(poly)
    show_graph(xgr, ygr, n_x, n_y)
    

main()
