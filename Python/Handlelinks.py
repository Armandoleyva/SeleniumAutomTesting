import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# click on link
oneclick = driver.find_element(By.LINK_TEXT,"merrymoonmary")
oneclick.click()

#Find number of links in a page
links = driver.find_elements(By.TAG_NAME,'a')
print("total number of links:", len(links))

# print all the link names, el .text es para imprimir el texto en la etiqueta "a"
for el in links:
    print(el.text)



input("Presiona Enter para cerrar el navegador...")


driver.quit()