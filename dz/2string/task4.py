s = 'Nwxisl scelerisque justo per hac cras purus lectus maecenas litora facilisi potenti'

if s.find('x') <= 0:
    print('There is no character x in the string')
elif s.find('w') <= 0:
    print('There is no character w in the string')
elif s.find('x') < s.find('w'): 
    print ('The character x in the string occurs before w')
else:
    print('The character w in the string occurs before x')
