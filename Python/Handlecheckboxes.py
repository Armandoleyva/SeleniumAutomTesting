import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#driver.implicitly_wait(10) # seconds  # implicit wait

# 1) select specific checkbox
#driver.find_element(By.XPATH,"//input[@id='thursday']").click()

#2) select all the checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes)) #7

#Appraoch1 - Ciclo for normal se guia por el indice
for i in range(len(checkboxes)):
     checkboxes[i].click()

#Appraoch2 -  lo mismo solo que se guia por la lista de elementos, mas pythonic
#for checkbox in checkboxes:
#    checkbox.click()


#3) select multiple checkboxes by choice
#for checkbox in checkboxes:
#     weekname = checkbox.get_attribute('id')
#     if weekname == 'friday' or weekname=='thursday':
#         checkbox.click()

#4 ) select last 2 checkboxes
# range(5,7) -->6,7
# totalnumberofelements-2=starting index - desde,hasta
#for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

#5) select first 4 checkboxes
#for i in range(len(checkboxes)):
#     if i<4:
#         checkboxes[i].click()

#6) clearing all the check boxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()


input("Presiona Enter para cerrar el navegador...")

driver.quit()