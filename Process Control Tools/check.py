from sympy import symbols, exp, oo, integrate, pi

def calculate_dn(n):
    x, y = symbols('x y')
    phi = symbols('phi', cls=Function)(x+y)

    # Define the integrand
    integrand = (n*(n-1)*pi**2 * exp(-(x**2 + (y+x)**2)/2) * (phi - symbols('phi', cls=Function)(x))**(n-2))

    # Perform the double integration
    result = integrate(integrate(integrand, (x, -oo, oo)), (y, -oo, oo))

    return result

# Test the function for a specific value of n
n = 3
result = calculate_dn(n)
print(f"The value of d(n) for n = {n} is: {result}")