l = ''
x = '0123456789'
y = 'abcdefgjhf'
for i in range(0,10):
	if i % 2 == 0:
		l = l + str(i)
		l = l + y[i]
print(l)

