import urllib.request
from bs4 import BeautifulSoup
import os

def Download(url, picAlt, name):
    #存储路径
    path = r'C:\Users\ASUS\Desktop\成果\python爬虫妹子图'+picAlt+'\\'
    if not os.path.exists(path):
        os.makedirs(path)
    urllib.request.urlretrieve(url, '{0}{1}.jpg'.format(path, name))

header = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}

def run(targetUrl, beginNUM, endNUM):
    req = urllib.request.Request(url=targetUrl)
    response = urllib.request.urlopen(req)
    html = response.read().decode('gb2312', 'ignore')
    soup = BeautifulSoup(html, 'html.parser')
    Divs = soup.find_all('div', attrs={'id':'big-pic'})
    nowpage = soup.find('span', attrs={'class':'nowpage'}).get_text()
    totalpage=soup.find('span', attrs={'class':'totalpage'}).get_text()
    if beginNUM == endNUM:
        return
    for div in Divs:
        beginNUM = beginNUM+1
        if div.find("a") is None:
            print("没有下一张啦")
            return
        elif div.find("a")['href'] is None or div.find("a")['href'] =="":
            print("没有下一张啦")
            return
        print("下载信息：总进度：",beginNUM, "", endNUM,", 正在下载套图：(",nowpage,"",totalpage,")")
        if int(nowpage) < int(totalpage):
            nextPageLink ="http://www.mmonly.cc/mmtp/qcmn/" +(div.find('a')['href'])
        elif int(nowpage) == int(totalpage):
            nextPageLink =(div.find('a')['href'])
        picLink = (div.find('a').find('img')['src'])
        picAlt = (div.find('a').find('img'))['alt']
        print('下载的图片链接：', picLink)
        print('套图名：[',picAlt,']')
        print('开始下载..........')
        Download(picLink, picAlt, nowpage)
        print('下载成功！')
        print('下一页链接:', nextPageLink)
        run(nextPageLink, beginNUM, endNUM)
        return            

if __name__ == '__main__':
    #爬虫图片途径,可以修改路径
    targetUrl = "http://www.mmonly.cc/mmtp/qcmn/294125.html"
    run(targetUrl, beginNUM=0, endNUM=70)
    print(" OVER")