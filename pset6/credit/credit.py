import re
original = input('Number: ')
card = list(original)
card.reverse()
card = ''.join(card)
even = [int(card[i]) for i in range(len(card)) if i % 2 == 0]
odd = [int(card[i]) * 2 for i in range(len(card)) if i % 2 != 0]
even = [str(i) for i in even]
odd = [str(i) for i in odd]
even = ''.join(even)
odd = ''.join(odd)
even = [int(i) for i in even]
odd = [int(i) for i in odd]
result = sum(even) + sum(odd)

if result % 10 == 0:
    if len(original) == 15 and (original[:2] == '34' or original[:2] == '37'):
        print('AMEX')
    elif len(original) == 16 and re.search('51|52|53|54|55', original[:2]):
        print('MASTERCARD')
    elif (len(original) == 16 or len(original) == 13) and original[0] == '4':
        print('VISA')
    else:
        print('INVALID')
else:
    print('INVALID')