# we need to install requests package through File-->Settings-->ProjectIntrepreter-->+--> requests

import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

allLinks=driver.find_elements(By.TAG_NAME,'a')
count=0


for link in allLinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url,"  is broken link")
        count+=1
    else:
        print(url,"   is valid link")

print("Total number of broken links:",count)

input("Presiona Enter para cerrar el navegador...")


driver.quit()
