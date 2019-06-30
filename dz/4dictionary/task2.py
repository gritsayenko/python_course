d = {1: True, 2: 'abc', 'msg': 'hello'}
def check_key(d, k):
    d_keys = d.keys()
    if k in d_keys:
        print(True)
    else:
        print(False)

check_key(d, 'msg')


