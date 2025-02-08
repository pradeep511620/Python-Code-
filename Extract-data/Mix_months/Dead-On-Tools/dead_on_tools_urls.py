import requests                                                                                            
from bs4 import BeautifulSoup                                                                              
import time                                                                                                
from datetime import datetime                                                                              
                                                                                                           
from selenium import webdriver                                                                             
from selenium.webdriver.common.by import By                                                                
                                                                                                           
driver = webdriver.Chrome()                                                                                
mylst = [                                                                                                  
    'https://deadontools.com/collections/tool-belts',                                                      
    # 'https://deadontools.com/collections/jobsite-apparel',                                               
    # 'https://deadontools.com/collections/work-gear',                                                     
    # 'https://deadontools.com/collections/hand-tools',                                                    
                                                                                                           
]                                                                                                          
for url in mylst:                                                                                          
    r = requests.get(url)                                                                                  
    soup = BeautifulSoup(r.content, 'html.parser')                                                         
    driver.get(url)                                                                                        
    now = datetime.now()                                                                                   
                                                                                                           
    print("microsecond", now.microsecond)                                                                  
    current_time = now.strftime("%H:%M:%S:%MS")                                                            
    print("without for loop", current_time)                                                                
                                                                                                           
    url_links = driver.find_element(By.ID, "main-collection-product-grid")                                 
    href = url_links.find_elements(By.TAG_NAME, "a")                                                       
    print(len(href))                                                                                       
    for link in href:                                                                                      
        u_link = link.get_attribute('href')                                                                
        print("'"+u_link+"',")                                                                             
        print("Current Time =", current_time)                                                              
        now1 = datetime.now()                                                                              
        print('microsecond...', now1.microsecond)                                                          
