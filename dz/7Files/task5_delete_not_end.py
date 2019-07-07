import os
def del_emty_folders(path):
	#for dirs in os.walk(path):
	print(list(os.walk(path)))
	"""try:
			os.rmdir(dirs)
		except:
			pass
		
	for root, dirs, files in os.walk(src):
		for root, dirnames, filenames in os.walk(src):
			file_size = [os.stat(src(files)).st_size for name in files]
			print(file_size)"""
del_emty_folders('D:\\Python\\dz\\7Files')
