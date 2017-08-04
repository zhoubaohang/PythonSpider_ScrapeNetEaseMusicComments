#coding:utf8
import argparse
from spider_main import SpiderMain

def main():

    parser = argparse.ArgumentParser(description="通过链接抓取 网易云音乐 评论区评论")
    parser.add_argument("-l", "--link", help="爬取链接", dest="link")
    parser.add_argument("-d", "--dir", help="保存结果 html 文件的路径", dest="direction")
    args = parser.parse_args()
    url = args.link
    direction = args.direction
    if url is not None:   
        spider = SpiderMain()
        spider.craw(url, direction)
    
    
    

if __name__ == '__main__':
    main()