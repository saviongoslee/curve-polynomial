# Example of Interpolation Using NumPy.

import numpy as np
import matplotlib.pyplot as plt

# Configuration

x = np.array([5, 4, 9]) # Curve representation.
y = np.array([6, 2, 8]) # PRF value.

use_graph = True

# Functions

def use_poly(poly, x_range): # Adjust x-range, calculate y-values using polyfit.
    new_x = np.array(x_range)
    new_y = poly(new_x)
    return new_x, new_y


def show_graph(x, y, new_x, new_y):
    if not use_graph: return

    plt.plot(new_x, new_y, label='Polynomial Fit')
    plt.scatter(x, y, color='red', label='Data Points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Polynomial Interpolation')
    plt.legend()
    plt.show()

# Program
        
def main():
    curve = np.polyfit(x, y, 2) # Fits a polynomial using a degree to (x, y).
    poly = np.poly1d(curve) # Create a Polynomial object using the fit.
    new_x, new_y = use_poly(poly, range(-10, 12))
    
    print(f"""
    Polynomial Fit:
    {poly}
    """)

    show_graph(x, y, new_x, new_y)    

main()
