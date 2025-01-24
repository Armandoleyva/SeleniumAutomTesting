#Assignment
#-----------
#1) Open Web Browser(Chrome/firefox/IE).
#2) Open URL  https://admin-demo.nopcommerce.com/login
#3) Provide Email  (admin@yourstore.com).
#4) Provide password  (admin).
#5) Click on Login.
#	driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
#6) Capture title of the dashboad page.(Actual title)
#7) Verify title of the page: "Dashboard / nopCommerce administration" (Expected)
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

#2) Open URL  https://admin-demo.nopcommerce.com/login
driver.get("https://admin-demo.nopcommerce.com/login")
# Expande la ventana a pantalla completa
driver.fullscreen_window()

#3) Provide Email  (admin@yourstore.com).
driver.find_element(By.NAME, "Email").clear()
driver.find_element(By.NAME, "Email").send_keys("admin@yourstore.com")

#4) Enter password  (admin123).
driver.find_element(By.NAME, "Password").send_keys("admin")


#5) Click on Login.
driver.find_element(By.XPATH,"//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()

#6) Capture title of the dashboad page.(Actual title)
enc_title= driver.title
real_title = "Just a moment..."
    #7) Verify title of the page:
if enc_title==real_title:
    print("Login test passed")
else:
    print("Login test failed")


input("Presiona Enter para cerrar el navegador...")
driver.quit()