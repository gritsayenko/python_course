l = []
l1, l2, l3 = [],[2,2],[2,2]
l.append(l1)
l.append(l2)
l.append(l3)

def check_empty_list(l):
	x = []
	for i in range (0,len(l)):
		if l[i] ==  x:
			pass
		else:
			print("The current list contain at list one not empty list item(s)")
			break 	
check_empty_list(l)
