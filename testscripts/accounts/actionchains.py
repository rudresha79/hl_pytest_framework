


from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver=webdriver.Edge()
webdriver.Chrome()



driver.get("https://www.ndtv.com/")
driver.maximize_window()
time.sleep(5)



a = driver.find_element(By.XPATH,"/html/body/div[4]/nav/div/div/div/nav/ul/li[5]/a")
b= driver.find_element(By.XPATH,"/html/body/div[4]/nav/div/div/div/nav/ul/li[5]/div/div/div/div/div[1]/ul/li[1]/a")

act=ActionChains(driver)
act.move_to_element(a).perform()
time.sleep(2)
b.click()
#act.context_click(b)
time.sleep(5)








