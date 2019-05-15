# import pandas as pd
# import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from time import sleep 
from selenium.webdriver.common.by import By
class scrape:
    def __init__(self,url,pages=10):
        driver = webdriver.Chrome() 
        driver.get(url)
        
        i = 0
        while i < pages:
            try:
                driver.find_element(By.XPATH,"//button[@data-aut-id='btnLoadMore']").click()
            except:
                print('unabl to load more')
                pass
            sleep(3)
            i = i+1
        #print(driver)
        soup = BeautifulSoup(driver.page_source)
        t = soup.findAll('li')
        links = []
        for i in t:
            if i.a and i.span:
                try:
                    links.append(i.a['href'])
                except:
                    pass
        self.item_links = []
        for i,val in enumerate(links):
            if val.split('/')[1] == 'item':
                self.item_links.append(val)
        return
        
        