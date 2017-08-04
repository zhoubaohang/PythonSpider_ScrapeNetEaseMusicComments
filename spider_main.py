#coding:utf-8
from url_downloader import HtmlDownloader
from html_parser import HtmlParser
from jsondata_parser import JsonData_Parser
from url_manager import UrlManager
from html_outputer import HtmlOutPuter

class SpiderMain():
    def __init__(self):
        self.urlDownLoader = HtmlDownloader()
        self.htmlParser = HtmlParser()
        self.urlManager = UrlManager()
        self.jsondataParser = JsonData_Parser()
        self.htmlOutPuter = HtmlOutPuter()
    def _get_from_discover_toplist(self, url):
        urls = self.htmlParser.parse(htmlContent=self.urlDownLoader.download(url), type='discover_toplist')
        self.urlManager.add_new_urls(urls)
    
    def _get_from_discover_artist(self, url):
        urls = self.htmlParser.parse(htmlContent=self.urlDownLoader.download(url), type='discover_artist')
        self.urlManager.add_new_urls(urls)
    
    def _get_from_artist(self, url):
        results = self.htmlParser.parse(htmlContent=self.urlDownLoader.download(url), type='artist')
        for name,urls in results.items():
            print(name)
            self.urlManager.add_new_urls(urls)
    
    def _get_from_song(self, url):
        tmp = {}
        name = self.htmlParser.parse(htmlContent=self.urlDownLoader.download(url), type='song')
        print("正收集："+name)
        comments = self.jsondataParser.parse(self.urlDownLoader.downloadJsonData(url))
        tmp[name] = comments
        self.htmlOutPuter.collect_datas(tmp)
        
    def _parse_url(self, url):
        res = ''
        SONG = 'song'
        DISCOVER = 'discover'
        ARTIST = 'artist'
        TOPLIST = 'toplist'
        if(url.find(DISCOVER) != -1):
            res += DISCOVER
        if(url.find(ARTIST) != -1):
            if(res != ''):
                res += '_'+ARTIST
            else:
                res += ARTIST
        if(url.find(TOPLIST) != -1):
            if(res != ''):
                res += '_'+TOPLIST
            else:
                res += TOPLIST
        if(url.find(SONG) != -1):
            res += SONG
        return res
    def craw(self, rootUrl, direction=""):
        if(rootUrl.find('#') != -1):
            pos = rootUrl.find('#')            
            rootUrl = rootUrl[:pos] + rootUrl[pos+2:]
        self.urlManager.add_new_url(rootUrl)
        while self.urlManager.has_new_url():
            url = self.urlManager.get_url()
            methodName = '_get_from_'+self._parse_url(url)
            method = getattr(self, methodName)
            if(method != None):
                method(url)                
        self.htmlOutPuter.output_html(direction=direction)
            