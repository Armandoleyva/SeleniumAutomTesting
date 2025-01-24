from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#1) Open Web Browser(Chrome/firefox/Edge).
service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service)

#2) Open URL
driver.get("https://youtube.com/")

driver.maximize_window()

#Absolute Xpath
#driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("holahellow")
#driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button").click()

#Relative Xpath
#driver.find_element(By.XPATH,"//input[@id='search']").send_keys("hellowjona")
#driver.find_element(By.XPATH, "//*[@id='search-icon-legacy']").click()

#or  and
# driver.find_element(By.XPATH,"//input[@id='search_query_top' or @name='search_query' ]").send_keys("T-shirts")
# driver.find_element(By.XPATH,"//button[@name='submit_search' and @class='btn btn-default button-search']").click()
driver.find_element(By.XPATH,"//input[@id='search' or @name='search_query']").send_keys("xpath ejes axes explicacion")
driver.find_element(By.XPATH,"//button[@id='search-icon-legacy' and @class='style-scope ytd-searchbox']").click()

#contains()   & start-with() En resumen, contains() se usa cuando deseas buscar un texto dentro de un atributo,
# mientras que starts-with() se usa cuando deseas buscar un texto que comienza con cierto prefijo en un atributo.

# driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("T-shirts")
# driver.find_element(By.XPATH,"//button[starts-with(@name,'submit_')]").click()

#text()
#driver.find_element(By.XPATH,"//a[text()='Women']").click()


