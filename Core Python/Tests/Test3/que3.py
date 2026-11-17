num = int(input('Enter the number of employees: '))
total = 0
for i in range(1, num + 1):
  salary = int(input(f'Enter the salary of Employee{i}: '))
  if(salary < 20000):
    da = salary * 0.10
    ta = salary * 0.12
    hra = salary * 0.15
    sum = da + ta + hra + salary
    print(f'Salary of Employee{i}: {sum}')
    total += sum
  elif(salary >= 20000):
    da = salary * 0.15
    ta = salary * 0.18
    hra = salary * 0.20
    sum = da + ta + hra + salary
    print(f'Salary of Employee{i}: {sum}')
    total += sum
print(f'Total Salary is {total}')