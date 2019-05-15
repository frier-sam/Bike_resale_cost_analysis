# import pandas as pd
# import requests
import time
import re
import pandas as pd
import requests
from bs4 import BeautifulSoup
import random
from tqdm import tqdm
class scrape:
    def __init__(self,links,periodic_time=False,stime=2):
        self.scraped_data=[]
        for i in tqdm(range(0,len(links))):
            #sleep time
            if periodic_time:
                time.sleep(stime)
            else:
                time.sleep(random.randint(1,10))
            
            #url phrase and scrape
            try:
                url = 'https://www.olx.in' + links[i]
                t = requests.get(url)
                soup = BeautifulSoup(t.text)
                brand = soup.find("span", {"data-aut-id" : "value_make"}).text
                model = soup.find("span", {"data-aut-id" : "value_model"}).text
                year = soup.find("span", {"data-aut-id" : "value_year"}).text
                kms = soup.find("span", {"data-aut-id" : "value_mileage"}).text
                description = soup.find("div", {"data-aut-id" : "itemDescriptionContent"}).text
                location = soup.find("div", {"data-aut-id" : "itemLocation"}).text
                date = soup.find("div", {"data-aut-id" : "itemCreationDate"}).text
                price = soup.find("span", {"data-aut-id" : "itemPrice"}).text
                self.scraped_data.append([brand,model,year,re.sub("\D", "", kms),re.sub("\D", "", price),description,location,date])
#                 print('{} is done'.format(i))
            except:
                print('{} is not available'.format(i))
            
                
        