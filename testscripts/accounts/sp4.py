import time


from selenium import webdriver
from selenium.webdriver.common.by import By

s = webdriver.Edge()

s.get("https://sp3test.claritysystemsinc.com/#/login")
s.maximize_window()
time.sleep(10)
s.find_element(By.ID,"name").send_keys("aravind@claritysystemsinc.com")
time.sleep(0.5)
s.find_element(By.ID,"emailSubmit").click()
time.sleep(1)
s.find_element(By.ID,"password").send_keys("1111")
time.sleep(1)
s.find_element(By.ID,"passwordSubmit").click()
time.sleep(1)
s.find_element(By.ID,"otp").send_keys("1")
time.sleep(1)
s.find_element(By.ID,"otpSubmit").click()
time.sleep(15)

elements =  s.find_element(By.XPATH,"//span[@role='combobox']")
elements.click()
element =  s.find_element(By.XPATH,"//li[text()='Walters Resources']")
element.click()
time.sleep(5)

s.find_element(By.XPATH,"//p[@class='navbar_title small'][normalize-space()='work']").click()
time.sleep(10)






dop = s.find_element(By.XPATH,"//*[@name='asset']")
dop.click()
time.sleep(15)

s.find_element(By.XPATH,"//div[@class='navbar_icon logout w-embed']//*[name()='svg']").click()

