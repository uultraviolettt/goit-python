print('Enter odds, please')

a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))

print(f"Equation: {a}*x**2 + {b}*x + {c}")

rd = (b**2 - 4 * a * c)**0.5
r1 = (-b - rd) / (a * 2)
r2 = (-b + rd) / (a * 2)

print(f"Discriminant is: {rd}")
print(f"Roots of eq are: x1={r1} & x2={r2}")










