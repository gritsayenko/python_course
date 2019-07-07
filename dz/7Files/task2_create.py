from datetime import datetime
date = str(datetime.today())
f = open('.\\timefile.py', 'tw', encoding='utf-8')
f.write(date + "\n")
f.close()
