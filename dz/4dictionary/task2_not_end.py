d = {1: True, 2: 'abc', 'msg': 'hello'}
def check_key(d, k):
    res = 0
    d_keys = d.keys()
    if k in d_keys:
        res = res + 1

check_key(d, 'msg')
 


