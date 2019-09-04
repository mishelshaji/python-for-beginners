import urllib.request

url = 'FILE_URL_HERE'
urllib.request.urlretrieve(url, 'img/FILE.jpg')
print('Download completed')

