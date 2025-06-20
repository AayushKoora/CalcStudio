from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sympy import *

def gradientDescent(func_str, x0, y0, r):
    x, y = symbols('x y')
    func = sympify(func_str)
    deriv_x = diff(func, x)
    deriv_y = diff(func, y)

    step_x, step_y = 1, 1

    n = 0

    while abs(step_x) > .001 or abs(step_y) > .001:

        step_x = r*deriv_x.subs(x, x0)
        step_y = r*deriv_y.subs(y, y0)

        x0 = x0 - step_x
        y0 = y0 - step_y
        z = func.subs({x: x0, y: y0})
        n = n+1

        print(f'Step: {n} ({x0}, {y0}, {z})')

gradientDescent("x**2 + y**2", 50, 29, .1)
