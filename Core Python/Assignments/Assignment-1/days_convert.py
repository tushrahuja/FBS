days = int(input('Enter the number of days: '))

years = days // 365 
rem_days = days % 365
weeks = rem_days // 7
rem_days %= 7

print(f'{days} days are {years} years, {weeks} weeks and {rem_days} days')