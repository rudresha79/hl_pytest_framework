
import pytest
from selenium import webdriver


driver = None

@pytest.fixture(scope="function")
def setup(request):
    browser_name = request.config.getoption("--browser").lower()
    global driver
    if browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "chrome":
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="edge", help="Choose browser: chrome, firefox, edge"
    )

def pytest_collection_modifyitems(items):
    for item in items:
        if "skip" in item.name:
            item.add_marker(pytest.mark.skip(reason="Skipping test as per hook logic"))
