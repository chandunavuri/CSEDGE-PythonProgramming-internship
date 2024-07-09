import csv
import json

import requests
from bs4 import BeautifulSoup


def website_scraper(url,output='csv'):
    response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    info=[]
    columns=soup.find_all('h2',class_='columns')
    for column in columns:
        info.append(column.text.strip())
    if output=='csv':
        with open('output.csv','w',newline='',encoding='utf-8') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(['column'])
            for packet in info:
                writer.writerow([info])
        print("Information has been saved as output.csv")
    elif output=='json':
        with open('output.json','w',encoding='utf-8') as jsonfile:
            json.dump(info,jsonfile,ensure_ascii=False,indent=4)
        print("Information has been saved to output.json")
    else:
        print("Invalid output format.Select Format:('Json'/'csv')")
website_scraper('https://en.wikipedia.org/wiki/Cricket',output='csv')
website_scraper('https://en.wikipedia.org/wiki/Cricket',output='json')