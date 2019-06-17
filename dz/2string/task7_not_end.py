s = 'Nesaxb'
for i in range(0, len(s)):
	if i % 2 == 1:
		if s[i] == 'a':
			s = s.replace(s[i], 'c')
		elif s[i] == 'b':
		 	s = s.replace(s[i], 'c')
		else:
			s = s.replace(s[i], 'a')
print(s)
