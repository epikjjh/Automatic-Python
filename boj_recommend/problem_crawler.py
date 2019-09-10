import requests
from bs4 import BeautifulSoup


class CrawlProblem:
    def __init__(self):
        self.url = 'https://www.acmicpc.net/problemset'
        ret = requests.get(self.url)
        if ret.status_code == 200:
            html = ret.text
        else:
            print("Invalid url")
            exit() 
        soup = BeautifulSoup(html, 'html.parser')
        self.page_num = len(list(soup.find('ul', {'class': 'pagination'}).children))
    
    def crawl_