import zipfile
#import os
 
files = zipfile.ZipFile('D:\\Python\\dz\\7Files\\testfile.zip')
files.extractall('D:\\Python\\dz\\testfile')
files.close()
result_f = open('D:\\Python\\dz\\testfile\\testfile.dat')
#or line in result_f:
while True:
    data = result_f.read(1024)
    print(data)
 
    if not data:
        break
result_f.close()
#print(link.read())



"""
if file is max(paths, key=os.path.getctime)
print(f.read())       
files.close()

filelist = [os.path.join(rootpath, f) for f in os.listdir(rootpath)]
filelist = [f for f in filelist if os.path.isfile(f)]
newest = max(filelist, key=lambda x: os.stat(x).st_mtime)"""
