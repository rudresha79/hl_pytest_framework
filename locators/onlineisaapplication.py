from selenium.webdriver.common.by import By


class obj_loc:

    # Main page
    lnk_stocksandsharesisa = (
    By.XPATH, "//nav[@aria-label='ISAs navigation']//span[@class='sn-link-text'][normalize-space()='Stocks and Shares ISA']", "Stocks and Shares ISA")
    # //nav[@aria-label='ISAs navigation']//span[@class='sn-link-text'][normalize-space()='Stocks and Shares ISA']
    lnk_openyourstocksandsharesisa = (By.XPATH, "//div[@class='heroPullout__content medium-hide small-hide']//a[@class='buttonPrimaryCta'][contains(text(),'Open')]", "Open your Stocks and Shares ISA")
    lnk_openyourisanow = (By.XPATH, "//button[@class='buttonPrimaryCta'][contains(text(),'Open')]", "Open your ISA now")

    lnk_my_accounts = (
        By.XPATH, "//button[normalize-space()='Accounts']", "Accounts")



    # Online IAS page

    header_onlineisaapplication = (By.XPATH, "//div[@class='cms-header-title']", "Stocks & Shares ISA")

    sel_fieldtitle = (By.ID, "fldTitle", "Select Name Dropdown")
    text_forename = (By.ID, "form_forename", "Forename")
    text_surname = (By.ID, "form_surname", "Surname")
    sel_dob = (By.ID, "form_date_of_birth", "Day")
    sel_dobmonth = (By.ID, "fldDob_Month", "Month")
    sel_dobyear = (By.ID, "fldDob_Year", "Year")
    chk_nonationalinsurancenumber = (By.ID, "form_no_nino", " I do not have a National Insurance number")
    rad_nationality_non = (By.ID, "non", "Non-UK")
   # sel_country = (By.XPATH, "//*[@ d='nationality-select']/select", "Country")
    sel_country = (By.XPATH, "/html/body/div[2]/div[2]/div/div/div[1]/div[1]/form/fieldset[2]/div[5]/div[2]/span/select", "Country")
    text_passportnumber = (By.XPATH, "/html/body/div[2]/div[2]/div[1]/div/div[1]/div[1]/form/fieldset[2]/div[5]/div[3]/div/span/input", "Passport Number")
    text_housenumber = (By.ID, "fldHouse", "House Number")
    text_postalcode = (By.ID, "fldPostcode", "Postal Code")
    text_emailaddress = (By.ID, "fldEmail", "Email Address")
    text_maintelephonenumber = (By.ID, "fldTel_eve:", "Main Telephone Number")
    text_mobiletelephonenumber = (By.ID, "fldTel_day:", "Mobile Telephone Number")
    sel_wheredidyouhear = (By.ID, "fldSource", "Where did you hear about us")
    rad_addmoney_addcash = (By.ID, "fldInvest_method_lump", "add cash 100")
    chk_personaldata_phone = (By.ID, "No_Phone", "Phone")
    lnk_openmyisa =  (By.ID, "next", "Open My IAS")





