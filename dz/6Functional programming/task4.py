from time import sleep
from datetime import datetime
def decorator(fn):
	def decorated_fn(*args,**kwargs,):
		fn(*args, **kwargs)
		print('function call time - ', datetime.now().strftime('%H:%M:%S'))
	return decorated_fn

@decorator
def my_fn():
	print('"my_fn" executed')
    
@decorator
def my_delayed_fn(n):
	sleep(n)
	print('"my_delayed_fn" executed')

my_fn()
my_delayed_fn(3)