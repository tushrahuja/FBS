num = int(input('Enter the number: '))

sum = 0
for i in range(1, num + 1):
  factorial = 1
  for j in range(1, i + 1):
    factorial *= j
  ans = i / factorial
  sum += ans
  
print(f'{sum:.2f}')