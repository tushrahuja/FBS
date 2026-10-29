hours = int(input('Enter the hours: '))
minutes = int(input('Enter the minutes: '))
seconds = int(input('Enter the seconds: '))

total_seconds = (hours * 3600) + (minutes * 60) + seconds

print(f'Total seconds are {total_seconds}')