#import collection
d1 = {1: True, 2: 'abc', 'd': 'hello'}
d2 = {5: True, 2: 'abc', 'msg': 'hello'}
d3 = {1: True, 4: 'abc', 'msg': 'hello'}
r = {}
for i in range(0,len(d1)):
    if d1[i] in d2:
        pass
    if d1[i] in d3:
        pass
    else:
        r.update(d1[i])

#def merge(d1,d2,d3):



