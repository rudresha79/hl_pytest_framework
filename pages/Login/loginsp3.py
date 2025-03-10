import time

from selenium.webdriver.common.by import By

from utils.utility import utility



class login_sp3:


    company_dropdown = (By.XPATH, "//span[@role='combobox']", "Company Dropdown")

    def __init__(self,driver):
        self.driver = driver
        self.lib = utility(self.driver)



    def launch_browser(self,url):

        self.lib.launch_browser(url)

    def enter_user(self,user):

        text_user = (By.ID, "name", "User Name")

        self.lib.input_text(text_user,user)

    def click_login_user(self):

        button_login = (By.ID, "emailSubmit", "Login")

        self.lib.click_element(button_login)

    def enter_password(self, password):

        text_password = (By.ID, "password", "Password")

        self.lib.input_text(text_password, password)

    def click_login_password(self):
        button_login = (By.ID, "passwordSubmit", "Login")
        self.lib.click_element(button_login)

    def enter_otp(self, otp):
        text_otp = (By.ID, "otp", "OTP")
        self.lib.input_text(text_otp, otp)

    def click_login_otp(self):
        button_login = (By.ID, "otpSubmit", "Login")
        self.lib.click_element(button_login)

    def verify_home_page(self):
        #button_login = (By.XPATH, "//h1[@class ='hero_heading ng-tns-c189-1']", "Home Page")
        button_login = (By.XPATH, "//h1[text()='HOME']", "Home Page")
        self.lib.verify_element_is_present(button_login)

    def click_company_dropdown(self,company):
        time.sleep(5)
        self.lib.click_element(self.company_dropdown)
        company_list_var = "//li[text()='" + company + "']"
        company_list = (By.XPATH, company_list_var, "Web List item")
        self.lib.click_element(company_list)
        time.sleep(5)









