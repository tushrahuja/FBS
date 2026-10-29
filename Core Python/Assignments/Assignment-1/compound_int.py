amount = int(input('Enter the Principal Amount: '))
interest = int(input('Enter the Rate of Interest: '))
time = int(input('Enter the time in years: '))

total_amount = amount*(1+(interest/100))**2
CI = total_amount - amount

print(f'Compound Interest on amount {amount}₹ at {interest}% interest for {time} years is {CI:.2f}₹')