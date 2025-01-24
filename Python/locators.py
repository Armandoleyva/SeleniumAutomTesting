from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


#1) Open Web Browser(Chrome/firefox/Edge).
service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service)

#2) Open URL  https://opensource-demo.orangehrmlive.com/
driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()

# id & name locators =============================================================================================
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")


# linktext & partial linktext ======================================================================================
#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()


#Aqui podemos ver cuantos sliders hay By.ClassName =================================================================
#sliders = driver.find_elements(By.CLASS_NAME,"item-box")
#print(len(sliders))

#Aqui podemos ver cuantos links hay By_TagName =====================================================================
#links = driver.find_element(By.TAG_NAME,"a")
#print(len(links))

#CSS selector Tag and ID ============================================================================================
#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc@gmail.com"

#CSS selector Tag and Class =========================================================================================
#driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc@gmail.com")

#CSS selector Tag and attribute ======================================================================================
#driver.find_element(By.CSS_SELECTOR,"[name=email]").send_keys("abc@gmail.com")
#driver.find_element(By.CSS_SELECTOR,"input[name=email]").send_keys("abc@gmail.com")

#Localizar elementos Tag, Class, attrib =============================================================================
#driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("abc@gmail.com") #Email
#driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("abc") #Password
