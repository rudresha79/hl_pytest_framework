import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

s = webdriver.Edge()

s.get("https://testautomationpractice.blogspot.com/")

s.maximize_window()
time.sleep(4)

a = s.find_elements(By.TAG_NAME,"a")
count=0
for e in a:
    b = e.get_attribute('href')
    try:
        res1 = requests.head(b)
        if res1.status_code >= 400:
            print(b, "  is broken link")
            count += 1
        else:
            print(b, "   is valid link")
    except:
        var = None

print("Total number of broken links:", count)







