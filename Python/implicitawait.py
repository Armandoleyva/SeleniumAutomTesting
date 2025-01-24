from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


#el de por defecto es el time.sleep(5) pero este wait es de python no de selenium y no es muy practico
service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10) # seconds  # implicit wait

driver.get("https://www.google.com/")
driver.maximize_window()

searchbox=driver.find_element(By.NAME,'q')

searchbox.send_keys("Selenium")
searchbox.submit()


driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

input("Presiona Enter para cerrar el navegador...")
driver.quit()