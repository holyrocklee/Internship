from bs4 import BeautifulSoup, Tag

from util.http_util import download
from util.requestutil import requestutil

requtil = requestutil()
count = 0

'''汽车之家论坛抓取图片
'''


def capture(url):
    global requtil
    requtil.setUrl(url)
    return requtil.request(method='get', json=False, isjson=False)


def analysisPage(html_doc):
    temp = []
    soup = BeautifulSoup(html_doc, 'html.parser')
    for x in soup.find_all('a'):
        if x.get('href').startswith('//club.autohome.com.cn/bbs/thread') and len(list(x.children)) == 1 and x.get('onclick') is None:
            temp.append(x.get('href'))
    return temp


def analysisTie(savepath, html_doc):
    global count
    soup = BeautifulSoup(html_doc, 'html.parser')
    for x in soup.find_all('img'):
        if x.get('onerror') == 'tz.picNotFind(this)':
            count = count + 1
            if x.get('src9'):
                #print(x.get('src9'))
                download('https:' + x.get('src9'), savepath + str(count) + '.jpg')
            else:
                download('https:' + x.get('src'), savepath + str(count) + '.jpg')


if __name__ == '__main__':
    for x in range(10):
        print('page======' + str(x+1))
        # 爬取该栏目下第几页
        page = capture('https://club.autohome.com.cn/jingxuan/119/' + str(x + 1))
        tielist = analysisPage(page)
        print(tielist[0])
        analysisTie('C:\\api_iscar\\', capture('https:' + tielist[0]))
