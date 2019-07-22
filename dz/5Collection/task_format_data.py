import collections
f = open('.\\test_data.txt', 'r', encoding='utf-8')
s = ''.join(f.readlines())
brands=[]
new_dict={}
for item in s.split('\n'):
	new_list = item.split(';')
	brands.append(new_list[0])
# formating data to new dictionary
	new_dict.update({ new_list[0]: {new_list[1]: {
            'name': new_list[2],
            'quantity': new_list[3],
            'price': new_list[4] }
           } } )
# brand with max count of the products
counter_products = collections.Counter(brands)
print('Brand with max count of the products ', counter_products.most_common(1))
print(new_dict)

def filter(x):
	for item in new_dict.values():
		if x in item.keys():
			print(item)

filter('"ZZJ118110"')

f.close()