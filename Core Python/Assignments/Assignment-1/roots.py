a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

d = (b**2) - (4*a*c)

root1 = (-b + (d**0.5)) /(2 * a)
root2 = (-b - (d**0.5)) /(2 * a)

print(f'Root 1: {root1:.2f}')
print(f'Root 2: {root2:.2f}')