# What is Web scraping?
#It's a way of reading other websites and extract information from it using automation techniques.
# It allows programmers to extract data from other websites. Python is one of the more popular
# languages for doing such tasks. It uses request api to request the data it needs from a web
# page using HTTP GET. This can also be used to get data from web apis or RESTful Services.

#Modules required for working with web scraping
'''
Request module for making HTTP requests to the desired website.
BeautifulSoup module for python that allows get the data from the desired web page.
'''

#Examples of applying scraping on some data.
import requests
import pandas as pd
from bs4 import BeautifulSoup
from numpy.ma.core import append


'''
url = 'http://www.bbc.com/news'

response = requests.get(url)

if response.status_code == 200:
    print('This page is available')
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('h2', class_='sc-1207bea1-3 cZBSCm')
    headlines_list = []
    for headline in headlines:
        headlines_list.append(headline.getText())

    df = pd.DataFrame(headlines_list)
    print(df)
else:
    print(f'This page is not available: Status Code {response.status_code}')
'''
###Reading REST API
# rest_url = 'http://localhost:1234/emplist'
# rest_response = requests.get(rest_url)
# if rest_response.status_code == 200:
#     data = rest_response.json()
#     for row in data:
#         print(row)

#Etiquettes to be followed while doing web scraping
'''
1. API Rate Limiting: When you are accessing web apis, there shall be a certain limit within a 
time frame for allowing anonymous access.
2. Ethical Scraping: U may have to check if the websites allows scraping. U can review tha 
website's terms of service or its robots.txt file
3. U should be able to handle prominent HTTP errors like 500, 404, 403 etc.
'''

def scrap_page(url, parser='html.parser'):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, parser)
        return soup
    else:
        print(f'Failed to get valid response. Status code: {response.status_code}')
        return None

def scrap_wiki():
    url = 'https://en.wikipedia.org/wiki/Web_scraping'
    soup = scrap_page(url)

    if soup:
        title = soup.find('h1', {'id': 'firstHeading'}).text
        print(f'Title: {title}')

        first_paragraph = soup.find('p').text
        print(f'Content: {first_paragraph}')

def scrap_flipkart():
    url = 'https://www.flipkart.com/search?q=Iphone'
    soup = scrap_page(url)
    if soup:
        containers = soup.find_all('div')
    else:
        print('Not available for scrapping')

scrap_flipkart()

#scrap_wiki()