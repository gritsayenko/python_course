s = 'abcsdf aads'
if s[0:3] == 'abc':
	s = 'www' + s[3:]
else:
	s = s + 'zzz'
print(s)
