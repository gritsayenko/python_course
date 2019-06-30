s = "Nhsaxb"

def replace(s):
	l = list(s)
	for i in range(0, len(l)):
		if i % 2 == 1:
			if l[i] not in "ab":
				l[i]='a'
			else:
				l[i]='c'
	s = ''.join(l)
	print(s)


replace(s)
