from sympy import symbols, summation, sympify

x, i = symbols("x i")

def riemannSum(func, n, a, b, type):

    expr = sympify(func)
    delta = (b-a) / n

    if type == 'left':
        sum = summation(expr.subs(x, a + i*delta) * delta, (i, 0, n-1))
    elif type == 'right':
        sum = summation(expr.subs(x, a + i*delta) * delta, (i, 1, n))

    return sum

print(riemannSum("x**2 + 3*x + 1", 10, 0, 10, "right"))



