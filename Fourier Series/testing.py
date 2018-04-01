import sympy as sym

x = sym.symbols('x')

f = sym.Function('f')
print (sym.dsolve(sym.Derivative(f(x), x) + 9*f(x), f(x)))