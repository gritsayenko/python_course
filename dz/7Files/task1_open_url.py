import zipfile
import os
 
files = zipfile.ZipFile('D:\\Python\\dz\\7Files\\testfile.zip')
files.extractall('D:\\Python\\dz\\testfile')
files.close()
f = open('D:\\Python\\dz\\testfile\\testfile.dat', 'r')
for line in f.readlines():
	if "http" in line:
		print(line)
		break
f.close()
  
