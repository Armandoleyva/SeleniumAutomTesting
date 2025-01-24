#Test Case
#-----------
#1) Open Web Browser(Chrome/firefox/Edge).
#2) Open URL  https://opensource-demo.orangehrmlive.com/
#3) Enter username  (Admin).
#4) Enter password  (admin123).
#5) Click on Login.
#6) Capture title of the home page.(Actual title)
#7) Verify title of the page: OrangeHRM    (Expected)
#8) close browser

#Access to all methods
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager



#1) Choosing a chrome browser
#driver = webdriver.Chrome(executable_path="C:/Users/arman/OneDrive/Desktop/chromedriver/chromedriver.exe")
service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service)

#2) Open URL  https://opensource-demo.orangehrmlive.com/
driver.get("https://opensource-demo.orangehrmlive.com/")
# Expande la ventana a pantalla completa
driver.fullscreen_window()
# Define el WebDriverWait
wait = WebDriverWait(driver, 3)  # Espera hasta 3 segundos

#3) Enter username  (Admin).
#Selenium 3.9 hacia abajo "driver.find_element_by_name("username").send_keys("Admin")"
elemento = wait.until(EC.presence_of_element_located((By.NAME, "username")))
# Luego de encontrarlo, interactúa con el elemento
elemento.send_keys("Admin")

#4) Enter password  (admin123).
driver.find_element(By.NAME, "password").send_keys("admin123")


#5) Click on Login.
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button")))
# Haz clic en el botón
button.click()#driver.find_element_by_class_name("oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()

#6) Capture title of the home page.(Actual title)
enc_title= driver.title
real_title = "OrangeHRM"

if enc_title==real_title:
    print("Login test passed")
else:
    print("Login test failed")


input("Presiona Enter para cerrar el navegador...")
driver.quit()








