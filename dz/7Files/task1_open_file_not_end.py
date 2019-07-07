import zipfile
import os
 
files = zipfile.ZipFile('D:\\Python\\dz\\7Files\\testfile.zip')
files.extractall('D:\\Python\\dz\\testfile')
files.close()
result_f = open('D:\\Python\\dz\\testfile\\testfile.dat')
for line in result_f:
    if os.path.islink(line) is True:
        print(line.read())



"""
if file is max(paths, key=os.path.getctime)
print(f.read())       
files.close()

filelist = [os.path.join(rootpath, f) for f in os.listdir(rootpath)]
filelist = [f for f in filelist if os.path.isfile(f)]
newest = max(filelist, key=lambda x: os.stat(x).st_mtime)"""
