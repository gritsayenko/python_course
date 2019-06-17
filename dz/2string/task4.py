s = 'Nwisxl scelerisque justo per hac cras purus lectus maecenas litora facilisi potenti'
s1 = 'x'
s2 = 'w'
x = []
y = []
for i in range(0, len(s)):
    if s[i] == s1:
        x.append(i)
    elif s[i] == s2:
    	y.append(i)
if len(x) == 0:
    print('There is no character x in the string')
elif len(y) == 0:
    print('There is no character w in the string')
else:
    if x[0] < y[0]:
        print ('The character x in the string occurs before w')
    else:
        print('The character w in the string occurs before s')


