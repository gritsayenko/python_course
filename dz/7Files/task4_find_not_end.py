import os
from os.path import getsize, join
def find(src):
	for root, dirs, files in os.walk(src):
		total_size = sum(getsize(join(root, name)) for name in files)
		print(root, total_size)
		for root, dirnames, filenames in os.walk(src):
			file_size = [os.stat(src(files)).st_size for name in files]
			print(file_size)
		"""if os.path.getsize(filename)> 1048576: 
			files.extend(filename)
	print(files)
	for root, dirs, files in os.walk('D:\\'):
		for file in files:
			if file.endswith('.txt'):
				print(file)

def find():
	list = []
	os.chdir('D:\\')
	for files in os.walk("./"):
		for files in files:
			if '*.*' in files:
				list.append(files)
				print(list)
		if os.path.getsize(files)> 1048576 :
			print(1)
			#return list.append(files)"""
find('D:\\')


#str(os.getenv("SystemDrive")
