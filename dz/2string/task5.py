s = 'Nwisxlggjj'
if len(s) > 10:
    s = s[0:6]
else:
    x = 12 - len(s)
    s = s + 'o' * x
print(s)
