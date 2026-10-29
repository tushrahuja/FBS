a = int(input("Enter a number for 'a': "))
b = int(input("Enter a number for 'b': "))

print(f"Before Swap: 'a': {a}, 'b': {b}")

a = a + b
b = a - b
a = a - b 

print(f"After Swap: 'a': {a}, 'b': {b}")