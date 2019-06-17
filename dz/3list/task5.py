from typing import Any

l = []
l1 = [1,3,4]
l2 = ['w','hello',3,5]
l3 = []
l.append(l1)
l.append(l2)
l.append(l3)

def check_empty_list(l):
        count = 0
        for i in range (0,len(l)):
	        if len(l[i]) < 1:
                    count = count + 1
        if count > 0:
            print("The current list contains", count, "empty list item(s)")
        else:
            print("The current list does not contain an empty list item.")
check_empty_list(l)
