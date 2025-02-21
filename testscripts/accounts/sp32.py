import time


from selenium import webdriver
from selenium.webdriver.common.by import By

s = webdriver.Edge()

s.get("https://sp3test.claritysystemsinc.com/#/login")
s.maximize_window()
time.sleep(10)
s.find_element(By.ID,"name").send_keys("scott.inglis@clarity.com")
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
s.find_element(By.XPATH,"//p[@class='navbar_title small'][normalize-space()='team']").click()
time.sleep(5)
elements =  s.find_element(By.XPATH,"//span[@role='combobox']")
elements.click()
element =  s.find_element(By.XPATH,"//li[text()='Starflow Energies']")
element.click()

time.sleep(2)
dop = s.find_element(By.XPATH,"//*[@id='task-group-name']/span/span[1]/span")

d = ('Odorization Report','Odorization - Tank Inspection')

for i in range(len(d)):
    print(d[i])
    dop.click()
    time.sleep(2)
    dropdowns = s.find_elements(By.XPATH, "//*[@id='select2-task-group-name-results']/li")
    for x in dropdowns:
        if x.text == d[i]:
            x.click()
            time.sleep(2)
            break



# drop_down_lists = dropdown.find_elements(By.TAG_NAME,"li")
# time.sleep(10)
# for x in drop_down_lists:
#     print(x.text)
#     if x.text == 'Critical Bond':
#        x.click()
#        dop.click()
#     if x.text == 'Odorization - Tank Inspection':
#        x.click()
#        dop.click()







time.sleep(15)

s.find_element(By.XPATH,"//div[@class='navbar_icon logout w-embed']//*[name()='svg']").click()

