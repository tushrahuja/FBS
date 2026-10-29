num = int(input('Enter a number: '))

d1 = num % 10
d2 = (num // 10) % 10
d3 = num // 100

sum = d1 + d2 + d3
  
print(f'Sum of digit {num} is {sum}')