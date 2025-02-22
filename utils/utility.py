import csv
import getpass
import glob
import os
import time
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException, TimeoutException, ElementClickInterceptedException, NoAlertPresentException, UnexpectedAlertPresentException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

from testscripts.conftest import driver


class utility:

    default_timeout = 10
    def __init__(self, driver):
        self.driver = driver



    ################################################################-- LAUNCHBROWSER --##########################################################################################
    # Function:launchbrowser - Launches the browser and navigates to the URL
    # Parameters:
    #           url:https://preproductionpro.rantcell.com/
    #           title:https://preproductionpro.rantcell.com/
    # Revision History:

    def launch_browser(self, url):
        try:
            with allure.step(f"Launch the browser and navigate to {url}"):
                self.driver.get(url)
                self.driver.maximize_window()
                actual_url = self.driver.current_url  # Renamed for clarity

                if actual_url == url:  # Ensure exact match
                    screenshot_path = "screenshot.png"
                    self.driver.get_screenshot_as_file(screenshot_path)
                    allure.attach.file(screenshot_path, name=f"URL: {actual_url}",
                                       attachment_type=allure.attachment_type.PNG)
                else:
                    raise Exception(f"URL mismatch: Expected {url}, but got {actual_url}")

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="URL_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            pytest.fail(f"Failed to navigate to the URL {url}: {type(e).__name__} - {str(e)}")

    ##################################################################################################################################################################################

    ##################################################################-- click_element --##################################################################################################
    # Function:click - Clicks on particular element
    # Parameters:
    #           locators: (By.ID, self.textbox_username_id)
    # Revision History:
    def click_element(self, locators):

        locator_type = locators[0]

        locator_property = locators[1]

        element_name = locators[2]

        # Combine locator type and property into a tuple for Selenium

        selenium_locator = (locator_type, locator_property)

        with allure.step(f"Click on {element_name} element"):
            try:
                # Wait for the element to be clickable
                WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable(selenium_locator))
                # Find the element and click
                self.driver.find_element(locator_type, locator_property).click()
            except (NoSuchElementException, TimeoutException, ElementClickInterceptedException, StaleElementReferenceException) as e:
                # Attach a screenshot to the allure report if an exception occurs
                allure.attach(self.driver.get_screenshot_as_png(),name=f"{element_name}_screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
                # Fail the test with the exception message
                pytest.fail(f"Failed to click on {element_name}: {type(e).__name__} - {str(e)}")



    def handlecookes(self):
        if self.driver.find_element(By.ID, "acceptCookieButton").is_displayed():
            self.driver.find_element(By.ID, "acceptCookieButton").click()


    def click_hyperlink(self, link_name):
        with allure.step("Click on " + link_name + " link"):
            try:
                # Wait for the element to be clickable
                WebDriverWait(self.driver, self.default_timeout).until(EC.element_to_be_clickable(selenium_locator))
                # Find the element and click
                self.driver.find_element(locator_type, locator_property).click()
            except (NoSuchElementException, TimeoutException, ElementClickInterceptedException,
                    StaleElementReferenceException) as e:
                # Attach a screenshot to the allure report if an exception occurs
                allure.attach(self.driver.get_screenshot_as_png(), name=f"{link_name}_screenshot",
                              attachment_type=allure.attachment_type.PNG,
                              )
                # Fail the test with the exception message
                # pytest.fail(f"Failed to click on {element_name}: + type(exception).__name__ + {str(e)}")
                pytest.fail(f"Failed to click on {link_name}: {type(e).__name__} - {str(e)}")

    def mouse_hover(self, link_name):
        with allure.step("Click on " + link_name + " element"):
            try:
                web_ele_ment = self.driver.find_element(By.LINK_TEXT, link_name)
                if web_ele_ment.is_displayed():
                    time.sleep(2)
                    actions = ActionChains(web_ele_ment._parent)
                    actions.move_to_element(web_ele_ment)
                    actions.perform()
                    time.sleep(2)
            except Exception as e:
                allure.attach(self.driver.get_screenshot_as_png(), name=f"{link_name}_screenshot",
                              attachment_type=allure.attachment_type.PNG)
                pytest.fail(str(e))

    ##########################################################################################################################################################################################

    #################################################################-- input_text --###################################################################################
    # Function:input_text - Enters the value in Text Edit Field
    # Parameters:
    #           locators: (By.ID, self.textbox_username_id)
    #           value   : eva@rantcell.com
    # Revision History:

    def input_text(self, locators, value):
        locator_type = locators[0]
        locator_property = locators[1]
        element_name = locators[2]
        locators = locators[0], locators[1]
        with allure.step("Enter value in " + element_name + " edit field."):
            try:
                # Wait for the element to be clickable
                WebDriverWait(self.driver, self.default_timeout).until(EC.visibility_of_element_located(locators))
                # Find the element and enter the value
                self.driver.find_element(locator_type, locator_property).send_keys(value)
            except (NoSuchElementException, TimeoutException, ElementClickInterceptedException,
                    StaleElementReferenceException) as e:
                # Attach a screenshot to the allure report if an exception occurs
                allure.attach(self.driver.get_screenshot_as_png(), name=f"{element_name}_screenshot",
                              attachment_type=allure.attachment_type.PNG,
                              )
                # Fail the test with the exception message
                # pytest.fail(f"Failed to click on {element_name}: + type(exception).__name__ + {str(e)}")
                pytest.fail(f"Failed to enter the value in {element_name}: {type(e).__name__} - {str(e)}")

    ###################################################################################################################################################################################

    #####################################################################-- verify_element_is_present --############################################################################################
    # Function:verify_element_is_present - Verifies if a particular element is present or not
    # Parameters:
    #           locators: (By.XPATH, self.link_dashboard)
    #           elementName: Dashboard link
    # Revision History:

    def verify_element_is_present(self, locators):
        locator_type = locators[0]
        locator_property = locators[1]
        element_name = locators[2]
        locators = locators[0], locators[1]
        with allure.step("Verify " + element_name + " element/page is present "):
            try:
                # Wait for the element to be clickable
                WebDriverWait(self.driver, self.default_timeout).until(
                    EC.visibility_of_element_located(locators))
                ele_ment = self.driver.find_element(locator_type, locator_property)
                # Verify if the element is present
                if ele_ment.is_displayed:
                    allure.attach(self.driver.get_screenshot_as_png(), name=f"{element_name}_screenshot",
                                  attachment_type=allure.attachment_type.PNG)
            except (NoSuchElementException, TimeoutException, ElementClickInterceptedException,
                    StaleElementReferenceException) as e:
                # Attach a screenshot to the allure report if an exception occurs
                allure.attach(self.driver.get_screenshot_as_png(), name=f"{element_name}_screenshot",
                              attachment_type=allure.attachment_type.PNG,
                              )
                # Fail the test with the exception message
                # pytest.fail(f"Failed to click on {element_name}: + type(exception).__name__ + {str(e)}")
                pytest.fail(f"Failed to verify the element/value {element_name}: {type(e).__name__} - {str(e)}")

    ###############################################################################################################################################################
