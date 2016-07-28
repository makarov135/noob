import urllib.request
from bs4 import BeautifulSoup

url = 'http://tieba.baidu.com/p/4405041388?pn='
def download(url):
    html = urllib.request.urlopen(url)
    bs = BeautifulSoup(html,'html.parser')
    img_list = bs.find_all('img',class_="BDE_Image")
    x = 0
    for i in img_list:
        imgurl = i.get('src')
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        print('Downloading %s picture now!!!' % x)
        x += 1
    return x

for k in range(1,29):
    ur = url + str(k)
    download(ur)

