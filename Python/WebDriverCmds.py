from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Open Web Browser(Chrome/firefox/Edge).
service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service)

# Open URL  https://www.nopcommerce.com/es/demo
driver.get("https://www.youtube.com")
driver.maximize_window()

#1) Application commands======================================================================================

#print(driver.title)
#print(driver.current_url)
#print(driver.page_source)

#2) Conditional commands=======================================================================================
#Estos son para identificar webelements, como textbox, etc.

#is_displayed()     #is_enabled()
#searchbox = driver.find_element(By.XPATH, "//*[@id='search-container']")
#print(searchbox.is_displayed())
#print(searchbox.is_enabled())

#is_selected() Esto es mas para radio buttons/checkboxes
# botones de esos por ejemplo hombre mujer
# y tienes que seleccionar uno

#rd_male=driver.find_element(By.XPATH,"un xpath de male")
#rd_female=driver.find_element(By.XPATH,"otro xpath de female")

#print("Default status") #
#print(rd_male.is_selected())
#print(rd_female.is_selected())

#rd_male.click()

#print("Current status")  #Aqui ya se muestra en True el state del rd_male de que esta seleccionado
#print(rd_male.is_selected())
#print(rd_female.is_selected())

#3) Browser commands=============================================================================================

#driver.close() #Este cierra una ventana solamente por ejemplo si un click lo manda a otra solo cierra la actual
#driver.quit() #Este mata el proceso, cierra todas las ventanas,


#4) Navigational commands============================================================================================
#back()
#forward()
#refresh()

#Bueno aqui se tripeo el Indio y empezo a explicar findelement() y findelements() ==================================

#1)Locator matching with single webelement
# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Apple MacBook Pro 13-inch")

#2) Locator matching with multiple webelements
# element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)  #prints first link from the footer "Sitemap"

#3) Element not available then throw NoSuchElementException
# login_element=driver.find_element(By.LINK_TEXT,"Log")
# login_element.click()

#######   find_elements() - Returns multiple webElements

#1)Locator matching with single webelement
# elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))  #1
# elements[0].send_keys("Apple MacBook Pro 13-inch")

#2) Locator matching with multiple webelements
# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements))  #23
# #print(elements[0].text) #Sitemap
# for ele in elements:
#     print(ele.text)

#3) Element not available - zero(Que no hay resultados con log ps)
elements=driver.find_elements(By.LINK_TEXT,"Log")
print("elementws returend:",len(elements))

#text Vs get_attribute('value') =====================================================================================

#text -----> regresa lo que hay dentro de un text box si es que hay algo
#get_attribute() ----> returns values of any attribute of web element
# emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
#
# emailbox.clear()
# emailbox.send_keys("abc@gmail.com")
#
# print("result of text:",emailbox.text)  # printed nothing
# print("result of get_attribute():",emailbox.get_attribute('value')) #abc@gmail.com





