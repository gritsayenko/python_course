d1 = {1: True, 2: 'abc', 'd': 'hello'}
d2 = {5: True, 2: 'abc', 'msg': 'hello'}
d3 = {1: True, 4: 'abc', 'msg': 'hello'}

def diff_dict(*args):
    diff = set()
    for n in args:
        diff = diff ^ set(n.items())
    print(dict(diff))

diff_dict(d1,d2,d3)

