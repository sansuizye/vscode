import requests
from lxml import etree

urx = "https://new.qq.com/rain/a/20211128A05MMY00"
response = requests.get(urx).text
selector = etree.HTML(response)
image = selector.xpath('//img[@class="content-picture"]/@src')
name = "图"
index = 0
filename = 'images.jpg' 

with open(filename,'wb') as f:
    img = requests.get('https://inews.gtimg.com/newsapp_bt/0/14236427157/1000').content
    f.write(img)
        
        



