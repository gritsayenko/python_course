l = ['w', 2.5, 'r', 4, 5, 6, 'Hello']
s = ''
for i in range(0,len(l)):
	s = s + str(l[i]) + ','
s = s[:-1]
print (s)
