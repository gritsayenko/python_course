import collections
f = open('.\\test_data.txt', 'r', encoding='utf-8')
s = ''.join(f.readlines())
brands=[]
data={}
for i in s.split('\n'):
	l = i.split(';')
	brands.append(l[0])
# отформатированный словарь
	data.update({ l[0]: {l[1]: {
            'name': l[2],
            'quantity': l[3],
            'price': l[4] }
           } } )
# производитель с наибольшим количеством товара
counter = collections.Counter(brands)
print('Brand with max product ', counter.most_common(1))
print(data)

f.close()