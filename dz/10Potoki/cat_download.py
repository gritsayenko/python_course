import requests
from threading import Thread 
import pathlib

p = pathlib.Path("cats/")
p.mkdir(parents=True, exist_ok=True)
API_KEY = '2cd9bcdf-fc78-4a25-ac1f-53dbfae17750'
source=[]

def get_urls():
	# logger.debug("loading started")
	r = requests.get(
		'http://api.thecatapi.com/v1/images/search', 
		params = {
		'limit':100
		}, 
		headers={
		'x-api-key': API_KEY
	})
	data = r.json()
	# logger.debug("loaded page")
	r.close()
	return data
tr1 = Thread(target=get_urls, args=('Thread-1', ))
tr2 = Thread(target=get_urls, args=('Thread-2', ))

if __name__== '__main__':
	tr1.start()
	tr2.start()
for _ in range(10):
	source.extend(i['url'] for i in get_urls())


# logger.debug("starting loader")

def load_cat(url):
	r= requests.get(url)
	data=r.content
	r.close()
	*_,name = url.split('/')
	return name,data

for num,link in enumerate(source):
	name,pic = load_cat(link)
	store.joinpath(name).write_bytes(pic)
	print('saved',num, 'from', len(source))
	#logger.info("File saved")

	