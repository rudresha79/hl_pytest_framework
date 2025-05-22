import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

options = UiAutomator2Options()
options.platform_name = "Android"
#options.device_name = "8TCUKBW8JZJBAMDI"
options.device_name = "emulator-5554"
#options.app_package = "com.application.zomato"
#options.app_package = "com.application.zomato"
options.app_package = "com.whatsapp"
options.app_activity = "com.whatsapp.HomeActivity"  # Adjust based on your app
#options.app_activity = "com.application.zomato.login.ZomatoActivity"  # Adjust based on your app
options.automation_name = "UiAutomator2"
options.uiautomator2ServerInstallTimeout = 60000  # Increase timeout
options.noReset = True


driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(3)
driver.find_element(By.ID,"next_button").click()
time.sleep(3)
driver.find_element(By.ID,"eula_accept").click()

#driver.swipe()
#time.sleep(3)
#driver.find_element(By.ID,"registration_phone").send_keys("9980567894")

time.sleep(15)
driver.quit()