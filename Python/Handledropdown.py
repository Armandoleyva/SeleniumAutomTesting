import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10) # seconds  # implicit wait

#drpcountry_ele=driver.find_element(By.XPATH,"//*[@id='comboBox']")
drpelement = driver.find_element(By.XPATH, "//*[@id='comboBox']")
#ahora  = Select(drpelement)

drpelement.click()  # Abre el dropdown
option = driver.find_element(By.XPATH, "//*[@id='dropdown']/div[29]")
option.click()
#drpbar = ahora.select_by_visible_text("Item 10")

input("Presiona Enter para cerrar el navegador...")


driver.quit()