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

time.sleep(2)
ele = s.find_elements(By.XPATH,"//*[@id='email-form-2']/div")
i=0
found_flag = False
for e in ele:
    i = i + i
    if "shelby" in e.text:
         print(e.text)
         a = e.find_elements(By.TAG_NAME, 'img')
         for w in a:
            print(w.get_attribute("src"))
            if w.get_attribute("src")=="https://sp3test.claritysystemsinc.com/assets/images/sp3-arrow-down.svg":
                 s.execute_script("arguments[0].scrollIntoView();", w)
                 w.click()
                 found_flag = True
                 break
         if found_flag:
             break
         original_style = e.get_attribute("style")
         s.execute_script(
             "arguments[0].setAttribute(arguments[1], arguments[2])",
              e,
              "style",
              "border: 2px solid red; border-style: dashed;")


time.sleep(5)
for e in ele:
    if "shelby" in e.text:
        b = e.find_elements(By.XPATH, '//div[starts-with(@class,"inside-white-container")]')
        for d in b:
            #print(d.text)
            q = d.find_elements(By.TAG_NAME, 'img')
            for z in q:
                print(z.get_attribute("src"))
                if z.get_attribute("src") == "https://sp3test.claritysystemsinc.com/assets/images/sp3-arrow-down.svg":
                    s.execute_script("arguments[0].scrollIntoView();", z)
                    z.click()
                    time.sleep(1)
                    str_value = d.text
                    print(str_value)
                    s.execute_script("arguments[0].scrollIntoView();", d)
                    time.sleep(1)

            # if "Odorization Report" in s.text:
            #   print(s.text)
            #   q = s.find_elements(By.TAG_NAME, 'img')
            #   for z in q:
            #       print(z.get_attribute("src"))
            #       if z.get_attribute("src") == "https://sp3test.claritysystemsinc.com/assets/images/sp3-arrow-down.svg":
            #           z.click()
            # if "Critical Bonds" in s.text:
            #   print(s.text)
            #   q = s.find_elements(By.TAG_NAME, 'img')
            #   for z in q:
            #       print(z.get_attribute("src"))
            #       if z.get_attribute("src") == "https://sp3test.claritysystemsinc.com/assets/images/sp3-arrow-down.svg":
            #           z.click()
time.sleep(15)

s.find_element(By.XPATH,"//div[@class='navbar_icon logout w-embed']//*[name()='svg']").click()

