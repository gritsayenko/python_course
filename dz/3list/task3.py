l = [1, 2, 3, 4, 6, 8, '1', '2']
s = 0
for i in range(0, len(l)):
	if type(l[i]) is int and l[i] % 2 == 0:
		s = s + l[i]
print(s)
