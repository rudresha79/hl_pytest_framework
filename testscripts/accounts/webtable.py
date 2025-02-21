from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()  # maximize window
table_element = driver.find_element(By.XPATH,"//table[@name='BookTable']")
no_of_rows = table_element.find_elements(By.TAG_NAME,'tr')
print(len(no_of_rows))
value_to_be_searched = "Mukesh"
for x in no_of_rows:
    if value_to_be_searched in x.text:
        no_of_columns = x.find_elements(By.TAG_NAME,"td")
        book_name =  no_of_columns[0].text
        subject_name = no_of_columns[2].text
        price = no_of_columns[3].text
        print(book_name + "-" + subject_name +  "-" + price)
        break
noOfColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(noOfColumns)