amount = int(input('Enter the amount: '))

five_hun = amount // 500
amount %= 500
two_hun = amount // 200
amount %= 200
one_hun = amount // 100
amount %= 100
fifty = amount // 50
amount %= 50
twenty = amount // 20
amount %= 20
ten = amount // 10
amount %= 10

total_notes = five_hun + two_hun + one_hun + fifty + twenty + ten

print(f'Total notes are {total_notes} in which, 500: {five_hun}, 200: {two_hun}, 100: {one_hun}, 50: {fifty}, 20: {twenty}, 10: {ten}')