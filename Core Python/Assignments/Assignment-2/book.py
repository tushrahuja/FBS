cost = int(input('Enter the cost price: '))
discount = int(input('Enter the discount percentage: '))

discount_amt = (cost * discount)/100

selling = cost - discount_amt

print(f'Selling price of book is {selling}₹ after discount of {discount_amt}₹')