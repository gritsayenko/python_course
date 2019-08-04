def list_important_things(primary, *args):
     print(primary, *args)

def rpart(list_important_things, *args, **kwargs):
    pass
    
list_dispute_args = rpart(fn, 'и животноводство', 'and my axe!')
list_dispute_args(input('dispute args: '))
"""def a(x, y):
  print (x, y)

def b(other, function, *args, **kwargs):
  function(*args, **kwargs)
  print (other)

b('world', a, 'hello', 'dude')"""