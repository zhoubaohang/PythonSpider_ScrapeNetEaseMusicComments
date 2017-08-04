from bs4 import BeautifulSoup as bs

head = 'http://music.163.com'

class HtmlParser():
    def from_artist(self, htmlContent):
        res = {}
        songs = set()
        main_page = bs(htmlContent, 'html5lib')
        name = main_page.find('h2',{'id':'artist-name'}).getText()
        links = main_page.find_all('a')
        for link in links:
            url = link['href']
            if(url.find('song') != -1):
                songs.add(head+url)     
        res[name] = songs
        return res

    def from_song(self, htmlContent):
        main_page = bs(htmlContent, 'html5lib')
        name = main_page.find('em')
        return name.getText()
    
    def from_discover_artist(self, htmlContent):
        res = set()
        main_page = bs(htmlContent, 'html5lib')
        tags = main_page.findAll('a', {'class':'msk'})
        for tag in tags:
            res.add(head+tag['href'])
        return res
    
    def from_discover_toplist(self, htmlContent):
        res = set()
        main_page = bs(htmlContent, 'html5lib')
        tags = main_page.findAll('a')
        for tag in tags:
            name = tag['href']
            if(name.find('song') != -1):
                res.add(head+name)
        return res
    
    def parse(self, htmlContent, type):
        method = getattr(self, 'from_'+type)
        if method != None:
            return method(htmlContent)
            