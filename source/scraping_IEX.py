import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
month_to_number = {
'January' : 1,         
'February' : 2,         
'March' : 3,           
'April' : 4,              
'May' : 5, 
'June' : 6,
'July' : 7, 
'August' : 8, 
'September' : 9, 
'October' : 10, 
'November' : 11, 
'December' : 12}
all_urls = []
url = 'https://indianexpress.com/'
data = requests.get(url).text
soup = BeautifulSoup(data, features="html.parser")
for a in soup.find_all('a', href=True):
    if a['href'] and a['href'][0] == '/' and a['href'] != '#':
        a['href'] = url + a['href']
    all_urls.append(a['href'])

# print(all_urls)

def url_is_article(url):
    if url:
        if '/article/' in url:
            return True
    return False

article_urls = [url for url in all_urls if url_is_article(url)]
article_urls=set(article_urls)
# print(article_urls)

IEX_data=list()

for url in article_urls:
    data = requests.get(url).text

    def return_text_if_not_none(element):
        if element:
            return element.text.strip()
        else:
            return ''
    # def p_date(date_text):
    #     parsed_date = parse(date_text)
    #     date_only = parsed_date.date()
    #     return date_only
    
    def parse(html):
        soup = BeautifulSoup(html, features="html.parser")
        Title = return_text_if_not_none(soup.find('h1',{'class':'native_story_title'}))

        Summary_text = return_text_if_not_none(soup.find('div',{'class':'story_details'}))
        lines = Summary_text.split('\n')
        if len(lines) > 2:
            lines = lines[:2]
            # Add an ellipsis to indicate truncation
            lines[-1] += " ..."
        Summary="".join(lines)
        p_date_text=return_text_if_not_none(soup.find('span',{'itemprop':'dateModified'}))
        date_list=list(p_date_text.split())

        if 'Updated:' in date_list:
            month_p=date_list[1]
            day=int(date_list[2][0])
            year=int(date_list[3])
        else:
            month_p=date_list[0]
            day=int(date_list[1][0])
            year=int(date_list[2])
        month_num= int([v for k, v in month_to_number.items() if month_p.lower() in k.lower()][0])
        # print(day,month_num,year)
        # Publication_Date = datetime(int(date_list[3].strip()), datetime.strptime(date_list[0].strip(), "%B").month, int(date_list[1].strip()))
        # date_lines = Publication_Date_text.split('\n')
        # Publication_Date=date_lines[-1].strip()
        Publication_Date=dt.date(year,month_num,day)
        # print(Publication_Date)
        Source="Indian Express"

        category=list(url.split("/"))[4]
        # print(category)
        IEX_data.append({'Title':Title,'Summary':Summary,'PublicationDate':Publication_Date,'Source':Source,'URL':url,'Category':category})
    parse(data)

def csv_IEX_data():
    df_IEX=pd.DataFrame(IEX_data)
    df_IEX.to_csv('./source/news_csv/IEX_news_data.csv', index=False)

csv_IEX_data()

