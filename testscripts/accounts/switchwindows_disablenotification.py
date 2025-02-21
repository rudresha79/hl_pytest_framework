import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

a = webdriver.EdgeOptions()
a.add_argument("--disable-notifications")


driver = webdriver.Edge(a)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='HTML4']/div[1]/button").click()
time.sleep(2)



#After opening all the pages, capture windowid's
windowIds=driver.window_handles
b= ''
i = 0
print("Switching to each browser window and getting the titles........")
for windowid in windowIds:
    if i == 0:
        b = windowid
        print(b)
    i=i+1
    driver.switch_to.window(windowid)
    print(driver.title)
    time.sleep(2)

driver.switch_to.window(b)
time.sleep(5)


driver.quit()