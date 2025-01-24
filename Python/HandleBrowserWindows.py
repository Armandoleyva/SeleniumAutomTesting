from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install()) 
driver = webdriver.Chrome(service=service)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# windowid=driver.current_window_handle
# print(windowid) #CDwindow-24CFB4FFB7CB60C7309293A9217B9F2A
#                 #CDwindow-E7283DA0F55EF107A63C1CD349434080

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowsIDs=driver.window_handles

#Approach1
# parentwindowid=windowsIDs[0] #CDwindow-A82AD2C060A4BBCAFAD3DF3C6172CCBE
# childwindowid=windowsIDs[1] #CDwindow-F63E2A3D2324F7132FFD60C9A8E16A95
# #print(parentwindowid,childwindowid)
#
# driver.switch_to.window(childwindowid)
# print("title of the child window",driver.title)
#
# driver.switch_to.window(parentwindowid)
# print("title of the parent window",driver.title)

#Approach2

# for winid in windowsIDs:
#     driver.switch_to.window(winid)
#     print(driver.title)

time.sleep(3)

#Close specific browser windows   1 2 3
for winid in windowsIDs:
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM HR Software | Free HR Software | HRMS | HRIS" or driver.title=='XYZ':
        driver.close()