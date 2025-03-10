import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.utility import utility



class work_sp3:


    work_side_bar_menu = (By.XPATH, "//p[@class='navbar_title small'][normalize-space()='work']", "Work Side Bar Menu")
    work_page = (By.XPATH, "//h1[text()='WORK']", "WORK")
    #asset_dropdown = (By.XPATH, "//*[@id='select2-lmk4-container']", "ASSET")
    asset_dropdown = (By.XPATH, "//*[@name='asset']", "ASSET")
    inspections_dropdown = (By.XPATH, "//*[@name='Inspection-Name-3']", "INSPECTIONS")
    inspect_now= (By.XPATH, "//div[@id='id_operations_inspection0']", "INSPECTIONS")
    performed_by = (By.XPATH, "//*[@id='performedBy']/select", "Performed By")
    submit_inspection_correction_action_page = (By.XPATH, "//h2[text()='Submit Inspection / Corrective Action']", "Submit Inspection / Corrective Action")
    test_description = (By.XPATH, "//*[@id='name00']", "Test Description")
    inspectable = (By.XPATH, "//*[@id='flag04']", "Inspectable")
    structure_pipe_to_soil_on = (By.XPATH, "//*[@id='structurePipeToSoilOn0']", "structure pipe to soil on")



    def __init__(self,driver):
        self.driver = driver
        self.lib = utility(self.driver)



    def select_work_side_bar_menu(self):
        self.lib.click_element(self.work_side_bar_menu)
    def verify_work_page(self):
        self.lib.verify_element_is_present(self.work_page)
        time.sleep(5)
    def select_item_from_asset_dd(self,item):
        self.lib.select_item_from_dropdown(self.asset_dropdown,item)
        time.sleep(2)
    def select_item_from_inspections_dd(self,item):
        self.lib.select_item_from_dropdown(self.inspections_dropdown,item)
        time.sleep(20)
    def click_inspect_now(self):
        self.lib.click_element(self.inspect_now)
    def verify_submit_inspection_correction_action_page(self):
        self.lib.verify_element_is_present(self.submit_inspection_correction_action_page)
        time.sleep(5)
    def select_performed_by(self,item):
        self.lib.select_item_from_dropdown_option(self.performed_by,item)
        # option = self.driver.find_element(By.XPATH, "//*[@id='performedBy']/select")
        # dropdown = Select(option)
        # dropdown.select_by_visible_text(item)
        #time.sleep(10)
    def select_test_description(self, item):
        self.lib.select_item_from_dropdown_option(self.test_description, item)
    def select_inspectable(self, item):
        self.lib.select_item_from_dropdown_option(self.inspectable, item)
    def enter_structure_pipe_to_soil_on(self,value):
        self.lib.input_text(self.structure_pipe_to_soil_on,value)
        time.sleep(10)


