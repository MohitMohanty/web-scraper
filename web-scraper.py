import requests
from bs4 import BeautifulSoup

def get_page(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content,'html.parser')

    #print(soup.find_all("a"))
    a_tag = soup.find_all("a")

    for tag in a_tag:
        print(tag.get("href"))

get_page(input("Enter the Url link for scrapping? "))    
