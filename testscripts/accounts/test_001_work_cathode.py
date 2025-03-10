import time

import pytest

from pages.Login import loginsp3 as login
from pages.work import work as work


class Test_Open_Stocks_Shares_ISA:

    #driver = None

    data_cathod = [('https://sp3test.claritysystemsinc.com/#/login','aravind@claritysystemsinc.com','1111','1')]


    @pytest.mark.parametrize("data", data_cathod)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_work_cathode(self,setup,data):

        self.driver = setup

        url= data[0]
        user= data[1]
        password = data[2]
        token = data[3]

        self.a = login.login_sp3(self.driver)

        # Login to SP3 application

        self.a.launch_browser(url)

        self.a.enter_user(user)

        self.a.click_login_user()

        self.a.enter_password(password)

        self.a.click_login_password()

        self.a.enter_otp(token)

        self.a.click_login_otp()

        self.a.verify_home_page()

        #select company

        self.a.click_company_dropdown("Walters Resources")

        self.work = work.work_sp3(self.driver)

        self.work.select_work_side_bar_menu()

        self.work.verify_work_page()

        #select an item from ASSET drop down

        self.work.select_item_from_asset_dd("CA GAS")

        # select an item from inspections drop down

        self.work.select_item_from_inspections_dd("Cathodic Protection Survey")

        #click inspect now

        self.work.click_inspect_now()

        self.work.verify_submit_inspection_correction_action_page()

        self.work.select_performed_by("Aravind FI")

        self.work.select_test_description("CA")

        self.work.select_inspectable("Yes")

        self.work.enter_structure_pipe_to_soil_on("12.22")


















