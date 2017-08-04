from urllib.request import urlopen
from urllib.request import Request
import requests



class HtmlDownloader():
    def download(self, url):
        headers = {
            'Referer':'http://music.163.com',
            'Host':'music.163.com',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        }        
        if url is None:
            return None
        else:
            req = Request(url, headers=headers)
            response = urlopen(req)
            if response.getcode() != 200:
                return None
            else:
                return response.read()
    def downloadJsonData(self, url):
        headers = {
            'Cookie': 'appver=1.5.0.75771',
            'Referer': 'http://music.163.com',
        }
        user_data = {
            'params': 'vRlMDmFsdQgApSPW3Fuh93jGTi/ZN2hZ2MhdqMB503TZaIWYWujKWM4hAJnKoPdV7vMXi5GZX6iOa1aljfQwxnKsNT+5/uJKuxosmdhdBQxvX/uwXSOVdT+0RFcnSPtv',
            'encSecKey': '46fddcef9ca665289ff5a8888aa2d3b0490e94ccffe48332eca2d2a775ee932624afea7e95f321d8565fd9101a8fbc5a9cadbe07daa61a27d18e4eb214ff83ad301255722b154f3c1dd1364570c60e3f003e15515de7c6ede0ca6ca255e8e39788c2f72877f64bc68d29fac51d33103c181cad6b0a297fe13cd55aa67333e3e5'
        }
        id = url[url.find('=')+1:]
        trueUrl = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s/?csrf_token=' % (id)
        try:
            r = requests.post(trueUrl, headers=headers, data=user_data)        
            if r.status_code == 200 and r.text.find('comments') != -1:
                return r.text
        except Exception as ex:
            print(ex)