feet = int(input('Enter the feet: '))
inches = int(input('Enter the inches: '))

total_inches = (feet * 12) + inches

centimeter = total_inches * 2.54
meters = centimeter / 100

print(f'Total meters: {meters} and total centimeters: {centimeter}')