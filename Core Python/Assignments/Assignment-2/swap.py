a = int(input("Enter a number for 'a': "))
b = int(input("Enter a number for 'b': "))

print(f"Before Swap: 'a': {a}, 'b': {b}")

temp = a
a = b
b = temp

print(f"After Swap: 'a': {a}, 'b': {b}")