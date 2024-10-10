import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

all_urls = []
url = 'https://www.cnn.com'
data = requests.get(url).text
soup = BeautifulSoup(data, features="html.parser")
for a in soup.find_all('a', href=True):
    if a['href'] and a['href'][0] == '/' and a['href'] != '#':
        a['href'] = url + a['href']
    all_urls.append(a['href'])

# print(all_urls)

def url_is_article(url, current_year_start='2'):
    if url:
        if 'cnn.com/{}/'.format(current_year_start) in url and '/gallery/' not in url:
            return True
    return False

article_urls = [url for url in all_urls if url_is_article(url)]
article_urls=set(article_urls)
# print(article_urls)

CNN_data=list()

for url in article_urls:
    data = requests.get(url).text

    def return_text_if_not_none(element):
        if element:
            return element.text.strip()
        else:
            return ''

    def parse(html):
        soup = BeautifulSoup(html, features="html.parser")
        Title = return_text_if_not_none(soup.find('h1', {'class': 'headline__text'}))

        Summary_text = return_text_if_not_none(soup.find('p', {'class': 'paragraph'})) 
        lines = Summary_text.split('\n')
        if len(lines) > 3:
            lines = lines[:3]
            # Add an ellipsis to indicate truncation
            lines[-1] += " ..."
        Summary="".join(lines)
        url_list=list(url.split("/"))

        Publication_Date = dt.datetime(int(url_list[3]), int(url_list[4]), int(url_list[5])).date()
        # print(Publication_Date)
        Source="CNN"
        category=url_list[6]
        # print(category)
        if len(Summary)!= 0:
            CNN_data.append({'Title':Title,'Summary':Summary,'PublicationDate':Publication_Date,'Source':Source,'URL':url,'Category':category})
    parse(data)


def csv_CNN_data():
    df_IEX=pd.DataFrame(CNN_data)
    df_IEX.to_csv('./source/news_csv/CNN_news_data.csv', index=False)

csv_CNN_data()