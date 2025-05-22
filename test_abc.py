import pytest

from utils import read_test_data_from_excel as td
from pages.register import register_name as rg
from config.config import Read_Config as conf
from conftest import setup



class Test_Register_Online:
    driver = None

    @pytest.mark.parametrize("data", td.read_excel_test_data(
        conf.test_data_folder_rootpath, "Register"))
    def test_reg_online(self, setup, data):

        print(data)
        self.driver = setup
        url = data['URL']


        a = rg.register_name_a(self.driver)

        a.lunch_browser(url)

        a.click_register()

        a.verify_registration()
