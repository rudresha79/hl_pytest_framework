import time
from selenium.webdriver.common.by import By
from utils.utility import utility


class register_name_a:
    def __init__(self,driver):
        self.driver = driver
        self.lib = utility(self.driver)


    title_registerforonlineaccess = (
        By.XPATH, "//h1[normalize-space() = 'Register for online access']", "Register for online access")
    rad_no = (By.XPATH, "//h1[normalize-space() = 'Register for online access']", "Register for online access")
    text_surname = (By.ID, "surname", "Surname")
    text_dateofbirth = (By.ID, "date-of-birth-alternative", "Date of Birth")
    text_email = (By.ID, "email", "Email")
    button_continue = (By.ID, "submit", "Continue")
    errort_message = (
        By.XPATH, "//p[contains(text(),'The details you entered were not recognised. Pleas')]", "Error Message")
    lnk_register = (By.XPATH, "//div[@class='websiteHeader sn-is-variant']//a[@class='sn-only-unauth'][normalize-space()='Register']", "Register")
    No_Radio_Button = (By.XPATH, '//label[@for="clientno_no" and @class="input-radio"]', "No")



    def lunch_browser(self,url):

        # 1. Open the "https://www.hl.co.uk/" website in the Chrome browser.

        self.lib.launch_browser(url)

        time.sleep(10)
        if self.driver.find_element(By.ID, "onetrust-accept-btn-handler").is_displayed():
            self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

    def click_register(self):

        # 2.Click on the Register link

        self.lib.click_element(self.lnk_register)


    def verify_registration(self):

        # 3. Verify Register for online access screen is displayed

        self.lib.verify_element_is_present(self.title_registerforonlineaccess)

        time.sleep(2)

    def click_radiobutton(self):

        # 4. Click on "No" button in the field "Do you know your client number"

        self.lib.click_element(self.No_Radio_Button)

        #5. Enter the fields mentioned below.
        # Last name
        # Date of birth
        # Email address.
    def enter_forename(self,surname):
        self.lib.input_text(self.text_surname,surname)

    def enter_dob(self,dob):

        self.lib.input_text(self.text_dateofbirth, dob)

    def enter_email(self, email):
        self.lib.input_text(self.text_email, email)

    def click_continue(self):

        #6. Then click on button "Continue".

        self.lib.click_element(self.button_continue)

    def verify_error_message(self):

        #7. Verify Error Message is displayed

        self.lib.verify_element_is_present(self.errort_message)
