# не придумала пока другого решения, понимаю что этот может не подходить для больших файлов и займёт много памяти
import os
def message_write(filepath,message):
	if not os.path.exists(filepath):
		f = open(filepath, "w")
		f.write(message)
	else:
		f = open(filepath, 'r')
		file = f.read()
		f.close()
		f = open(filepath, 'w')
		f.write((message +' '+ file))
message_write('.\\file_name.py', "Message")


