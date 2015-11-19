from bs4 import BeautifulSoup
import urllib2


def crawl_shop_html(shop):
    url = "http://www.dianping.com/shop/" + shop
    request = urllib2.Request(url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'content-type': 'charset=utf8'
    })
    req = urllib2.urlopen(request)
    html = req.read()
    # with open(r'C:\Users\howie\Desktop\a.html') as fp:
    #     html = fp.read()
    # print(html)
    return html


def parse_shop_html(html):
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.find_all('div')
    for div in divs:
        if div['class'][0] == 'main':
            shop_name = div.div.h1.text.strip().split()[0]
            print shop_name

        if div['class'][0] == 'breadcrumb':
            district = div.a
            print district.text.strip()

        if div['class'][0] == 'brief-info':
            # print div
            spans = div.find_all('span')
            print spans[1].text
            print spans[2].text
            print spans[3].text
        # if div['breadcrumb'] == 'body':
        #   print div
        #
        # if div['class'] == 'main':
        #   print div


shop = "5707165"
html = crawl_shop_html(shop)
parse_shop_html(html)


