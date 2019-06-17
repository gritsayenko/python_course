s1 = 'dsjgjdhgfsjdh'
s2 = 'dsjgfjshdgfhsjdh'
if s1[0:4] == s2[0:4]:
	if s1[-4:] == s2[-4:]:
		print('The first and last 4 characters are the same in these strings')
	else:
		print('In this strings are not the same the first and the last 4 characters')
else:
	print('In this strings are not the same the first and the last 4 characters')

