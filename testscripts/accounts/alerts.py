

import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("http://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(4)
driver.find_element(By.XPATH,"//Button[normalize-space()='Click for JS Prompt']").click()
alertwindow = driver.switch_to.alert
print(alertwindow.text)
time.sleep(4)
alertwindow.send_keys("Welcome")
time.sleep(4)
alertwindow.accept()
time.sleep(4)
driver.find_element(By.XPATH,"//Button[normalize-space()='Click for JS Prompt']").click()
alertwindow = driver.switch_to.alert
print(alertwindow.text)
time.sleep(4)
alertwindow.send_keys("Welcome")
time.sleep(4)
alertwindow.dismiss()

