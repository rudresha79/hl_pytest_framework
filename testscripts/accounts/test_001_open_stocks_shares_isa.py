import time

import pytest
from selenium.webdriver.common.by import By

from pages.accounts import open_stocks_shares_isa
from utils import read_test_data_from_excel as td
from config.config import Read_Config as conf
from   utils.utility import utility as lib

class Test_Open_Stocks_Shares_ISA:

    #driver = None

    @pytest.mark.parametrize("data", td.read_excel_test_data(conf.test_data_folder_rootpath,
                                                                     "Stocks and Shares ISA"))

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_stocks_shares_isa(self,setup,data):

        self.driver = setup

        url = data['URL']
        title = data['Title']
        forename = data['Forename']
        surname = data['Surname']
        dob = data['DOB']
        nationality = data['Nationality']
        country = data['Country']
        passport_number = data['PassportNumber']
        house_number = data['HouseNumber']
        postcode = data['PostCode']
        email_address = data['EmailAddress']
        main_telephone_number = data['MainTelephoneNumber']
        mobile_telephone_number = data['MobileTelephoneNumber']
        where_did_you_hear_about_us = data['Wheredidyouhearaboutus']
        add_money = data['AddMoney']
        personal_data = data['PersonalData']

        # lb = lib(self.driver)
        # lb.launch_browser(url)
        # time.sleep(10)
        #
        # if self.driver.find_element(By.ID, "onetrust-accept-btn-handler").is_displayed():
        #     self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

        self.a = open_stocks_shares_isa.open_stocks_shares_isa(self.driver)
        self.a.a(url,title,forename,surname,dob,nationality,country,passport_number,house_number,postcode,email_address,main_telephone_number,mobile_telephone_number,where_did_you_hear_about_us,add_money,personal_data)




