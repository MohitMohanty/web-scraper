
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
from urllib import *

visited_urls = set()

def spider_url(url,keyword):
    try:
        response = requests.get(url)
        
    except:
        print(f"Request failed {url}")
        return

    if response.status_code == 200:
        soup = BeautifulSoup(response.content,'html.parser')
        #print(soup)
        a_tag = soup.find_all('a')
        urls=[]
        for tag in a_tag:
            href = tag.get("href")
            if href is not None and href !="":
                urls.append(href)
            #print(href)
        #for urlns in urls:
            #print(urlns)

        for i in urls:
            if i not in visited_urls:
                visited_urls.add(i)
                url_join = urljoin(url,i)
                if keyword in url_join.lower():
                    print(url_join)
                    spider_url(url_join,keyword)
            else:
                pass



url = input("Enter the URL? ")
keyword = input("Enter the keyword to search in URL? ")

spider_url(url,keyword)