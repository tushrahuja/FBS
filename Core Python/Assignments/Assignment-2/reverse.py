num = int(input('Enter a number: '))

d1 = num % 10
d2 = (num // 10) % 10
d3 = num // 100

reversed = (d1*100) + (d2*10) + d3
  
print(f'Reversed number is {reversed}')