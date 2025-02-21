import pytest
from selenium import webdriver


driver = None

@pytest.fixture(scope="function")
def setup():
    global driver
    driver = webdriver.Edge()

    # if browser == "chrome":
    #     from selenium.webdriver.chrome.service import Service
    #     serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    #     driver = webdriver.Chrome(service=serv_obj)
    # elif browser == "edge":
    #     from selenium.webdriver.edge.service import Service
    #     serv_obj = Service("C:\\Drivers\\edgedriver_win64\\msedgedriver.exe")
    #     driver = webdriver.Edge(service=serv_obj)
    # elif browser == "firefox":
    #     from selenium.webdriver.firefox.service import Service
    #     serv_obj = Service("C:\\Drivers\\geckodriver-v0.29.1-win64\\geckodriver.exe")
    #     driver = webdriver.Firefox(service=serv_obj)
    # return driver


    yield driver
    driver.quit()


# def pytest_adaption(parser):
#     parser.adoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")


