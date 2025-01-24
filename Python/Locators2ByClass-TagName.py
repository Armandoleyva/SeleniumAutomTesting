from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()  #maximize the browser window

sliders=driver.find_elements(By.CLASS_NAME,'homeslider-container')
print(len(sliders)) #5    total number of sliders on home page

links=driver.find_elements(By.TAG_NAME,'a')
print(len(links)) #  149 total number of links on home page


