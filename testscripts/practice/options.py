



import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s = webdriver.Edge()

s.get("https://www.opencart.com/index.php?route=account/register")
s.maximize_window()
time.sleep(20)

option = s.find_element(By.XPATH,"//*[@id='input-country']")
dropdown=  Select(option)

dropdown.select_by_visible_text("India")


# capture all the options and print them
alloptions=dropdown.options
print("total number of options:",len(alloptions))

# for opt in alloptions:
#     print(opt.text)

# select option from dropdown without using built-in method
# for opt in alloptions:
#     if opt.text=="India":
#         opt.click()
#         break

allOptions=s.find_elements(By.XPATH,'//*[@id="input-country"]/option')
print(len(allOptions))

for x in allOptions:
    print(x.text)





