amount = int(input('Enter the Principal Amount: '))
interest = int(input('Enter the Rate of Interest: '))
time = int(input('Enter the time in years: '))

SI = (amount*interest*time)/100

print(f'Simple Interest on amount {amount}₹ at {interest}% interest for {time} years is {SI}₹')