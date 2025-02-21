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

        # 2. Click on the "Accounts"

        self.lib.click_element(obj.lnk_my_accounts)

        # Select "Stocks and Shares ISA" from ISA's section.

        self.lib.click_element(obj.lnk_stocksandsharesisa)

        # 3. Click on "OPEN YOURS STOCKS AND SHARES ISA" link.

        self.lib.click_element(obj.lnk_openyourstocksandsharesisa)

        # 4. Scroll Down the page and  Click on the "OPEN YOUR ISA NOW" link.

        self.lib.click_element(obj.lnk_openyourisanow)

        # Verify Online ISA Application Title is displayed

        self.lib.verify_element_is_present(obj.header_onlineisaapplication)

        # 5. Enter the data in below fields under the  ""Your detail"" section.
        # Name
        # DOB
        # Nationality
        # House number
        # Postcode
        # E mail address
        # Main telephone number
        # Mobile telephone number
        # Where did you hear about us.

        #self.lib.selectitemfromdropdownrlistbox(obj.sel_fieldtitle, title)

        var = self.driver.find_element(By.XPATH, "//input[@type='radio' and @value ='Mr']")

        var.click


        time.sleep(10)

        self.lib.input_text(obj.text_forename, forename)

        self.lib.input_text(obj.text_surname, surname)

        self.lib.input_text(obj.sel_dob, dob)

        self.lib.click_element(obj.chk_nonationalinsurancenumber)

        self.lib.click_element(obj.rad_nationality_non)

        time.sleep(2)

        #  lib.selectitemfromdropdownrlistbox(self.driver, obj.sel_country, country)

        time.sleep(2)

        # lib.inputtext(self.driver, obj.text_passportnumber, passport_number)

        # lib.inputtext(self.driver, obj.text_housenumber, house_number)

        # lib.inputtext(self.driver, obj.text_postalcode, postcode)

        # lib.inputtext(self.driver, obj.text_emailaddress, email_address)

        # time.sleep(2)

        # lib.inputtext(self, obj.text_maintelephonenumber, mobile_telephone_number)
        #
        # lib.inputtext(self, obj.text_mobiletelephonenumber, mobile_telephone_number)

        # lib.selectitemfromdropdownrlistbox(self.driver, obj.sel_wheredidyouhear, wheredidyouhearaboutus)

        time.sleep(5)

        # lib.click(self, obj.rad_addmoney_addcash)

        # lib.click(self, obj.chk_personaldata_phone)

        #lib.click(self.driver, obj.lnk_openmyisa)
