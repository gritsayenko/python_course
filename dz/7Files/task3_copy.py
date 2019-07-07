import os
import shutil

# создание каталога с файлами
filepath = os.path.join('.\\Folder1', 'file1.py')
if not os.path.exists('.\\Folder1'):
    os.makedirs('.\\Folder1')
f1 = open('.\\Folder1\\file1.py', "a")
f1.close()
filepath = os.path.join('.\\Folder1', 'file2.py')
if not os.path.exists('.\\Folder1'):
    os.makedirs('.\\Folder1')
f2 = open('.\\Folder1\\file2.py', "a")
f2.close()

# копирование содержимого папки без атребутов
def copy_files(src):
	for filename in os.listdir(src):
		filepath = os.path.join(src, filename)
		shutil.copy(filepath,src.join('.'))


copy_files('.\\Folder1')
