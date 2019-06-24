d = {2: True, 4: 'abc', 'msg': 'hello'}
def fn(d):
    for key, value in d.items():
        print('{} {}'.format(key, value))

fn(d)

