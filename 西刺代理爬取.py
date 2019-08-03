import requests
from lxml import etree

class Proxy(object):
    def __init__(self):
        self.url = 'https://www.xicidaili.com/wt/'
        self.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                        'Accept-Encoding':'gzip, deflate, br',
                        'Accept-Language':'zh-CN,zh;q=0.9',
                        'Connection':'keep-alive',
                        'Cookie':'free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWI5YWFkMWE2OGMyY2QxOTAyNThhMGNjN2M4ZTFiODE5BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWJhcWZhUkxEd2FOY3R4WGJ5ZVFZRjRjMnFMcFhuOWREMzVtaTlKSjcwdFE9BjsARg%3D%3D--0fd596152621e235cba6b3ba963c280e77415a55; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1564708082; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1564710061',
                        'Referer':'https://www.xicidaili.com/wt/1',
                        'Upgrade-Insecure-Requests':'1',
                        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
                        }
        #储存可用的代理
        self.proxies_list = []

    def get_page(self,url):
        response = requests.get(url,headers=self.headers)
        response.encoding = 'utf-8'
        html = response.text
        self.parse_page(html)

    def parse_page(self,html):
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath('//table[@id="ip_list"]/tr[position()>1]')
        for tr in tr_list:
            ip = tr.xpath('./td[2]/text()')[0].strip()
            port = tr.xpath('./td[3]/text()')[0].strip()
            an = tr.xpath('./td[5]/text()')[0].strip()
            if an == '高匿':
                b = 'http://%s:%s' % (ip,port)
                self.check_b(b)
    '''检查代理ip是否可用'''
    def check_b(self,b):
        url = 'http://music.taihe.com'
        proxies = {'http':b}
        try:
            response = requests.get(url, proxies=proxies, headers=self.headers)
            self.proxies_list.append(b)
            print(self.proxies_list)
        except Exception as e:
            print('代理不可用')

    def main(self):
        for i in range(1,21):
            url = self.url + str(i)
            self.get_page(url)


if __name__ == "__main__":
    proxy = Proxy()
    proxy.main()


