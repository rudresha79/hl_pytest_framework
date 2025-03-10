

import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

s = webdriver.Edge()

s.get("https://testautomationpractice.blogspot.com/")
s.maximize_window()
time.sleep(4)

allcheck = s.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")


#for x in allcheck:
    #x.click()

for i in range(len(allcheck)-2,len(allcheck)):
    allcheck[i].click()
time.sleep(4)

for x in allcheck:
    if x.is_selected():
       x.click()

time.sleep(4)



