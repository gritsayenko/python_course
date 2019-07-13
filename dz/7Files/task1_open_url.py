import zipfile
 
files = zipfile.ZipFile('.\\testfile.zip')
files.extractall('.\\testfile')
files.close()
f = open('.\\testfile\\testfile.dat', 'rb')
while True:
	data = f.read(1024*1024)
	if "http" in str(data):
		print(data)
	if data == "":
		break
f.close()