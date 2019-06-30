import collections
s = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce fermentum volutpat velit, sit amet consequat massa convallis in. Mauris sollicitudin fringilla augue et pellentesque. Curabitur at sapien in dolor malesuada luctus. Nullam. '''
def counter(s):
    counter_letter = dict(collections.Counter([s[i:(i+2)].lower() for i in range(0, len(s))]))
    print (counter_letter)

counter(s)
