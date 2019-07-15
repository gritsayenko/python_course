# не придумала пока другого решения, понимаю что этот может не подходить для больших файлов и займёт много памяти
import os
def message_write(filepath,message):
	if not os.path.exists(filepath):
		f = open(filepath, "a+")
		f.write(message)
	else:
		with open(filepath, 'r+', encoding='utf-8') as f:
			exist_filedata = f.read()
			f.seek(0)
			f.write(message + ' ' + exist_filedata)


message_write('.\\file_name.py', "Message")
message_write('.\\file_name.py', "Message2")


