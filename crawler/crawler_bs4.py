import csv
import logging
import urllib.request
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


logging.basicConfig(#filename='crawler_bs4.log',
                    format='%(asctime)s %(levelname)s:%(message)s',
                    level=logging.INFO)

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'
headers = {'User-Agent': user_agent}


class Crawler:

    def __init__(self, urls=None):
        if urls is None:
            urls = []
        self.csv_address = 'result/bs4.csv'
        self.visited_urls = []
        self.urls_to_visit = urls

    def download_url(self, url):
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        return response.read()

    def get_linked_urls(self, url, html):
        urls = []
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            #yield path
            urls.append(path)
        return urls

    def add_url_to_visit(self, url):
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)

    def crawl(self, url):
        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_url_to_visit(url)

    def save(self, urls):
        cw = csv.writer(open(self.csv_address, 'w'))
        for url in list(urls):
            cw.writerow([url])

    def run(self):
        while self.urls_to_visit and len(self.visited_urls) <= 10:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)
        self.save(self.visited_urls)


if __name__ == '__main__':
    Crawler(urls=['https://www.imdb.com/']).run()
