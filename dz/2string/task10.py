s = 'neERTRRTyre'
if len(s) % 2 == 1:
    middle_number = int(len(s) / 2 )
    middle_symbol = s[middle_number].lower()
    print("The middle symbol is ", middle_symbol)
else:
    print('This string have not one the middle symbol')

