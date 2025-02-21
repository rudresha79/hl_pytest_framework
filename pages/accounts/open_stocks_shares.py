import time

from selenium.webdriver.common.by import By
from locators.onlineisaapplication import obj_loc as obj
from utils.utility import utility

class open_stocks_shares_isa:


    def __init__(self,driver):
        self.driver = driver
        self.lib = utility(self.driver)



    def a(self, url,title,forename,surname,dob,nationality,country,passport_number,house_number,postcode,email_address,main_telephone_number,mobile_telephone_number,where_did_you_hear_about_us,add_money,personal_data):

        self.lib.launch_browser(url)
        time.sleep(10)
        if self.driver.find_element(By.ID, "onetrust-accept-btn-handler").is_displayed():
            self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()


    def click_em(self):
        #2. Click on the "Accounts"
        self.lib.click_element(obj.lnk_my_accounts)

    def click_em1(self):
        # Select "Stocks and Shares ISA" from ISA's section.
        self.lib.click_element(obj.lnk_stocksandsharesisa)

    def click_em2(self):
        # 3. Click on "OPEN YOURS STOCKS AND SHARES ISA" link.
        self.lib.click_element(obj.lnk_openyourstocksandsharesisa)

