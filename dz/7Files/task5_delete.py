import os

def del_empty_dirs(path):
	for dirs in os.listdir(path):
		dir_i = os.path.join(path, dirs)
		if os.path.isdir(dir_i):
			if not os.listdir(dir_i):
				os.rmdir(dir_i)
				print('Directories ',dir_i, 'removed')

del_empty_dirs('.\\')

