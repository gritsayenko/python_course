s = 'neERTERTyre'
if len(s) % 2 == 1:
    middle_number = int(len(s) / 2 )
    middle_symbol = s[middle_number]
    result = middle_symbol.lower()
    print("The middle symbol is ", result)
else:
    print('This string have not one the middle symbol')

