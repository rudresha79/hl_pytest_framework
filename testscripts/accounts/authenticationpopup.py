import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
#http://the-internet.herokuapp.com/basic_auth
#syntax: http://username:password@test.com
#Example: http://admin:admin@the-internet.herokuapp.com/basic_auth
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(4)


