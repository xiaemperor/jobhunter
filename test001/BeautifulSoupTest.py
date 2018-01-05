from bs4 import BeautifulSoup
html_sample='<html><body> \
            <h1>HelloWrold</h1> \
            <a href="#">This is a link1</a>\
<a href="www.baidu.com" id="link">This is a link2</a>\
            </body></html>'
soup = BeautifulSoup(html_sample,'html.parser');
print(type(soup))
print(soup.text)
print(soup.select('h1'))
print(soup.select('h1')[0])
print(soup.select('h1')[0].text)  #标签h1中的text
alink = soup.select('a') #获取标签a
print(alink)
for link in alink: #循环
    print(link)
    print(link['href']) #获取a元素中的具体单元内容
alinkbyid = soup.select("#link"); #选择器。#为id，.为class
print(alinkbyid[0].text)